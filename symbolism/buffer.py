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
    channel: int


@dataclass
class Buffer:
    notes: list[Note] = field(default_factory=list)
    channels: set[int] = field(default_factory=set)

    def add_note(self, midi_number: int, velocity: int, start_sec: float, gate_sec: float, channel: int = 0) -> None:
        self.notes.append(Note(midi_number, velocity, start_sec, gate_sec, channel))
        self.channels.add(channel)

    def write(self, fname: str, bpm: float = 120) -> None:
        for channel in self.channels:
            outfile = mido.MidiFile()
            notes = [note for note in self.notes if note.channel == channel]
            track = make_track(notes, bpm)
            outfile.tracks.append(track)
            outfile.save(f"{channel}.{fname}")

    def play(self, port: str) -> None:
        with mido.open_output(port) as outport:
            track = make_track(self.notes, 120)

            now = time.time()
            for msg in track:
                if isinstance(msg, mido.MetaMessage):
                    continue

                now += tick_to_sec(msg.time)
                dt = now - time.time()
                if dt > 0:
                    time.sleep(dt)

                outport.send(msg)


def make_track(notes: list[Note], bpm: float) -> mido.MidiTrack:
    midi_events: list[MidiEvent] = []
    for note in notes:
        midi_events.append(MidiEvent("note_on", note.midi_number, note.velocity, sec_to_tick(note.start_sec), note.channel))
        midi_events.append(MidiEvent("note_off", note.midi_number, note.velocity, sec_to_tick(note.start_sec + note.gate_sec), note.channel))

    track = mido.MidiTrack()
    track.append(mido.MetaMessage("set_tempo", tempo=mido.bpm2tempo(bpm)))

    rc: dict[int, int] = {}
    t = 0
    for e in sorted(midi_events, key=lambda e: e.tick):
        dt = e.tick - t
        if e.typ == "note_on":
            if rc.get(e.midi_number, 0) == 0:
                track.append(mido.Message(type="note_on", note=e.midi_number, velocity=e.velocity, time=dt, channel=e.channel))
                rc[e.midi_number] = 1
            else:
                track.append(mido.Message(type="note_off", note=e.midi_number, velocity=e.velocity, time=dt, channel=e.channel))
                track.append(mido.Message(type="note_on", note=e.midi_number, velocity=e.velocity, time=0, channel=e.channel))
                rc[e.midi_number] += 1
        elif e.typ == "note_off":
            if rc[e.midi_number] == 1:
                track.append(mido.Message(type="note_off", note=e.midi_number, velocity=e.velocity, time=dt, channel=e.channel))
                rc[e.midi_number] = 0
            else:
                rc[e.midi_number] -= 1
                continue
        t = e.tick
    return track
