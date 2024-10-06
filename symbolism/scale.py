from dataclasses import dataclass


@dataclass
class Scale:
    root: int
    degrees: list[int]

    def __post_init__(self):
        if self.root < 0 or 11 < self.root:
            raise ValueError
        if len(self.degrees) != len(set(self.degrees)):
            raise ValueError
        if max(self.degrees) < 0 or 11 < max(self.degrees):
            raise ValueError

    def map(self, x: int) -> int:
        octave = x // len(self.degrees)
        y = x % len(self.degrees)
        return octave * 12 + self.degrees[y] + self.root
