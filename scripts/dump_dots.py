import re
import sys

BITS = {(0, 0): 1, (0, 1): 2, (0, 2): 4, (1, 0): 8, (1, 1): 16, (1, 2): 32, (0, 3): 64, (1, 3): 128}


def main():
    if len(sys.argv) < 2:
        sys.exit('usage: dump_dots.py build_svg.py [first_y last_y]')
    source = open(sys.argv[1], encoding='utf-8').read()
    lines = re.search(r'ART = """\\\n(.*?)"""', source, re.S).group(1).split('\n')
    dots = {(col * 2 + dx, row * 4 + dy)
            for row, line in enumerate(lines)
            for col, char in enumerate(line)
            for (dx, dy), bit in BITS.items()
            if (ord(char) - 0x2800) & bit}
    width, height = max(map(len, lines)) * 2, len(lines) * 4
    first = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    last = int(sys.argv[3]) if len(sys.argv) > 3 else height - 1
    print(f'{len(lines)} rows, {width // 2} cols, {width} x {height} dots')
    print('     ' + ''.join(str(x // 10 % 10) if x % 10 == 0 else ' ' for x in range(width)))
    for y in range(first, last + 1):
        marker = '|' if y % 4 == 0 else ' '
        print(f'{y:3d} {marker}' + ''.join('#' if (x, y) in dots else '.' for x in range(width)))


if __name__ == '__main__':
    main()
