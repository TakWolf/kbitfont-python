from pathlib import Path

import pytest

from kbitfont import KbitFont


@pytest.mark.parametrize(
    'font_dir, font_file_name', [
        ('demo', 'demo.kbits'),
        ('macintosh', 'Athens.kbits'),
        ('macintosh', 'Geneva-12.kbits'),
        ('macintosh', 'New-York-14.kbits'),
    ],
)
def test_parse_dump_kbits(assets_dir: Path, font_dir: str, font_file_name: str):
    data = assets_dir.joinpath(font_dir, font_file_name).read_bytes()
    font = KbitFont.parse_kbits(data)
    assert font.dump_kbits_to_bytes() == data


@pytest.mark.parametrize(
    'font_dir, font_file_name', [
        ('demo', 'demo.kbitx'),
        ('macintosh', 'Athens.kbitx'),
        ('macintosh', 'Geneva-12.kbitx'),
        ('macintosh', 'New-York-14.kbitx'),
    ],
)
def test_parse_dump_kbitx(assets_dir: Path, font_dir: str, font_file_name: str):
    data = assets_dir.joinpath(font_dir, font_file_name).read_bytes()
    font = KbitFont.parse_kbitx(data)
    assert font.dump_kbitx_to_bytes() == data.replace(b'\r\n', b'\n')
