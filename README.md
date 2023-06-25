# scale-chord

## usage

scale
```
$ poetry run python -m scale_chord scale --key A#/Bb --degrees 1,2,b3,4,5,b6,b7
key: A#/Bb
degrees: ['1', '2', 'b3', '4', '5', 'b6', 'b7']
notes: ['A#/Bb', 'C', 'C#/Db', 'D#/Eb', 'F', 'F#/Gb', 'G#/Ab']
--------
A#/Bb ['1', '2', 'b3', '4', '5', 'b6', 'b7']   ['A#/Bb', 'C', 'C#/Db', 'D#/Eb', 'F', 'F#/Gb', 'G#/Ab']
C     ['1', 'b2', 'b3', '4', '#4', 'b6', 'b7'] ['C', 'C#/Db', 'D#/Eb', 'F', 'F#/Gb', 'G#/Ab', 'A#/Bb']
C#/Db ['1', '2', '3', '4', '5', '6', '7']      ['C#/Db', 'D#/Eb', 'F', 'F#/Gb', 'G#/Ab', 'A#/Bb', 'C']
D#/Eb ['1', '2', 'b3', '4', '5', '6', 'b7']    ['D#/Eb', 'F', 'F#/Gb', 'G#/Ab', 'A#/Bb', 'C', 'C#/Db']
F     ['1', 'b2', 'b3', '4', '5', 'b6', 'b7']  ['F', 'F#/Gb', 'G#/Ab', 'A#/Bb', 'C', 'C#/Db', 'D#/Eb']
F#/Gb ['1', '2', '3', '#4', '5', '6', '7']     ['F#/Gb', 'G#/Ab', 'A#/Bb', 'C', 'C#/Db', 'D#/Eb', 'F']
G#/Ab ['1', '2', '3', '4', '5', '6', 'b7']     ['G#/Ab', 'A#/Bb', 'C', 'C#/Db', 'D#/Eb', 'F', 'F#/Gb']
--------
|..      |F       |F#/Gb   |.       |G#/Ab   |.       |[A#/Bb] |.       |C       |C#/Db   |        |D#/Eb   |..      |F       |F#/Gb   |.       |
|..      |C       |C#/Db   |.       |D#/Eb   |.       |F       |F#/Gb   |        |G#/Ab   |        |[A#/Bb] |..      |C       |C#/Db   |.       |
|..      |G#/Ab   |        |[A#/Bb] |        |C       |C#/Db   |.       |D#/Eb   |        |F       |F#/Gb   |..      |G#/Ab   |        |[A#/Bb] |
|..      |D#/Eb   |        |F       |F#/Gb   |.       |G#/Ab   |.       |[A#/Bb] |        |C       |C#/Db   |..      |D#/Eb   |        |F       |
|..      |[A#/Bb] |        |C       |C#/Db   |.       |D#/Eb   |.       |F       |F#/Gb   |        |G#/Ab   |..      |[A#/Bb] |        |C       |
|..      |F       |F#/Gb   |.       |G#/Ab   |.       |[A#/Bb] |.       |C       |C#/Db   |        |D#/Eb   |..      |F       |F#/Gb   |.       |
```

logic
```
$ poetry run python -m scale_chord logic --a_key A#/Bb --a_degrees 1,2,b3,4,5,b6,b7 --b_key E --b_degrees 1,3,5,b7
a: A#/Bb ['1', '2', 'b3', '4', '5', 'b6', 'b7'] ['A#/Bb', 'C', 'C#/Db', 'D#/Eb', 'F', 'F#/Gb', 'G#/Ab']
b: E     ['1', '3', '5', 'b7']                  ['E', 'G#/Ab', 'B', 'D']
a & b: ['G#/Ab']
a | b: ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G#/Ab', 'A#/Bb', 'B']
a ^ b: ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'A#/Bb', 'B']
a - b: ['C', 'C#/Db', 'D#/Eb', 'F', 'F#/Gb', 'A#/Bb']
b - a: ['D', 'E', 'B']
```
