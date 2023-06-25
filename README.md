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
|0       |(F)     |(F#/Gb) |3       |(G#/Ab) |5       |[A#/Bb] |7       |(C)     |(C#/Db) |10      |(D#/Eb) |12      |(F)     |(F#/Gb) |15      |
|0       |(C)     |(C#/Db) |3       |(D#/Eb) |5       |(F)     |(F#/Gb) |8       |(G#/Ab) |10      |[A#/Bb] |12      |(C)     |(C#/Db) |15      |
|0       |(G#/Ab) |2       |[A#/Bb] |4       |(C)     |(C#/Db) |7       |(D#/Eb) |9       |(F)     |(F#/Gb) |12      |(G#/Ab) |14      |[A#/Bb] |
|0       |(D#/Eb) |2       |(F)     |(F#/Gb) |5       |(G#/Ab) |7       |[A#/Bb] |9       |(C)     |(C#/Db) |12      |(D#/Eb) |14      |(F)     |
|0       |[A#/Bb] |2       |(C)     |(C#/Db) |5       |(D#/Eb) |7       |(F)     |(F#/Gb) |10      |(G#/Ab) |12      |[A#/Bb] |14      |(C)     |
|0       |(F)     |(F#/Gb) |3       |(G#/Ab) |5       |[A#/Bb] |7       |(C)     |(C#/Db) |10      |(D#/Eb) |12      |(F)     |(F#/Gb) |15      |
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
