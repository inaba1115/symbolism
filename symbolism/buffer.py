import time
from dataclasses import dataclass, field

import mido  # type: ignore

from .note import Note
from .utils import sec_to_tick, tick_to_sec


@dataclass
class MidiEvent:
    typ: str
    midi_number: int
    velocity: int
    tick: int


@dataclass
class Buffer:
    notes: list[tuple[float, Note]] = field(default_factory=list)

    def add(self, t: float, note: Note) -> None:
        self.notes.append((t, note))

    def __make_track(self, bpm: float = 120) -> mido.MidiTrack:
        track = mido.MidiTrack()
        track.append(mido.MetaMessage("set_tempo", tempo=mido.bpm2tempo(bpm)))

        midi_events: list[MidiEvent] = []
        for t, note in self.notes:
            midi_events.append(MidiEvent("note_on", note.midi_number, note.velocity, sec_to_tick(t)))
            midi_events.append(MidiEvent("note_off", note.midi_number, note.velocity, sec_to_tick(t + note.gate_sec)))

        rc: dict[int, int] = {}
        t = 0
        for e in sorted(midi_events, key=lambda e: e.tick):
            dt = e.tick - t
            if e.typ == "note_on":
                if rc.get(e.midi_number, 0) == 0:
                    track.append(mido.Message(type="note_on", note=e.midi_number, velocity=e.velocity, time=dt))
                    rc[e.midi_number] = 1
                else:
                    track.append(mido.Message(type="note_off", note=e.midi_number, velocity=e.velocity, time=dt))
                    track.append(mido.Message(type="note_on", note=e.midi_number, velocity=e.velocity, time=0))
                    rc[e.midi_number] += 1
            elif e.typ == "note_off":
                if rc[e.midi_number] == 1:
                    track.append(mido.Message(type="note_off", note=e.midi_number, velocity=e.velocity, time=dt))
                    rc[e.midi_number] = 0
                else:
                    rc[e.midi_number] -= 1
                    continue
            t = e.tick
        return track

    def write(self, fname: str, bpm: float = 120) -> None:
        outfile = mido.MidiFile()
        track = self.__make_track(bpm)
        outfile.tracks.append(track)
        outfile.save(fname)

    def play(self, port: str) -> None:
        with mido.open_output(port) as outport:
            track = self.__make_track()

            now = time.time()
            for msg in track:
                if isinstance(msg, mido.MetaMessage):
                    continue

                now += tick_to_sec(msg.time)
                dt = now - time.time()
                if dt > 0:
                    time.sleep(dt)

                outport.send(msg)
