import scale_chord.guitar_viewer as g
import scale_chord.model as m


def test_nth_string():
    nth = 6
    key_note = m.Note.C
    scale_notes = [m.Note.C, m.Note.D, m.Note.E, m.Note.F, m.Note.G, m.Note.A, m.Note.B]
    max_flet = 15

    got = g.GuitarViewer._GuitarViewer__nth_string(nth, key_note, scale_notes, max_flet)

    want = [
        "(E)",
        "(F)",
        "2",
        "(G)",
        "4",
        "(A)",
        "6",
        "(B)",
        "[C]",
        "9",
        "(D)",
        "11",
        "(E)",
        "(F)",
        "14",
        "(G)",
    ]
    assert got == want
