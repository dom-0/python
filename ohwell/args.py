#!/usr/bin/env python3

import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("dir", help="dir name")
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
parser.add_argument("-f", "--filename", help="name of the file", default="/etc/passwd")
parser.add_argument("-t", "--type", help="type of the file", required=True)
args = parser.parse_args()
print ("{} {} {} {}".format(args.dir, args.verbose, args.filename, args.type))
