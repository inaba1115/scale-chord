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
        strings = [6, 5, 4, 3, 2, 1]
        fingerboard = {}
        for nth in strings:
            fingerboard[nth] = cls.__nth_string(nth, key_note, scale_notes, max_flet)

        for flet in range(max_flet + 1):
            for nth in strings:
                print("|{:8}".format(fingerboard[nth][flet]), end="")
            print("|")
