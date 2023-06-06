import argparse

import logic as l
import model as m
import scale as s


def cmd_scale(args):
    key_note = m.Note.from_str(args.key)
    degrees = args.degrees.split(",")
    result = s.do_scale(key_note, degrees)
    result.pprint()


def cmd_logic(args):
    a_key_note = m.Note.from_str(args.a_key)
    a_degrees = args.a_degrees.split(",")
    b_key_note = m.Note.from_str(args.b_key)
    b_degrees = args.b_degrees.split(",")
    result = l.do_logic(a_key_note, a_degrees, b_key_note, b_degrees)
    result.pprint()


parser = argparse.ArgumentParser()
subparser = parser.add_subparsers()
subparser.required = True

parser_scale = subparser.add_parser("scale")
parser_scale.add_argument("--key", default="C", choices=m.Note.choices())
parser_scale.add_argument("--degrees", default="1,3,5")  # TODO: choices
parser_scale.set_defaults(func=cmd_scale)

parser_logic = subparser.add_parser("logic")
parser_logic.add_argument("--a_key", default="C", choices=m.Note.choices())
parser_logic.add_argument("--a_degrees", default="1,3,5")  # TODO: choices
parser_logic.add_argument("--b_key", default="A", choices=m.Note.choices())
parser_logic.add_argument("--b_degrees", default="1,b3,5")  # TODO: choices
parser_logic.set_defaults(func=cmd_logic)

args = parser.parse_args()
args.func(args)
