from pathlib import Path

from kbitfont import KbitFont


def test_demo_kbits(assets_dir: Path):
    data = assets_dir.joinpath('demo', 'demo.kbits').read_bytes()
    font = KbitFont.parse_kbits(data)
    assert font.dump_kbits_to_bytes() == data


def test_demo_kbitx(assets_dir: Path):
    data = assets_dir.joinpath('demo', 'demo.kbitx').read_bytes()
    font = KbitFont.parse_kbitx(data)
    assert font.dump_kbitx_to_bytes() == data.replace(b'\r\n', b'\n')
