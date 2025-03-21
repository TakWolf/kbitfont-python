import shutil

from examples import assets_dir, build_dir
from kbitfont import KbitFont


def main():
    outputs_dir = build_dir.joinpath('load_kbits')
    if outputs_dir.exists():
        shutil.rmtree(outputs_dir)
    outputs_dir.mkdir(parents=True)

    font = KbitFont.load_kbits(assets_dir.joinpath('macintosh', 'Athens.kbits'))
    print(f'name: {font.names.family}')
    print(f'size: {font.props.em_height}')
    print(f'ascent: {font.props.line_ascent}')
    print(f'descent: {font.props.line_descent}')
    print()
    for code_point, glyph in sorted(font.characters.items()):
        print(f'char: {chr(code_point)} ({code_point:04X})')
        print(f'xy: {(glyph.x, glyph.y)}')
        print(f'dimensions: {glyph.dimensions}')
        print(f'advance: {glyph.advance}')
        for bitmap_row in glyph.bitmap:
            text = ''.join('  ' if color <= 127 else '██' for color in bitmap_row)
            print(f'{text}*')
        print()
    font.save_kbits(outputs_dir.joinpath('Athens.kbits'))


if __name__ == '__main__':
    main()
