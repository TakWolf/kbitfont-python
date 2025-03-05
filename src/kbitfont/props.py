
class KbitProps:
    em_ascent: int
    em_descent: int
    line_ascent: int
    line_descent: int
    line_gap: int
    x_height: int
    cap_height: int

    def __init__(
            self,
            em_ascent: int = 0,
            em_descent: int = 0,
            line_ascent: int = 0,
            line_descent: int = 0,
            line_gap: int = 0,
            x_height: int = 0,
            cap_height: int = 0,
    ):
        self.em_ascent = em_ascent
        self.em_descent = em_descent
        self.line_ascent = line_ascent
        self.line_descent = line_descent
        self.line_gap = line_gap
        self.x_height = x_height
        self.cap_height = cap_height

    @property
    def em_height(self) -> int:
        return self.em_ascent + self.em_descent

    @property
    def line_height(self) -> int:
        return self.line_ascent + self.line_descent
