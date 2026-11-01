# Braille profile card

Instructions for any coding agent. `KIT` below means the folder holding this file, so write out its real path in commands. Run every command from the user's profile repo, where `build_svg.py` is the repo's own copy.

Use this when someone wants a GitHub profile README, a neofetch-style or terminal-style profile, braille or ASCII art on their profile, or profile art that moves or reacts to their activity. It is not for repository READMEs, or for GIF, video or general website animation.

Needs Python 3 with Pillow for art conversion. `gh` is used to look up the user and test moods, and a browser is used to check the result.

Build the whole profile in stages: art, card, README, animation, moods. Each stage leaves something that works, so the user can stop at any point. A plain static card is a perfectly good result.

## Why it is built this way

These choices came from a working build, and each prevents a real failure.

- **SVG, not GIF.** GitHub shows the card as an image, so JavaScript and hover never run, but CSS animation does. A GIF would need one file per theme and would blur the text.
- **Overlay rows start with blank braille cells, not an x offset.** Fonts give braille different widths, so a pixel position drifts. `U+2800` advances exactly as far as the dots beside it, in any font.
- **Only moving cells are redrawn.** The engine diffs every pose and removes changing cells from the still layer, which keeps an animated card around 30 to 40 KB.
- **Each part loops on its own length.** Different lengths make moves drift apart, so the card never looks like one mechanical cycle.
- **Animation lives inside `prefers-reduced-motion: no-preference`.** With no animation the resting pose still shows, so it must look good alone.

## Start

Check what exists before asking anything: `gh auth status`, the logged-in username, and whether `OWNER/OWNER` exists with a README or card already. If they have a card, keep it and join at the stage that fits.

Then get what cannot be looked up. Skip anything the user already told you.

1. **The art.** If they have not given any, stop and ask before building anything, and wait for the answer. The art is the identity of the card, so never pick the bundled cat or invent art for them. Ask for one of these:
   - an image file or link
   - art pasted as text, plain ASCII or braille
   - the bundled cat

   A description alone, like "a sleepy fox", is not art this kit can draw. Ask them for an image, or offer the cat.
2. **Stages:** static card only, or animation, or animation and moods.

Pull what you can for the panel from `gh api users/OWNER` and their repos' languages, and show it for confirmation. Ask for the rest, such as hobbies and contact links. Only put in details they gave or approved, because this is public and describes them.

Creating the `OWNER/OWNER` repo on GitHub is public, so confirm before doing it. Until then, work in a local folder named `OWNER`. If it does not exist, create it with `git init -b main`, so that the branch matches the README's image links.

## Stage 1: Art

Copy `KIT/assets/build_svg.py` into the repo. Skip the rest of this stage if they chose the bundled cat.

Get the art into a file. Save pasted art to a `.txt` file outside the repo, and download a link to a new empty folder outside the repo.

```
python3 KIT/scripts/image_to_braille.py ART_FILE --into build_svg.py
```

It needs Pillow, and it reads images, plain text art and braille text. Files ending in `.txt` or `.asc` are read as text. Braille text goes in as it is, and it stops with an error if it is over the card's size. Plain ASCII keeps its look, because each character is drawn as a large glyph, so `o.o` stays a pair of eyes. It reads as line art made of characters, and small art gets scaled up to fill the card.

The default 50 by 33 cells fills the card's left side, so keep to that unless the layout changes. For images and ASCII it finds the subject from the border and picks a threshold itself. Check the printed art, then adjust:

- `--dither` for photos and soft shading, not for ASCII
- `--threshold N` when detail is lost or the shape is blobby
- `--invert` when subject and background came out swapped

Faces and thin lines in images often need several tries, so expect to iterate and to show the user the result.

## Stage 2: Card

In `build_svg.py`, fill in `PANEL`. `title` is the header line, a short `name@host` style handle, so ask if theirs is not obvious. `kv` is a key and value row, and dotted keys like `Databases.SQL` work. `rule` is a section divider such as `Contact`, and `BLANK` is an empty row between groups. The template shows the usual layout, so follow it unless the user wants otherwise. Key and value together should stay under about 50 characters, because longer lines run off the card without any error. Set `PALETTES` if they want other colors.

Until Stage 3 replaces them, the template's other moods are the cat's. On new art they can stop with `moving parts overlap`, or worse, build cleanly and draw cat poses in the wrong places. So use only the `still` mood here, which draws any art with no motion:

```
python3 build_svg.py . still
```

Write `README.md` from `KIT/assets/README.md`, replacing `OWNER`, and using `main` for `BRANCH`. If they already have a README, add the card to it instead of replacing it.

Check it as in "Checking the result" below, passing `still` as the mood. The printed `art ends` figure is a rough estimate, so judge the gap between art and panel from a render.

If they want a static card, remove every `MOODS` entry except `still`, so that no cat poses remain to build by accident. The cat's helpers can stay or go, as long as `pose()`, `REST`, `MOODS` and `build_art()` remain, because the build uses them. The commit needs `build_svg.py`, `README.md` and both SVGs.

## Stage 3: Animation

The template is a complete working example for the cat, so read `pose()`, `MOODS` and `build_art()` first.

Map the art:

```
python3 KIT/scripts/dump_dots.py build_svg.py
python3 KIT/scripts/dump_dots.py build_svg.py 32 96
```

This prints the art as a grid of dots with x and y rulers. Each cell is 2 dots wide and 4 tall.

Identify what each shape actually is before animating it. The cat's left-hand squiggle looked like a tail and was a question mark.

**Replace the cat.** All of this belongs to the cat, and any of it left behind can silently draw on the wrong spot:

- `EYE_BOXES`, the `57..70` range in `EYE_HOLES`, and the rows in `EYELIDS`
- `QUESTION`, `BANG`, `SNORES` and `BLINK`
- the ear ranges and the `36` in `flick_ear`
- the `70 <= y <= 90` and `x < 50` tests in `twitch`
- `y >= 96` and the `96` and `36` in `breathe`
- the `pose()` arguments and every entry in `MOODS`

Rewrite `pose()` around the parts this art really has, and delete helpers it has no use for, such as `opened`, `SOLID`, `zed` and `snore`.

**How a mood is defined.** A pose is the full dot set for one look. A mood is `(rest, parts)`, where `rest` is a dict of `pose()` arguments. A part is `(changes, timeline)`. `changes` is a list of dicts, each merged over `rest`, and the first must be `{}` so that variant 0 is the rest. `timeline` is a list of `(variant, seconds)`, where variant is an index into `changes`. The seconds add up to that part's loop length.

Keep to dot moves that suit the art, so that it keeps its grid look. Good starting points are blinks, a breathing edge, small shears, and shifting a detached mark. Thin parts are easy to separate from a body with `opened()`.

Parts must not share cells, and the build stops with `moving parts overlap` if they do. Two moves in the same region, like a blink and a glance, must become one part with more variants. Moves in different regions should stay separate parts, because that is what lets them drift apart.

Let each part loop every 3 to 20 seconds. Slow moves can hold a pose for a second or more, and quick twitches take about 0.1 seconds per frame. Use quick moves rarely, because that is what makes it feel alive. Give each mood a resting pose that reads clearly as a still image, since that is what reduced motion shows.

The build cannot catch visual bugs, such as a line left behind when an eyelid closes, so look at paused poses of every mood.

If they want animation without moods, keep one mood called `normal`, plus `still` if you like, and remove the rest. Then build it. The commit needs `build_svg.py`, `README.md` and both SVGs:

```
python3 build_svg.py . normal
```

## Stage 4: Moods

Ask before this stage, since it adds a workflow to their repo. Copy `KIT/assets/mood.py` to the repo root and `KIT/assets/mood.yml` to `.github/workflows/mood.yml`. Change `branches: [main]` if their default branch differs.

`pick_mood` must return names that exist in `MOODS`. Its defaults are `sleeping` after 14 quiet days, `alert` when the last 7 days are in the top tenth of past weeks with at least 10 weeks to compare, otherwise `normal`. `MOODS` needs all three unless you change `pick_mood`.

Set `BRANCH` in the README to `output`. The workflow publishes the SVGs there, so with moods on the commit needs `build_svg.py`, `mood.py`, `README.md` and the workflow, and no SVGs. Delete any left in the repo root, or they will go stale.

To test the mood against real data without changing anything:

```
GH_LOGIN=OWNER GH_TOKEN=$(gh auth token) python3 -B mood.py
```

## Checking the result

```
python3 KIT/scripts/preview.py build_svg.py DIR [MOOD ...]
```

This builds the named moods, or all of them, fresh from `build_svg.py`, and writes an `index.html` showing them in both themes. Because it rebuilds, it says nothing about the SVGs in the repo, so rebuild those before finishing. Put `DIR` outside the git repo, and outside `/tmp` too, because snap browsers cannot read `/tmp`.

Where there is a display, open it with `xdg-open` and let the user see it. Without one, use a headless browser.

Look at actual renders rather than trusting the code. Check the panel fits and the art does not run into it. With Playwright or similar, which can go in a throwaway folder outside the repo with `npm i playwright`. It needs a matching browser, so run `npx playwright install chromium`, or pass an installed browser as `executablePath`:

- Open the SVG directly and pause it at a moment `t` in milliseconds with `document.getAnimations().forEach(a => { a.pause(); a.currentTime = t })`, then screenshot it. Do this for each mood, in both themes.
- Load the SVG through an `<img>` tag and compare screenshots over a few seconds. This is the case that matches GitHub. Scripts cannot reach inside an image, so screenshots are the only check here.
- Check body edges for notches, which hard-edged bands cause. Taper the change instead.

## Tell the user

Always:

- **To publish:** the card appears on their profile once everything is pushed to `OWNER/OWNER`. Leave committing and pushing to them unless they ask.

If moods are on:

- **Pushes:** the job runs nightly but only commits when the mood changes, plus an empty commit about every 45 days. Commits go to `output` as `github-actions[bot]`, so `main` stays clean and their contribution graph is unaffected.
- **First push:** the README image looks broken until the first run creates `output`.
- **Private work:** the built-in token sees public activity only. A check with their own `gh` token can read differently from the workflow. If their work is mostly private, they should add a personal token as a repo secret named `MOOD_TOKEN`, or the card will look inactive while they are busy.
- **Long quiet spells:** GitHub can silently turn off a schedule after 60 days without repo activity, and it is unconfirmed what resets that clock. The workflow re-enables itself nightly and makes that 45-day empty commit, but if the card stops changing they should run `gh workflow enable mood.yml`.
- **Reduced motion:** this works when the SVG is opened directly, but inside an `<img>` it was only tested with simulated settings, which did not reach the image.
