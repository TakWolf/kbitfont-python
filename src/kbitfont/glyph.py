from typing import Any


class KbitGlyph:
    x: int
    y: int
    advance: int
    bitmap: list[list[int]]

    def __init__(
            self,
            x: int = 0,
            y: int = 0,
            advance: int = 0,
            bitmap: list[list[int]] | None = None,
    ):
        self.x = x
        self.y = y
        self.advance = advance
        self.bitmap = [] if bitmap is None else bitmap

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KbitGlyph):
            return NotImplemented
        return (self.x == other.x and
                self.y == other.y and
                self.advance == other.advance and
                self.bitmap == other.bitmap)

    @property
    def width(self) -> int:
        if len(self.bitmap) > 0:
            return len(self.bitmap[0])
        else:
            return 0

    @property
    def height(self) -> int:
        return len(self.bitmap)

    @property
    def dimensions(self) -> tuple[int, int]:
        return self.width, self.height
