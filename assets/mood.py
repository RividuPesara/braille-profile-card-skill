import json
import os
import urllib.request
from datetime import datetime, timezone

SLEEP_QUIET_DAYS = 14
DAYS_PER_WEEK = 7
MIN_COMPARED_WEEKS = 10
BUSY_SHARE_DENOMINATOR = 10
QUERY = '''query ($login: String!) { user(login: $login) { contributionsCollection {
  contributionCalendar { weeks { contributionDays { date contributionCount } } } } } }'''


def fetch_days(login, token):
    request = urllib.request.Request(
        'https://api.github.com/graphql',
        data=json.dumps({'query': QUERY, 'variables': {'login': login}}).encode(),
        headers={'Authorization': f'bearer {token}', 'Content-Type': 'application/json'},
    )
    with urllib.request.urlopen(request) as response:
        body = json.load(response)
    if 'errors' in body:
        raise RuntimeError(body['errors'])
    weeks = body['data']['user']['contributionsCollection']['contributionCalendar']['weeks']
    return [day for week in weeks for day in week['contributionDays']]


# choose a mood from daily counts, newest last
def pick_mood(counts):
    quiet_days = 0
    for count in reversed(counts):
        if count:
            break
        quiet_days += 1
    if quiet_days >= SLEEP_QUIET_DAYS:
        return 'sleeping'
    this_week = sum(counts[-DAYS_PER_WEEK:])
    earlier = counts[:-DAYS_PER_WEEK]
    weeks = [sum(earlier[end - DAYS_PER_WEEK:end]) for end in range(len(earlier), DAYS_PER_WEEK - 1, -DAYS_PER_WEEK)]
    matching = sum(week >= this_week for week in weeks)
    if len(weeks) >= MIN_COMPARED_WEEKS and matching * BUSY_SHARE_DENOMINATOR <= len(weeks):
        return 'alert'
    return 'normal'


if __name__ == '__main__':
    today = datetime.now(timezone.utc).date().isoformat()
    days = fetch_days(os.environ['GH_LOGIN'], os.environ['GH_TOKEN'])
    print(pick_mood([day['contributionCount'] for day in days if day['date'] < today]))
