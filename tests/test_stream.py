import random
from io import BytesIO

import pytest

from kbitfont.internal.stream import Stream


def test_byte():
    stream = Stream(BytesIO())
    size = stream.write(b'Hello World')
    assert stream.tell() == size
    stream.seek(0)
    assert stream.read(11) == b'Hello World'
    assert stream.tell() == size


def test_eof():
    stream = Stream(BytesIO())
    with pytest.raises(EOFError):
        stream.read(1)


def test_int8():
    values = [random.randint(-0x80, 0x7F) for _ in range(20)]

    stream = Stream(BytesIO())
    size = 0
    for value in values:
        size += stream.write_int8(value)
    assert stream.tell() == size
    stream.seek(0)
    for value in values:
        assert stream.read_int8() == value
    assert stream.tell() == size


def test_uint8():
    values = [random.randint(0, 0xFF) for _ in range(20)]

    stream = Stream(BytesIO())
    size = 0
    for value in values:
        size += stream.write_uint8(value)
    assert stream.tell() == size
    stream.seek(0)
    for value in values:
        assert stream.read_uint8() == value
    assert stream.tell() == size


def test_int16():
    values = [random.randint(-0x80_00, 0x7F_FF) for _ in range(20)]

    stream = Stream(BytesIO())
    size = 0
    for value in values:
        size += stream.write_int16(value)
    assert stream.tell() == size
    stream.seek(0)
    for value in values:
        assert stream.read_int16() == value
    assert stream.tell() == size


def test_uint16():
    values = [random.randint(0, 0xFF_FF) for _ in range(20)]

    stream = Stream(BytesIO())
    size = 0
    for value in values:
        size += stream.write_uint16(value)
    assert stream.tell() == size
    stream.seek(0)
    for value in values:
        assert stream.read_uint16() == value
    assert stream.tell() == size


def test_int32():
    values = [random.randint(-0x80_00_00_00, 0x7F_FF_FF_FF) for _ in range(20)]

    stream = Stream(BytesIO())
    size = 0
    for value in values:
        size += stream.write_int32(value)
    assert stream.tell() == size
    stream.seek(0)
    for value in values:
        assert stream.read_int32() == value
    assert stream.tell() == size


def test_uint32():
    values = [random.randint(0, 0xFF_FF_FF_FF) for _ in range(20)]

    stream = Stream(BytesIO())
    size = 0
    for value in values:
        size += stream.write_uint32(value)
    assert stream.tell() == size
    stream.seek(0)
    for value in values:
        assert stream.read_uint32() == value
    assert stream.tell() == size


def test_utf():
    values = ['ABC', 'DEF', '12345', '67890']

    stream = Stream(BytesIO())
    size = 0
    for value in values:
        size += stream.write_utf(value)
    assert stream.tell() == size
    stream.seek(0)
    for value in values:
        assert stream.read_utf() == value
    assert stream.tell() == size


def test_uleb128():
    values = [random.randint(0, 0xFFFF) for _ in range(20)]

    stream = Stream(BytesIO())
    size = 0
    for value in values:
        size += stream.write_uleb128(value)
    assert stream.tell() == size
    stream.seek(0)
    for value in values:
        assert stream.read_uleb128() == value
    assert stream.tell() == size


def test_bitmap_1():
    bitmap = [
        [0x00, 0x00, 0xFF, 0xFF, 0x80],
        [0x00, 0x00, 0xFF, 0xFF, 0x80],
        [0x00, 0x00, 0xFF, 0xFF, 0x80],
    ]

    stream = Stream(BytesIO())
    size = stream.write_bitmap(bitmap)
    assert stream.tell() == size
    stream.seek(0)
    assert stream.read_bitmap() == bitmap
    assert stream.tell() == size


def test_bitmap_2():
    bitmap = [[i % 0xFF for i in range(1050)]]

    stream = Stream(BytesIO())
    size = stream.write_bitmap(bitmap)
    assert stream.tell() == size
    stream.seek(0)
    assert stream.read_bitmap() == bitmap
    assert stream.tell() == size


def test_bitmap_3():
    bitmap = [[0x00 for _ in range(1050)]]

    stream = Stream(BytesIO())
    size = stream.write_bitmap(bitmap)
    assert stream.tell() == size
    stream.seek(0)
    assert stream.read_bitmap() == bitmap
    assert stream.tell() == size


def test_bitmap_4():
    bitmap = [[0x80 for _ in range(1050)]]

    stream = Stream(BytesIO())
    size = stream.write_bitmap(bitmap)
    assert stream.tell() == size
    stream.seek(0)
    assert stream.read_bitmap() == bitmap
    assert stream.tell() == size


def test_bitmap_5():
    bitmap = [[0xFF for _ in range(1050)]]

    stream = Stream(BytesIO())
    size = stream.write_bitmap(bitmap)
    assert stream.tell() == size
    stream.seek(0)
    assert stream.read_bitmap() == bitmap
    assert stream.tell() == size
