import mido  # type: ignore


def sec_to_tick(sec: float) -> int:
    return mido.second2tick(sec, ticks_per_beat=480, tempo=500000)


def tick_to_sec(tick: int) -> float:
    return mido.tick2second(tick, ticks_per_beat=480, tempo=500000)


def get_output_names() -> list[str]:
    return mido.get_output_names()
