from __future__ import annotations

import model as m


class Guitar:
    __tuning = {
        6: m.Note.E,
        5: m.Note.A,
        4: m.Note.D,
        3: m.Note.G,
        2: m.Note.B,
        1: m.Note.E,
    }

    @classmethod
    def __nth_string(
        cls, nth: int, key_note: m.Note, scale_notes: list[m.Note], max_flet: int
    ) -> list[str]:
        x = cls.__tuning[nth]
        ret = []
        for flet in range(max_flet + 1):
            if x is key_note:
                ret.append("[{}]".format(str(x)))
            elif x in scale_notes:
                ret.append(str(x))
            else:
                ret.append(".")
            x = x.next()
        return ret

    @classmethod
    def pprint(cls, key_note: m.Note, scale_notes: list[m.Note], max_flet: int) -> None:
        strings = [1, 2, 3, 4, 5, 6]
        fingerboard = {}
        for nth in strings:
            fingerboard[nth] = cls.__nth_string(nth, key_note, scale_notes, max_flet)

        for nth in strings:
            for flet in range(max_flet + 1):
                print("|{:8}".format(fingerboard[nth][flet]), end="")
            print("|")


def get_scale_notes(key_note: m.Note, degrees: list[str]) -> list[m.Note]:
    intervals = [m.Scale.degree_to_interval(x) for x in degrees]
    scale_notes = [m.Note((x + key_note.value) % 12) for x in intervals]
    return scale_notes
