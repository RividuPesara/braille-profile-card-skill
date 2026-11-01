# Braille profile card skill

An agent skill that builds a neofetch-style GitHub profile card. Give it a picture or some text art and your details, and it makes a card with braille art next to an info panel, in dark and light themes.

The art can also blink, breathe and react to your GitHub activity. It's all one SVG, with no GIFs and no JavaScript.

<a href="https://github.com/RividuPesara">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/RividuPesara/RividuPesara/output/dark_mode.svg">
    <img alt="An animated braille cat next to a profile info panel" src="https://raw.githubusercontent.com/RividuPesara/RividuPesara/output/light_mode.svg">
  </picture>
</a>

## Install

**Claude Code:** clone this repo into your skills folder.

```bash
git clone https://github.com/RividuPesara/braille-profile-card-skill ~/.claude/skills/braille-profile-card-skill
```

**Other coding agents:** clone it anywhere and point your agent at `AGENTS.md`.

## Use

In Claude Code, run `/braille-profile-card-skill`, or just ask:

> Make me a GitHub profile card from `~/Pictures/fox.png`

With another agent:

> Follow `path/to/braille-profile-card-skill/AGENTS.md` and make me a GitHub profile card

The agent asks for anything it needs, shows you a preview, and leaves committing and pushing to you.

### What you can give it

- An image file or link
- ASCII art or braille art, pasted as text

High-contrast images with plain backgrounds convert best. It can't draw from a description like "a sleepy fox", so you'll need an image for that.

### How far to go

You can stop at any level:

| Level | What you get |
|---|---|
| **Static card** | Art, info panel, both themes and a README |
| **Animation** | Moves that suit your art, like blinks, breathing and ear flicks |
| **Moods** | A nightly GitHub Action that changes the art based on your activity |

Moods work like this:

| Mood | When | Example |
|---|---|---|
| Sleeping | 14 or more quiet days | Eyes closed, `z z z` floating up |
| Normal | Most days | Everyday blinks and breathing |
| Alert | One of your busiest weeks of the year | Wide eyes, a bouncing `!` |

Moods only count public activity by default. If most of your work is private, add a personal token as a repo secret named `MOOD_TOKEN`.

## Requirements

- Python 3 with [Pillow](https://python-pillow.org)
