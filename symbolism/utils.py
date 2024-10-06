import mido  # type: ignore


def sec_to_tick(sec: float) -> int:
    return mido.second2tick(sec, ticks_per_beat=480, tempo=500000)
