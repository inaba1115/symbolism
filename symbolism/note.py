from dataclasses import dataclass


@dataclass
class Note:
    midi_number: int
    velocity: int
    gate_sec: float

    def __post_init__(self):
        if self.midi_number < 0 or 127 < self.midi_number:
            raise ValueError
        if self.velocity < 0 or 127 < self.velocity:
            raise ValueError
        if self.gate_sec <= 0:
            raise ValueError
