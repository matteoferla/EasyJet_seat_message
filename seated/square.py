from enum import Enum
from collections import namedtuple

Border = Enum('border', names=['none', 'inner', 'outer'])
Border.__doc__ = 'The grey box around or inside the squares or absent'
Line = Enum('line', names=['square', 'TL', 'TR', 'BR', 'BL'])
Line.__doc__ = 'The orange line (T: Top, B: bottom, R: Right, L: Left)'


class Square:
    def __init__(self, border: Border, line: Line) -> None:
        self.border = border
        self.line = line

    def __hash__(self):
        """
        To allow eq to work. Not to be used for decoding.
        """
        return self.border.value * 10 + self.line.value

    def __eq__(self, other):
        return hash(self) == hash(other)