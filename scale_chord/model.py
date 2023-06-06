from __future__ import annotations

from enum import Enum, auto


class Note(Enum):
    C = 0
    CsDb = auto()
    D = auto()
    DsEb = auto()
    E = auto()
    F = auto()
    FsGb = auto()
    G = auto()
    GsAb = auto()
    A = auto()
    AsBb = auto()
    B = auto()

    __STR_TO_NOTE = {
        "C": C,
        "C#/Db": CsDb,
        "D": D,
        "D#/Eb": DsEb,
        "E": E,
        "F": F,
        "F#/Gb": FsGb,
        "G": G,
        "G#/Ab": GsAb,
        "A": A,
        "A#/Bb": AsBb,
        "B": B,
    }

    __NOTE_TO_STR = {
        C: "C",
        CsDb: "C#/Db",
        D: "D",
        DsEb: "D#/Eb",
        E: "E",
        F: "F",
        FsGb: "F#/Gb",
        G: "G",
        GsAb: "G#/Ab",
        A: "A",
        AsBb: "A#/Bb",
        B: "B",
    }

    @classmethod
    def from_str(cls, note_str: str) -> Note:
        return Note(cls.__STR_TO_NOTE[note_str])

    @classmethod
    def choices(cls) -> list[str]:
        return cls.__STR_TO_NOTE.keys()

    def __str__(self) -> str:
        return Note.__NOTE_TO_STR[self.value]

    def __lt__(self, other: Note) -> bool:
        return self.value < other.value

    def next(self) -> Note:
        return Note((self.value + 1) % 12)


class Degree:
    __INTERVAL_TO_DEGREE = {
        0: "1",
        1: "b2",
        2: "2",
        3: "b3",
        4: "3",
        5: "4",
        6: "#4",
        7: "5",
        8: "b6",
        9: "6",
        10: "b7",
        11: "7",
    }

    __DEGREE_TO_INTERVAL = {
        "1": 0,
        "b2": 1,
        "2": 2,
        "b3": 3,
        "3": 4,
        "4": 5,
        "#4": 6,
        "5": 7,
        "b6": 8,
        "6": 9,
        "b7": 10,
        "7": 11,
    }

    @classmethod
    def interval_to_degree(cls, interval: int) -> str:
        return cls.__INTERVAL_TO_DEGREE[interval]

    @classmethod
    def degree_to_interval(cls, degree: str) -> int:
        return cls.__DEGREE_TO_INTERVAL[degree]

    @classmethod
    def choices(cls) -> list[str]:
        return cls.__DEGREE_TO_INTERVAL.keys()


class Scale:
    @classmethod
    def gen_scale(cls, key_note: Note, degrees: list[str]) -> list[Note]:
        intervals = [Degree.degree_to_interval(x) for x in degrees]
        scale = [Note((x + key_note.value) % 12) for x in intervals]
        return scale


class Chord:
    @classmethod
    def gen_chord(
        cls, key_note: Note, degrees: list[str], idx: int
    ) -> tuple(Note, list[str], list[Note]):
        intervals = [Degree.degree_to_interval(x) for x in degrees]
        shifted_intervals = [x + key_note.value for x in intervals]

        root_interval = shifted_intervals[idx]
        rotated_intervals = shifted_intervals[idx:] + [
            x + 12 for x in shifted_intervals[:idx]
        ]

        chord_intervals = [x - root_interval for x in rotated_intervals]
        chord_degrees = [Degree.interval_to_degree(y) for y in chord_intervals]
        chord_notes = [Note(x % 12) for x in rotated_intervals]
        chord_root = chord_notes[0]

        return chord_root, chord_degrees, chord_notes
