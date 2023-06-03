import model as m


class ResultScale:
    def __init__(self, key_note, scale, scale_degrees, scale_notes, diatonic_chords):
        self.key_note = key_note
        self.scale = scale
        self.scale_degrees = scale_degrees
        self.scale_notes = scale_notes
        self.diatonic_chords = diatonic_chords

    def pprint(self):
        print("key: {}".format(self.key_note))
        print("scale: {}".format(self.scale))
        print("scale_degrees: {}".format(self.scale_degrees))
        print("scale_notes: {}".format([str(x) for x in self.scale_notes]))
        print("--------")
        w0, w1 = 0, 0
        for c in self.diatonic_chords:
            w2, w3 = c.str_width()
            w0, w1 = max(w0, w2), max(w1, w3)
        for c in self.diatonic_chords:
            c.pprint(w0 + 1, w1 + 1)


class ResultChord:
    def __init__(self, root, degrees, notes) -> None:
        self.root = root
        self.degrees = degrees
        self.notes = notes

    def str_width(self):
        return len(str(self.root)), len(str(self.degrees))

    def pprint(self, w0, w1):
        degrees = str(self.degrees)
        notes = str([str(x) for x in self.notes])
        print("{:{}}".format(self.root, w0), end="")
        print("{:{}}".format(degrees, w1), end="")
        print("{}".format(notes))


def get_chord(shifted_intervals: list[int], idx: int):
    root_interval = shifted_intervals[idx]
    root = m.Note(root_interval % 12)

    rotated_intervals = shifted_intervals[idx:] + [
        x + 12 for x in shifted_intervals[:idx]
    ]
    notes = [m.Note(x % 12) for x in rotated_intervals]

    intervals_from_root = [x - root_interval for x in rotated_intervals]
    degrees = [m.Scale.interval_to_degree(y) for y in intervals_from_root]

    return ResultChord(root, degrees, notes)


def get_scale(key_note: m.Note, scale: m.Scale):
    scale_degrees = [m.Scale.interval_to_degree(x) for x in scale.to_intervals()]
    scale_notes = [m.Note((x + key_note.value) % 12) for x in scale.to_intervals()]

    shifted_intervals = [x + key_note.value for x in scale.to_intervals()]
    diatonic_chords = []
    for idx in range(len(shifted_intervals)):
        diatonic_chords.append(get_chord(shifted_intervals, idx))

    return ResultScale(key_note, scale, scale_degrees, scale_notes, diatonic_chords)
