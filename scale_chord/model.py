from __future__ import annotations

from enum import Enum, auto
from typing import Any


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

    def next(self) -> Note:
        return Note((self.value + 1) % 12)

    __note_to_str = {
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

    def __str__(self) -> str:
        return Note.__note_to_str[self.value]

    __str_to_note = {
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

    @classmethod
    def from_str(cls, note_str: str) -> Note:
        return Note(cls.__str_to_note[note_str])

    @classmethod
    def choices(cls) -> list[str]:
        return cls.__str_to_note.keys()

    def __lt__(self, other: Note) -> bool:
        return self.value < other.value


class Scale(Enum):
    Major = auto()
    Minor = auto()

    __scale_to_str = {
        Major: "major",
        Minor: "minor",
    }

    def __str__(self) -> str:
        return Scale.__scale_to_str[self.value]

    __scale_to_intervals = {
        Major: [0, 2, 4, 5, 7, 9, 11],
        Minor: [0, 2, 3, 5, 7, 8, 10],
    }

    def to_intervals(self) -> list[int]:
        return Scale.__scale_to_intervals[self.value]

    __str_to_scale = {
        "major": Major,
        "minor": Minor,
    }

    @classmethod
    def from_str(cls, scale_str: str) -> Scale:
        return Scale(cls.__str_to_scale[scale_str])

    __interval_to_degree = {
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

    @classmethod
    def interval_to_degree(cls, interval: int) -> str:
        return cls.__interval_to_degree[interval]

    @classmethod
    def choices(cls) -> list[str]:
        return cls.__str_to_scale.keys()

    __degree_to_interval = {
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
    def degree_to_interval(cls, degree: str) -> int:
        return cls.__degree_to_interval[degree]

    @classmethod
    def choices_degree(cls) -> list[str]:
        return cls.__degree_to_interval.keys()
