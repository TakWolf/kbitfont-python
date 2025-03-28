# KbitFont.Python

[![Python](https://img.shields.io/badge/python-3.10-brightgreen)](https://www.python.org)
[![PyPI](https://img.shields.io/pypi/v/kbitfont)](https://pypi.org/project/kbitfont/)

KbitFont is a library for parsing [Bits'N'Picas](https://github.com/kreativekorp/bitsnpicas) native save format files (`.kbits` and `.kbitx`).

## Installation

```shell
pip install kbitfont
```

## Usage

### Create

```python
import shutil

from examples import build_dir
from kbitfont import KbitFont, KbitGlyph


def main():
    outputs_dir = build_dir.joinpath('create')
    if outputs_dir.exists():
        shutil.rmtree(outputs_dir)
    outputs_dir.mkdir(parents=True)

    font = KbitFont()
    font.props.em_ascent = 14
    font.props.em_descent = 2
    font.props.line_ascent = 14
    font.props.line_descent = 2
    font.props.x_height = 7
    font.props.cap_height = 10

    font.names.version = '1.0.0'
    font.names.family = 'My Font'
    font.names.style = 'Regular'
    font.names.manufacturer = 'Pixel Font Studio'
    font.names.designer = 'TakWolf'
    font.names.description = 'A pixel font'
    font.names.copyright = 'Copyright (c) TakWolf'
    font.names.license_description = 'This Font Software is licensed under the SIL Open Font License, Version 1.1'
    font.names.vendor_url = 'https://github.com/TakWolf/kbitfont-python'
    font.names.designer_url = 'https://takwolf.com'
    font.names.license_url = 'https://openfontlicense.org'

    font.characters[65] = KbitGlyph(
        x=0,
        y=14,
        advance=8,
        bitmap=[
            [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            [0x00, 0x00, 0x00, 0xFF, 0xFF, 0x00, 0x00, 0x00],
            [0x00, 0x00, 0xFF, 0x00, 0x00, 0xFF, 0x00, 0x00],
            [0x00, 0x00, 0xFF, 0x00, 0x00, 0xFF, 0x00, 0x00],
            [0x00, 0xFF, 0x00, 0x00, 0x00, 0x00, 0xFF, 0x00],
            [0x00, 0xFF, 0x00, 0x00, 0x00, 0x00, 0xFF, 0x00],
            [0x00, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x00],
            [0x00, 0xFF, 0x00, 0x00, 0x00, 0x00, 0xFF, 0x00],
            [0x00, 0xFF, 0x00, 0x00, 0x00, 0x00, 0xFF, 0x00],
            [0x00, 0xFF, 0x00, 0x00, 0x00, 0x00, 0xFF, 0x00],
            [0x00, 0xFF, 0x00, 0x00, 0x00, 0x00, 0xFF, 0x00],
            [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
        ],
    )

    font.named_glyphs['.notdef'] = KbitGlyph(
        x=0,
        y=14,
        advance=8,
        bitmap=[
            [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF],
            [0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF],
            [0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF],
            [0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF],
            [0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF],
            [0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF],
            [0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF],
            [0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF],
            [0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF],
            [0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF],
            [0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF],
            [0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF],
            [0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF],
            [0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF],
            [0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF],
            [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF],
        ],
    )

    font.save_kbits(outputs_dir.joinpath('my-font.kbits'))
    font.save_kbitx(outputs_dir.joinpath('my-font.kbitx'))


if __name__ == '__main__':
    main()
```

### Load Kbits

```python
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
```

### Load Kbitx

```python
import shutil

from examples import assets_dir, build_dir
from kbitfont import KbitFont


def main():
    outputs_dir = build_dir.joinpath('load_kbitx')
    if outputs_dir.exists():
        shutil.rmtree(outputs_dir)
    outputs_dir.mkdir(parents=True)

    font = KbitFont.load_kbitx(assets_dir.joinpath('macintosh', 'Athens.kbitx'))
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
    font.save_kbitx(outputs_dir.joinpath('Athens.kbitx'))


if __name__ == '__main__':
    main()
```

## Specifications

### Font Struct

- [Font.java](https://github.com/TakWolf/kbitfont-spec/blob/master/bitsnpicas/src/main/java/com/kreative/bitsnpicas/Font.java)
- [BitmapFont.java](https://github.com/TakWolf/kbitfont-spec/blob/master/bitsnpicas/src/main/java/com/kreative/bitsnpicas/BitmapFont.java)

### Kbits

- [KbitsBitmapFontImporter.java](https://github.com/TakWolf/kbitfont-spec/blob/master/bitsnpicas/src/main/java/com/kreative/bitsnpicas/importer/KbitsBitmapFontImporter.java)
- [KbitsBitmapFontExporter.java](https://github.com/TakWolf/kbitfont-spec/blob/master/bitsnpicas/src/main/java/com/kreative/bitsnpicas/exporter/KbitsBitmapFontExporter.java)

### Kbitx

- [KbitxBitmapFontImporter.java](https://github.com/TakWolf/kbitfont-spec/blob/master/bitsnpicas/src/main/java/com/kreative/bitsnpicas/importer/KbitxBitmapFontImporter.java)
- [KbitxBitmapFontExporter.java](https://github.com/TakWolf/kbitfont-spec/blob/master/bitsnpicas/src/main/java/com/kreative/bitsnpicas/exporter/KbitxBitmapFontExporter.java)

## Dependencies

- [lxml](https://github.com/lxml/lxml)

## License

[MIT License](LICENSE)
