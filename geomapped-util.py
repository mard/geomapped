#!/usr/bin/env python3

import os, glob, argparse, json, piexif

def main():
  if args.path:
    get_files()
  else:
    print('No arguments. -h or --help for more information')

def get_files():
  for filename in glob.iglob(args.path, recursive=True):
    print(filename)

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('path', help='path to a file or directory')
  args = parser.parse_args()
  main()