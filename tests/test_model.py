import scale_chord.model as m


def test_note_from_str():
    got = m.Note.from_str("C")
    want = m.Note.C
    assert got == want


def test_note_str():
    got = str(m.Note.C)
    want = "C"
    assert got == want


def test_note_lt():
    got = sorted([m.Note.C, m.Note.G, m.Note.E])
    want = [m.Note.C, m.Note.E, m.Note.G]
    assert got == want


def test_note_next():
    got = m.Note.B.next()
    want = m.Note.C
    assert got == want


def test_degree_interval_to_degree():
    got = m.Degree.interval_to_degree(5)
    want = "4"
    assert got == want


def test_degree_degree_to_interval():
    got = m.Degree.degree_to_interval("4")
    want = 5
    assert got == want


def test_scale_gen_scale():
    got = m.Scale.gen_scale(m.Note.C, ["1", "2", "3", "4", "5", "6", "7"])
    want = [m.Note.C, m.Note.D, m.Note.E, m.Note.F, m.Note.G, m.Note.A, m.Note.B]
    assert got == want


def test_chord_gen_chord():
    got_chord_root, got_chord_degrees, got_chord_notes = m.Chord.gen_chord(
        m.Note.C, ["1", "2", "3", "4", "5", "6", "7"], 3
    )

    want_chord_root = m.Note.F
    want_chord_degrees = ["1", "2", "3", "#4", "5", "6", "7"]
    want_chord_notes = [
        m.Note.F,
        m.Note.G,
        m.Note.A,
        m.Note.B,
        m.Note.C,
        m.Note.D,
        m.Note.E,
    ]

    assert got_chord_root == want_chord_root
    assert got_chord_degrees == want_chord_degrees
    assert got_chord_notes == want_chord_notes
