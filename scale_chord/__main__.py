import argparse

import model as m
import usecase as u


parser = argparse.ArgumentParser()
parser.add_argument("--key", default="C", choices=m.Note.choices())
parser.add_argument("--scale", default="minor", choices=m.Scale.choices())
args = parser.parse_args()

key_note = m.Note.from_str(args.key)
scale = m.Scale.from_str(args.scale)

result = u.get_scale(key_note, scale)
result.pprint()
