import importlib.util
import os
import sys

sys.dont_write_bytecode = True

PAGE = """<!doctype html><meta charset="utf-8"><title>card moods</title>
<style>
body{{margin:0;padding:24px;background:#0d1117;color:#f0f6fc;font:16px system-ui,sans-serif}}
section{{padding:8px 16px}}
.light{{background:#fff;color:#1f2328}}
h2{{margin:24px 0 8px;font-size:16px}}
img{{display:block;max-width:100%}}
</style>
{sections}
"""


def main():
    if len(sys.argv) < 3:
        sys.exit('usage: preview.py build_svg.py output_dir [mood ...]')
    script, output, chosen = sys.argv[1], sys.argv[2], sys.argv[3:]
    spec = importlib.util.spec_from_file_location('build_svg', script)
    card = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(card)
    moods = chosen or list(card.MOODS)
    sections = []
    for name in card.PALETTES:
        theme = 'light' if 'light' in name else 'dark'
        cards = ''.join(f'<h2>{mood} ({theme})</h2><img src="{mood}/{name}">' for mood in moods)
        sections.append(f'<section class="{theme}">{cards}</section>')
    for mood in moods:
        os.makedirs(f'{output}/{mood}', exist_ok=True)
        art = card.build_art(mood)
        for name, palette in card.PALETTES.items():
            with open(f'{output}/{mood}/{name}', 'w', encoding='utf-8') as f:
                f.write(card.build(palette, art))
    with open(f'{output}/index.html', 'w', encoding='utf-8') as f:
        f.write(PAGE.format(sections=''.join(sections)))
    print(os.path.abspath(f'{output}/index.html'))


if __name__ == '__main__':
    main()
