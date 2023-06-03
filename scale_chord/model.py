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

note_to_str = {
    Note.C: "C",
    Note.CsDb: "C#/Db",
    Note.D: "D",
    Note.DsEb: "D#/Eb",
    Note.E: "E",
    Note.F: "F",
    Note.FsGb: "F#/Gb",
    Note.G: "G",
    Note.GsAb: "G#/Ab",
    Note.A: "A",
    Note.AsBb: "A#/Bb",
    Note.B: "B",
}

class Scale(Enum):
    Major = auto()
    Minor = auto()


scale_map = {
    Scale.Major: [0, 2, 4, 5, 7, 9, 11],
    Scale.Minor: [0, 2, 3, 5, 7, 8, 10],
}

x_to_degree = {
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


def get_chord(xs: list[int], idx: int):
    root = xs[idx]
    print(Note(root%12))

    foos = xs[idx:] + [x+12 for x in xs[:idx]]
    bars = [note_to_str[Note(x%12)] for x in foos]
    print(bars)

    ys = [y-root for y in foos]
    ys = [x_to_degree[y] for y in ys]
    print(ys)

    #notes = [Note(x) for x in ys]
    #notes_str = [note_to_str[x] for x in notes]
    #print(ys)
    #print(notes_str)
    


def get_scale_notes(key_note: Note, scale_type: Scale):
    xs = [x + key_note.value for x in scale_map[scale_type]]
    zzz = [x%12 for x in xs]
    print(scale_map[scale_type])
    zzz = [note_to_str[Note(x)] for x in zzz]
    print(zzz)

    for idx in range(len(xs)):
        get_chord(xs, idx)

    #notes = [Note(x) for x in xs]
    #notes_str = [note_to_str[x] for x in notes]
    #print(notes_str)


    pass

# foo --key A#/Bb --scale minor

# foo --key C --scale major
# C D E F G A B
# C [1, 3, 5] [C, E, G]
# D [1, b3, 5] [D, F, A]
# ...

get_scale_notes(Note.AsBb, Scale.Minor)