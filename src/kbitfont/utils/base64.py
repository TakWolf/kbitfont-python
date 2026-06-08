import base64


def encode_no_padding(data: bytes) -> bytes:
    return base64.b64encode(data).rstrip(b'=')


def decode_no_padding(data: bytes) -> bytes:
    return base64.b64decode(data + b'=' * (-len(data) % 4))
