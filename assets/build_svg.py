from html import escape
from math import pi, sin

ART = """\
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣠⣤⣤⡀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⢰⣿⢋⠈⣿⡀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠙⠛⠀⣿⡄⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠛⠃⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢾⣿⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠟⢿⣿⡿⢿⣿⣿⣿⣿⣿⡟⠛⠛⠛⠛⢻⣿⠉⢹⣿⣿⣿⡃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⢸⣿⡇⢸⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢸⣿⠀⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠈⠟⣡⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠸⠏⣠⣾⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣶⣤⣤⣤⣴⣾⣿⣿⣿⣿⣶⣶⣿⣿⣿⣶⣤⣤⣤⣾⣿⣿⣿⣿⣿⣇⣀⣀⣀⣀⣀⣀⠀
⠀⠀⠀⠀⠸⠟⠛⠛⠛⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠉⠁⠀⠀⠀⠀⠁⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⡶⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠓⠲⠶⠶⠶⠤⣤⣀⠀
⠀⠀⠀⠀⠀⠛⠋⠉⠁⠀⠀⣠⣼⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣯⣄⣀⠀⠀⠀⠀⠀⠀⠈⠁
⠀⠀⠀⠀⠀⠀⠀⣀⣤⡶⠛⠉⠀⠀⠀⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠉⠀⠀⠀⠉⠙⠳⠶⣤⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""

CHAR_W    = 9.59
ART_FS    = 11
ART_LH    = 14
ART_X     = 15
ART_Y0    = 34
PANEL_FS  = 16
PANEL_LH  = 20
PANEL_W   = 54
WIDTH     = 985
HEIGHT    = 530
PANEL_X   = int(WIDTH - 15 - PANEL_W * CHAR_W)
ART_ROWS  = len(ART.split('\n'))
ART_COLS  = max(len(l) for l in ART.split('\n'))

PALETTES = {
    'dark_mode.svg': {
        'bg': '#161b22', 'fg': '#c9d1d9', 'key': '#ffa657', 'value': '#a5d6ff',
        'cc': '#616e7f',
    },
    'light_mode.svg': {
        'bg': '#f6f8fa', 'fg': '#24292f', 'key': '#953800', 'value': '#0a3069',
        'cc': '#c2cfde',
    },
}

BLANK_CELL = '\u2800'
DOT_BITS = {(0, 0): 1, (0, 1): 2, (0, 2): 4, (1, 0): 8, (1, 1): 16, (1, 2): 32, (0, 3): 64, (1, 3): 128}


def to_dots(lines):
    return {(col * 2 + dx, row * 4 + dy)
            for row, line in enumerate(lines)
            for col, char in enumerate(line)
            for (dx, dy), bit in DOT_BITS.items()
            if (ord(char) - 0x2800) & bit}


def to_cells(dots):
    cells = {}
    for x, y in dots:
        cell = (x // 2, y // 4)
        cells[cell] = cells.get(cell, 0) | DOT_BITS[x % 2, y % 4]
    return cells


def opened(dots, size=5):
    span = [(i, j) for i in range(size) for j in range(size)]
    core = {(x, y) for x, y in dots if all((x + i, y + j) in dots for i, j in span)}
    return {(x + i, y + j) for x, y in core for i, j in span}


DOTS = to_dots(ART.split('\n'))
SOLID = opened(DOTS)
SOLID_EDGES = {y: (min(x for x, sy in SOLID if sy == y), max(x for x, sy in SOLID if sy == y))
               for y in {sy for _, sy in SOLID}}
EYE_BOXES = ((29, 49), (60, 78))
EYE_HOLES = {(x, y) for left, right in EYE_BOXES for x in range(left, right) for y in range(57, 70)
             if (x, y) not in DOTS}
EYELIDS = {'open': lambda y: True, 'half': lambda y: y >= 62, 'shut': lambda y: y in (66, 67)}
QUESTION = {(x, y) for x, y in DOTS if x < 16 and 36 <= y < 56}
BANG = {(x, y) for x in range(6, 10) for y in (*range(34, 50), *range(52, 56))}


def set_eyes(dots, eyes):
    if eyes == 'wide':
        return dots - {(x, y - lift) for x, y in EYE_HOLES for lift in range(1, 4)}
    return dots | {dot for dot in EYE_HOLES if not EYELIDS[eyes](dot[1])}


def flick_ear(dots, left, right, push):
    return {(x + round(push * ((36 - y) / 36) ** 2), y) if y < 36 and left <= x < right else (x, y)
            for x, y in dots}


def twitch(dots, is_left, lift):
    moved = set()
    for x, y in dots:
        if lift and (x, y) not in SOLID and 70 <= y <= 90 and (x < 50) == is_left:
            reach = abs(x - SOLID_EDGES[y][0 if is_left else 1]) / 16
            y += round(lift * min(reach, 1))
        moved.add((x, y))
    return moved


def breathe(dots, peak):
    rows = {}
    for x, y in dots:
        if y >= 96:
            rows.setdefault(y, []).append(x)
    widened = set(dots)
    for y, xs in rows.items():
        for step in range(1, round(peak * sin(pi * (y - 96) / 36)) + 1):
            widened |= {(min(xs) - step, y), (max(xs) + step, y)}
    return widened


def zed(x, y, size):
    line = {(x + i, y) for i in range(size)} | {(x + i, y + size - 1) for i in range(size)}
    line |= {(x + size - 1 - i, y + i) for i in range(size)}
    return line | {(dx + 1, dy) for dx, dy in line if dx + 1 < x + size}


def snore(*zeds):
    return frozenset().union(*(zed(*spec) for spec in zeds))


def pose(eyes='open', ear_left=0, ear_right=0, whisker_left=0, whisker_right=0,
         mark=QUESTION, mark_lift=0, breath=0):
    dots = flick_ear(flick_ear(DOTS, 20, 55, ear_left), 55, 90, ear_right)
    dots = twitch(twitch(dots, True, whisker_left), False, whisker_right)
    dots = (dots - QUESTION) | {(x, y + mark_lift) for x, y in mark}
    return breathe(set_eyes(dots, eyes), breath)


REST = 0
BLINK = [{}, {'eyes': 'half'}, {'eyes': 'shut'}]
SNORES = [snore((13, 54, 5), (9, 42, 7), (3, 26, 9)), snore((9, 40, 7), (3, 24, 9)), snore((3, 22, 9)),
          snore(), snore((13, 58, 5)), snore((13, 56, 5), (9, 44, 7))]
# each mood is a rest pose plus parts that loop on their own length
MOODS = {
    'still': ({}, []),
    'normal': ({}, [
        (BLINK,
         [(REST, 2.6), (1, .06), (2, .12), (1, .06), (REST, 2.4), (1, .06), (2, .1), (1, .06),
          (2, .1), (1, .06), (REST, 1.92)]),
        ([{}, {'ear_left': -3}, {'ear_left': -5}],
         [(REST, 8), (1, .08), (2, .14), (1, .08), (REST, .12), (1, .08), (2, .14), (1, .08), (REST, 4.28)]),
        ([{}, {'ear_right': 3}, {'ear_right': 5}],
         [(REST, 3.4), (1, .08), (2, .14), (1, .08), (REST, 13.3)]),
        ([{}, {'whisker_left': -1}, {'whisker_left': -2}, {'whisker_left': 1}],
         [(REST, 5), (1, .07), (2, .12), (1, .07), (REST, .1), (3, .1), (REST, 5.54)]),
        ([{}, {'whisker_right': -1}, {'whisker_right': -2}, {'whisker_right': 1}],
         [(REST, 5.22), (1, .07), (2, .12), (1, .07), (REST, .1), (3, .1), (REST, 5.32)]),
        ([{}, {'mark_lift': -1}, {'mark_lift': -2}],
         [(REST, .9), (1, .5), (2, 1.2), (1, .5), (REST, 1.9)]),
        ([{}, {'breath': 1}, {'breath': 2}],
         [(REST, 1), (1, .5), (2, 1.2), (1, .5), (REST, .7)]),
    ]),
    'sleeping': ({'eyes': 'shut', 'ear_left': -7, 'ear_right': 7, 'mark': SNORES[0]}, [
        ([{}, {'eyes': 'half'}],
         [(REST, 19), (1, .9), (REST, 3.1)]),
        ([{}, {'ear_right': 4}],
         [(REST, 11), (1, .12), (REST, .1), (1, .12), (REST, 14.66)]),
        ([{'mark': mark} for mark in SNORES],
         [(0, 1), (1, .9), (2, .9), (3, 1.2), (4, .9), (5, .9)]),
        ([{}, {'breath': 1}, {'breath': 2}, {'breath': 3}],
         [(REST, .9), (1, .7), (2, .7), (3, 1.6), (2, .7), (1, .7)]),
    ]),
    'alert': ({'eyes': 'wide', 'ear_left': 2, 'ear_right': -2, 'whisker_left': -1, 'whisker_right': -1,
               'mark': BANG}, [
        (BLINK,
         [(REST, 1.5), (1, .05), (2, .08), (1, .05), (REST, 1.42)]),
        ([{}, {'ear_left': 0}, {'ear_left': -2}],
         [(REST, 2), (1, .06), (2, .1), (1, .06), (REST, 2.08)]),
        ([{}, {'ear_right': 0}, {'ear_right': 2}],
         [(REST, 3.1), (1, .06), (2, .1), (1, .06), (REST, 2.58)]),
        ([{}, {'whisker_left': -2}, {'whisker_left': -3}, {'whisker_left': 0}],
         [(REST, 1.4), (1, .06), (2, .1), (1, .06), (REST, .08), (3, .08), (REST, 1.92)]),
        ([{}, {'whisker_right': -2}, {'whisker_right': -3}, {'whisker_right': 0}],
         [(REST, 1.55), (1, .06), (2, .1), (1, .06), (REST, .08), (3, .08), (REST, 1.77)]),
        ([{}, {'mark_lift': -1}, {'mark_lift': -2}],
         [(REST, .5), (1, .1), (2, .2), (1, .1), (REST, .7)]),
        ([{}, {'breath': 1}],
         [(REST, 1.1), (1, 1.1)]),
    ]),
}


def moving_cells(variants):
    grids = [to_cells(dots) for dots in variants]
    return {cell for grid in grids for cell in grid
            if any(grid.get(cell) != other.get(cell) for other in grids)}


def art_rows(grid, keep):
    rows = {}
    for col, row in keep:
        rows.setdefault(row, {})[col] = grid.get((col, row), 0)
    return {row: ''.join(chr(0x2800 + cells.get(col, 0)) for col in range(max(cells) + 1)).rstrip(BLANK_CELL)
            for row, cells in rows.items()}


def rows_markup(rows):
    return ''.join(f'<tspan x="{ART_X}" y="{ART_Y0 + row * ART_LH}">{line}</tspan>'
                   for row, line in sorted(rows.items()) if line)


def keyframes(name, variant, timeline):
    total = sum(seconds for _, seconds in timeline)
    stops, elapsed = [], 0
    for shown, seconds in timeline:
        stops.append(f'{elapsed / total * 100:.2f}%{{visibility:{"visible" if shown == variant else "hidden"}}}')
        elapsed += seconds
    stops.append(f'100%{{visibility:{"visible" if timeline[-1][0] == variant else "hidden"}}}')
    return f'@keyframes {name}{{{"".join(stops)}}}', f'.{name}{{animation:{name} {total:.2f}s step-end infinite}}'


# split a mood into a still layer and animated overlays
def build_art(mood):
    rest, parts = MOODS[mood]
    posed = [([pose(**{**rest, **change}) for change in changes], timeline) for changes, timeline in parts]
    moving = [moving_cells(variants) for variants, _ in posed]
    all_moving = set().union(*moving)
    assert sum(map(len, moving)) == len(all_moving), 'moving parts overlap'
    grid = to_cells(pose(**rest))
    still = art_rows(grid, set(grid) - all_moving)
    frames, css = [], []
    for part, ((variants, timeline), cells) in enumerate(zip(posed, moving)):
        for variant, dots in enumerate(variants):
            name = f'p{part}v{variant}'
            hidden = ' idle' if variant != REST else ''
            frames.append(f'<text class="{name}{hidden}">{rows_markup(art_rows(to_cells(dots), cells))}</text>')
            css.extend(keyframes(name, variant, timeline))
    return rows_markup(still), frames, css


def dots(n):
    return ' ' + '.' * max(0, n - 2) + ' ' if n > 2 else {0: '', 1: ' ', 2: '. '}[max(0, n)]


def kv(key, value):
    keys = key.split('.')
    klen = sum(len(k) for k in keys) + (len(keys) - 1)
    kmarkup = '.'.join(f'<tspan class="key">{escape(k)}</tspan>' for k in keys)
    d = dots(PANEL_W - 2 - klen - 1 - len(value))
    return (f'<tspan class="cc">. </tspan>{kmarkup}:'
            f'<tspan class="cc">{d}</tspan><tspan class="value">{escape(value)}</tspan>')


def rule(label):
    text = f'- {label} '
    return f'<tspan class="hdr">{escape(text)}</tspan>' + '\u2014' * max(0, PANEL_W - len(text) - 3) + '-\u2014-'


def title(name):
    return f'<tspan class="key">{escape(name)}</tspan> ' + '\u2014' * max(0, PANEL_W - len(name) - 4) + '-\u2014-'


BLANK = '<tspan class="cc">. </tspan>'

PANEL = [
    title('name@host'),
    kv('OS', 'Linux'),
    kv('Languages', 'Python, Rust'),
    BLANK,
    kv('Hobbies.Code', 'Exploring Open Source'),
    BLANK,
    rule('Contact'),
    kv('GitHub', 'username'),
]

PANEL_Y0 = ART_Y0 + (HEIGHT - ART_Y0 - len(PANEL) * PANEL_LH) // 2


def build(palette, art):
    still, frames, css = art
    out = ["<?xml version='1.0' encoding='UTF-8'?>"]
    out.append(f'<svg xmlns="http://www.w3.org/2000/svg" '
               f'font-family="ConsolasFallback,Consolas,DejaVu Sans Mono,monospace" '
               f'width="{WIDTH}px" height="{HEIGHT}px" font-size="{PANEL_FS}px">')
    out.append('<style>')
    out.append("@font-face {")
    out.append("src: local('Consolas'), local('Consolas Bold');")
    out.append("font-family: 'ConsolasFallback';")
    out.append('font-display: swap;')
    out.append('-webkit-size-adjust: 109%;')
    out.append('size-adjust: 109%;')
    out.append('}')
    out.append('.key {fill: %s;}' % palette['key'])
    out.append('.value {fill: %s;}' % palette['value'])
    out.append('.cc {fill: %s;}' % palette['cc'])
    out.append('.hdr {fill: %s;}' % palette['key'])
    out.append('text, tspan {white-space: pre;}')
    out.append('.art {font-size: %spx; fill: %s;}' % (ART_FS, palette['fg']))
    out.append('.idle {visibility: hidden;}')
    out.append('@media (prefers-reduced-motion: no-preference) {')
    out.extend(css)
    out.append('}')
    out.append('</style>')
    out.append(f'<rect width="{WIDTH}px" height="{HEIGHT}px" fill="{palette["bg"]}" rx="15"/>')

    out.append('<g class="art">')
    out.append(f'<text>{still}</text>')
    out.extend(frames)
    out.append('</g>')

    out.append(f'<text x="{PANEL_X}" y="{PANEL_Y0}" fill="{palette["fg"]}">')
    for i, line in enumerate(PANEL):
        out.append(f'<tspan x="{PANEL_X}" y="{PANEL_Y0 + i * PANEL_LH}">{line}</tspan>')
    out.append('</text>')
    out.append('</svg>')
    return '\n'.join(out)


if __name__ == '__main__':
    import sys
    dest = sys.argv[1] if len(sys.argv) > 1 else '.'
    mood = sys.argv[2] if len(sys.argv) > 2 else 'normal' if 'normal' in MOODS else 'still'
    art = build_art(mood)
    art_px = ART_X + ART_COLS * ART_FS * 0.688
    print(f'svg {WIDTH}x{HEIGHT} | art ends ~{art_px:.0f}px | panel x={PANEL_X} | '
          f'art rows {ART_ROWS} -> {ART_Y0 + (ART_ROWS - 1) * ART_LH}px')
    for name, palette in PALETTES.items():
        with open(f'{dest}/{name}', 'w', encoding='utf-8') as f:
            f.write(build(palette, art))
        print('wrote', name, mood)
