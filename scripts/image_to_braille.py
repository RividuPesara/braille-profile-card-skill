import argparse
import re

from PIL import Image, ImageDraw, ImageFont, ImageOps

BITS = {(0, 0): 1, (0, 1): 2, (0, 2): 4, (1, 0): 8, (1, 1): 16, (1, 2): 32, (0, 3): 64, (1, 3): 128}
DOT_ASPECT = 1.1


def load_gray(path):
    image = Image.open(path).convert('RGBA')
    canvas = Image.new('RGBA', image.size, 'white')
    canvas.alpha_composite(image)
    return canvas.convert('L')


def read_text(path):
    with open(path, encoding='utf-8') as f:
        lines = f.read().rstrip().split('\n')
    return lines if any(line.strip() for line in lines) else None


def is_braille(lines):
    return all(0x2800 <= ord(char) <= 0x28ff for line in lines for char in line if char != ' ')


def tidy_braille(lines, cols, rows):
    width = max(map(len, lines))
    if width > cols or len(lines) > rows:
        raise SystemExit(f'braille art is {width} by {len(lines)} cells, the card holds {cols} by {rows}')
    return [line.replace(' ', '\u2800').ljust(cols, '\u2800') for line in lines]


def load_font(size):
    for name in ('DejaVuSansMono-Bold.ttf', 'DejaVuSansMono.ttf', 'Consolas.ttf', 'Menlo.ttc'):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            pass
    return ImageFont.load_default(size)


def text_to_gray(lines):
    size, cell_width, cell_height = 64, 39, 76
    canvas = Image.new('L', (max(map(len, lines)) * cell_width + 8, len(lines) * cell_height + 8), 255)
    draw = ImageDraw.Draw(canvas)
    font = load_font(size)
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if not char.isspace():
                draw.text((col * cell_width + 4, row * cell_height + 4), char, fill=0, font=font)
    return canvas


def otsu(gray):
    histogram = gray.histogram()
    total = sum(histogram)
    weighted = sum(level * count for level, count in enumerate(histogram))
    best, best_score, below, below_sum = 128, -1, 0, 0
    for level, count in enumerate(histogram):
        below += count
        below_sum += level * count
        above = total - below
        if below and above:
            gap = below_sum / below - (weighted - below_sum) / above
            score = below * above * gap * gap
            if score > best_score:
                best, best_score = level, score
    return best


def border_mean(gray):
    width, height = gray.size
    edge = [gray.getpixel((x, y)) for x in range(width) for y in (0, height - 1)]
    edge += [gray.getpixel((x, y)) for y in range(height) for x in (0, width - 1)]
    return sum(edge) / len(edge)


# convert a gray image into braille rows centered on the card
def to_lines(gray, cols, rows, threshold, dither, invert):
    border = border_mean(gray)
    gray = gray.crop(gray.point(lambda value: 255 if abs(value - border) > 32 else 0).getbbox() or (0, 0, *gray.size))
    scale = min(cols * 2 / (gray.width / DOT_ASPECT), rows * 4 / gray.height)
    size = (max(1, round(gray.width / DOT_ASPECT * scale)), max(1, round(gray.height * scale)))
    small = gray.resize(size, Image.LANCZOS)
    level = otsu(small) if threshold is None else threshold
    subject_is_dark = border_mean(small) > level
    if invert:
        subject_is_dark = not subject_is_dark
    if subject_is_dark:
        small = ImageOps.invert(small)
        level = 255 - level
    if dither:
        lit = small.convert('1')
    else:
        lit = small.point(lambda value: 255 if value > level else 0).convert('1')
    pixels = lit.load()
    width, height = lit.size
    used_cols, used_rows = (width + 1) // 2, (height + 3) // 4
    pad_cols, pad_rows = (cols - used_cols) // 2, (rows - used_rows) // 2
    lines = ['⠀' * cols for _ in range(pad_rows)]
    for row in range(used_rows):
        line = '⠀' * pad_cols
        for col in range(used_cols):
            value = 0
            for (dx, dy), bit in BITS.items():
                x, y = col * 2 + dx, row * 4 + dy
                if x < width and y < height and pixels[x, y]:
                    value |= bit
            line += chr(0x2800 + value)
        lines.append(line.ljust(cols, '⠀'))
    return lines


def main():
    parser = argparse.ArgumentParser(description='Convert an image, plain text art or braille text to card art')
    parser.add_argument('image')
    parser.add_argument('--cols', type=int, default=50)
    parser.add_argument('--rows', type=int, default=33)
    parser.add_argument('--threshold', type=int, help='0 to 255, chosen automatically if left out')
    parser.add_argument('--dither', action='store_true', help='for photos and soft shading')
    parser.add_argument('--invert', action='store_true', help='swap subject and background')
    parser.add_argument('--into', help='replace the ART block in this build_svg.py')
    args = parser.parse_args()
    if args.image.lower().endswith(('.txt', '.asc')):
        text = read_text(args.image)
        if text is None:
            raise SystemExit('the text file is empty')
    else:
        text = None
    if text and is_braille(text):
        lines = tidy_braille(text, args.cols, args.rows)
    else:
        gray = text_to_gray(text) if text else load_gray(args.image)
        lines = to_lines(gray, args.cols, args.rows, args.threshold, args.dither, args.invert)
    art = '\n'.join(lines)
    if args.into:
        with open(args.into, encoding='utf-8') as f:
            source = f.read()
        source, count = re.subn(r'ART = """\\\n.*?"""', lambda _: f'ART = """\\\n{art}"""', source, flags=re.S)
        if count != 1:
            raise SystemExit('no ART block found')
        with open(args.into, 'w', encoding='utf-8') as f:
            f.write(source)
    print(art)


if __name__ == '__main__':
    main()
