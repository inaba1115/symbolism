import mido  # type: ignore


def sec_to_tick(sec: float) -> int:
    return mido.second2tick(sec, ticks_per_beat=480, tempo=500000)


def get_output_names() -> list[str]:
    return mido.get_output_names()


def play(port: str, fname: str) -> None:
    with mido.open_output(port) as outport:
        mid = mido.MidiFile(fname)
        for msg in mid.play():
            outport.send(msg)
