import argparse

import guitar as g
import logic as l
import model as m
import usecase as u


def cmd_scale(args):
    key_note = m.Note.from_str(args.key)
    scale = m.Scale.from_str(args.scale)
    result = u.get_scale(key_note, scale)
    result.pprint()


def cmd_guitar(args):
    root_note = m.Note.from_str(args.root)
    degrees = args.degrees.split(",")
    scale_notes = g.get_scale_notes(root_note, degrees)
    g.Guitar.pprint(root_note, scale_notes, 15)


def cmd_logic(args):
    a_key_note = m.Note.from_str(args.a_key)
    a_degrees = args.a_degrees.split(",")
    b_key_note = m.Note.from_str(args.b_key)
    b_degrees = args.b_degrees.split(",")
    result = l.get_logic(a_key_note, a_degrees, b_key_note, b_degrees)
    result.pprint()


parser = argparse.ArgumentParser()
subparser = parser.add_subparsers()
subparser.required = True

parser_scale = subparser.add_parser("scale")
parser_scale.add_argument("--key", default="C", choices=m.Note.choices())
parser_scale.add_argument("--scale", default="minor", choices=m.Scale.choices())
parser_scale.set_defaults(func=cmd_scale)

parser_guitar = subparser.add_parser("guitar")
parser_guitar.add_argument("--root", default="C", choices=m.Note.choices())
parser_guitar.add_argument("--degrees", default="1,b3,5")  # TODO: choices
parser_guitar.set_defaults(func=cmd_guitar)

parser_logic = subparser.add_parser("logic")
parser_logic.add_argument("--a_key", default="C", choices=m.Note.choices())
parser_logic.add_argument("--a_degrees", default="1,3,5")  # TODO: choices
parser_logic.add_argument("--b_key", default="A", choices=m.Note.choices())
parser_logic.add_argument("--b_degrees", default="1,b3,5")  # TODO: choices
parser_logic.set_defaults(func=cmd_logic)

args = parser.parse_args()
args.func(args)
