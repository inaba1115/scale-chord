from __future__ import annotations

from dataclasses import dataclass

import model as m


@dataclass
class Result:
    a_key_note: m.Note
    a_degrees: list[str]
    a_scale_notes: list[m.Note]
    b_key_note: m.Note
    b_degrees: list[str]
    b_scale_notes: list[m.Note]
    x0: list[m.Note]
    x1: list[m.Note]
    x2: list[m.Note]
    x3: list[m.Note]
    x4: list[m.Note]

    def pprint(self) -> None:
        a_scale_notes = [str(x) for x in self.a_scale_notes]
        b_scale_notes = [str(x) for x in self.b_scale_notes]
        x0 = [str(x) for x in self.x0]
        x1 = [str(x) for x in self.x1]
        x2 = [str(x) for x in self.x2]
        x3 = [str(x) for x in self.x3]
        x4 = [str(x) for x in self.x4]

        w0 = max(len(str(self.a_key_note)), len(str(self.b_key_note))) + 1
        w1 = max(len(str(self.a_degrees)), len(str(self.b_degrees))) + 1

        print("a: ", end="")
        print("{:{}}".format(self.a_key_note, w0), end="")
        print("{:{}}".format(str(self.a_degrees), w1), end="")
        print("{}".format(a_scale_notes))
        print("b: ", end="")
        print("{:{}}".format(self.b_key_note, w0), end="")
        print("{:{}}".format(str(self.b_degrees), w1), end="")
        print("{}".format(b_scale_notes))
        print("a & b: {}".format(x0))
        print("a | b: {}".format(x1))
        print("a ^ b: {}".format(x2))
        print("a - b: {}".format(x3))
        print("b - a: {}".format(x4))


def get_logic(
    a_key_note: m.Note, a_degrees: list[str], b_key_note: m.Note, b_degrees: list[str]
) -> list[m.Note]:
    a_intervals = [m.Scale.degree_to_interval(x) for x in a_degrees]
    a_scale_notes = [m.Note((x + a_key_note.value) % 12) for x in a_intervals]

    b_intervals = [m.Scale.degree_to_interval(x) for x in b_degrees]
    b_scale_notes = [m.Note((x + b_key_note.value) % 12) for x in b_intervals]

    a = set(a_scale_notes)
    b = set(b_scale_notes)

    x0 = sorted(list(a & b))
    x1 = sorted(list(a | b))
    x2 = sorted(list(a ^ b))
    x3 = sorted(list(a - b))
    x4 = sorted(list(b - a))

    return Result(
        a_key_note,
        a_degrees,
        a_scale_notes,
        b_key_note,
        b_degrees,
        b_scale_notes,
        x0,
        x1,
        x2,
        x3,
        x4,
    )
