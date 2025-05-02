import pytest

from kbitfont.utils.stream import Stream


def test_bytes():
    stream = Stream()
    assert stream.write(b'Hello World') == 11
    assert stream.tell() == 11
    stream.seek(0)
    assert stream.read(11) == b'Hello World'
    assert stream.tell() == 11


def test_eof():
    stream = Stream()
    stream.write(b'ABC')
    with pytest.raises(EOFError):
        stream.read(4)
    stream.seek(0)
    assert stream.read(4, ignore_eof=True) == b'ABC'


def test_uint8():
    stream = Stream()
    assert stream.write_uint8(0x00) == 1
    assert stream.write_uint8(0xFF) == 1
    assert stream.tell() == 2
    stream.seek(0)
    assert stream.read_uint8() == 0x00
    assert stream.read_uint8() == 0xFF
    assert stream.tell() == 2


def test_int8():
    stream = Stream()
    assert stream.write_int8(-0x80) == 1
    assert stream.write_int8(0x7F) == 1
    assert stream.tell() == 2
    stream.seek(0)
    assert stream.read_int8() == -0x80
    assert stream.read_int8() == 0x7F
    assert stream.tell() == 2


def test_uint16():
    stream = Stream()
    assert stream.write_uint16(0x0000) == 2
    assert stream.write_uint16(0xFFFF) == 2
    assert stream.tell() == 4
    stream.seek(0)
    assert stream.read_uint16() == 0x0000
    assert stream.read_uint16() == 0xFFFF
    assert stream.tell() == 4


def test_int16():
    stream = Stream()
    assert stream.write_int16(-0x8000) == 2
    assert stream.write_int16(0x7FFF) == 2
    assert stream.tell() == 4
    stream.seek(0)
    assert stream.read_int16() == -0x8000
    assert stream.read_int16() == 0x7FFF
    assert stream.tell() == 4


def test_uint32():
    stream = Stream()
    assert stream.write_uint32(0x00000000) == 4
    assert stream.write_uint32(0xFFFFFFFF) == 4
    assert stream.tell() == 8
    stream.seek(0)
    assert stream.read_uint32() == 0x00000000
    assert stream.read_uint32() == 0xFFFFFFFF
    assert stream.tell() == 8


def test_int32():
    stream = Stream()
    assert stream.write_int32(-0x80000000) == 4
    assert stream.write_int32(0x7FFFFFFF) == 4
    assert stream.tell() == 8
    stream.seek(0)
    assert stream.read_int32() == -0x80000000
    assert stream.read_int32() == 0x7FFFFFFF
    assert stream.tell() == 8


def test_utf():
    stream = Stream()
    assert stream.write_utf('ABC') == 5
    assert stream.write_utf('12345') == 7
    assert stream.tell() == 12
    stream.seek(0)
    assert stream.read_utf() == 'ABC'
    assert stream.read_utf() == '12345'
    assert stream.tell() == 12


def test_uleb128():
    stream = Stream()
    assert stream.write_uleb128(65535) == 3
    assert stream.write_uleb128(624485) == 3
    assert stream.write(b'\xff\xff\x03') == 3
    assert stream.write(b'\xe5\x8e\x26') == 3
    assert stream.tell() == 12
    stream.seek(0)
    assert stream.read(3) == b'\xff\xff\x03'
    assert stream.read(3) == b'\xe5\x8e\x26'
    assert stream.read_uleb128() == 65535
    assert stream.read_uleb128() == 624485
    assert stream.tell() == 12


def test_bitmap_1():
    bitmap = [
        [0x00, 0x00, 0xFF, 0xFF, 0x80],
        [0x00, 0x00, 0xFF, 0xFF, 0x80],
        [0x00, 0x00, 0xFF, 0xFF, 0x80],
    ]

    stream = Stream()
    size = stream.write_bitmap(bitmap)
    assert stream.tell() == size
    stream.seek(0)
    assert stream.read_bitmap() == bitmap
    assert stream.tell() == size


def test_bitmap_2():
    bitmap = [[i % 0xFF for i in range(1050)]]

    stream = Stream()
    size = stream.write_bitmap(bitmap)
    assert stream.tell() == size
    stream.seek(0)
    assert stream.read_bitmap() == bitmap
    assert stream.tell() == size


def test_bitmap_3():
    bitmap = [[0x00 for _ in range(1050)]]

    stream = Stream()
    size = stream.write_bitmap(bitmap)
    assert stream.tell() == size
    stream.seek(0)
    assert stream.read_bitmap() == bitmap
    assert stream.tell() == size


def test_bitmap_4():
    bitmap = [[0x80 for _ in range(1050)]]

    stream = Stream()
    size = stream.write_bitmap(bitmap)
    assert stream.tell() == size
    stream.seek(0)
    assert stream.read_bitmap() == bitmap
    assert stream.tell() == size


def test_bitmap_5():
    bitmap = [[0xFF for _ in range(1050)]]

    stream = Stream()
    size = stream.write_bitmap(bitmap)
    assert stream.tell() == size
    stream.seek(0)
    assert stream.read_bitmap() == bitmap
    assert stream.tell() == size
