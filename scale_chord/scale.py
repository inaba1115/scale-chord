from __future__ import annotations

from dataclasses import dataclass

import scale_chord.guitar_viewer as g
import scale_chord.model as m


@dataclass
class ScaleResult:
    key_note: m.Note
    scale_degrees: list[str]
    scale_notes: list[m.Note]
    diatonic_chords: list[ChordResult]

    def pprint(self) -> None:
        print("key: {}".format(self.key_note))
        print("degrees: {}".format(self.scale_degrees))
        print("notes: {}".format([str(x) for x in self.scale_notes]))

        print("--------")

        w0, w1 = 0, 0
        for c in self.diatonic_chords:
            w2, w3 = c.str_width()
            w0, w1 = max(w0, w2), max(w1, w3)
        for c in self.diatonic_chords:
            c.pprint(w0 + 1, w1 + 1)

        print("--------")

        g.GuitarViewer.pprint(self.key_note, self.scale_notes, 15)


@dataclass
class ChordResult:
    root: m.Note
    degrees: list[str]
    notes: list[m.Note]

    def str_width(self) -> tuple[int, int]:
        return len(str(self.root)), len(str(self.degrees))

    def pprint(self, w0, w1) -> None:
        degrees = str(self.degrees)
        notes = str([str(x) for x in self.notes])
        print("{:{}}".format(self.root, w0), end="")
        print("{:{}}".format(degrees, w1), end="")
        print("{}".format(notes))


def do_scale(key_note: m.Note, degrees: list[str]) -> ScaleResult:
    notes = m.Scale.gen_scale(key_note, degrees)

    diatonic_chords = []
    for idx in range(len(degrees)):
        chord_root, chord_degrees, chord_notes = m.Chord.gen_chord(
            key_note, degrees, idx
        )
        diatonic_chords.append(ChordResult(chord_root, chord_degrees, chord_notes))

    return ScaleResult(key_note, degrees, notes, diatonic_chords)
