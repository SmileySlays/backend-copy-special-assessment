#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
import subprocess
import argparse

# This is to help coaches and graders identify student assignments
__author__ = "SmileySlays"


# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dir):
    """Returns a list of the absolute paths of the special files in the given directory"""
    os.chdir(dir)
    paths_list = []
    for files in os.listdir():
        match = re.findall(r'_(\w+)_', files)
        if len(match) > 0:
            paths_list.append(os.path.abspath(files))
    return paths_list


def copy_to(paths, dir):
    """Given a list of paths, copies those files into the given directory"""
    if os.path.exists(dir):
        for path in paths:
            shutil.copy(path, dir)
    else:
        os.makedirs(dir)
        for path in get_special_paths(paths):
            shutil.copy(path, dir)


def zip_to(paths, zippath):
    """Given a list of paths, zip those files up into the given zipfile"""
    # for path in paths:
    cmd = ["zip", "-j", zippath]
    cmd.extend(paths)
    print("\n Command I'm Going To Do: " + " ".join(cmd) + "\n")
    # zip_files = subprocess.call(["zip", "-j", zippath, path])
    try:
        zip_files = subprocess.check_output(
            " ".join(cmd), stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        print(e.output.decode("utf-8"))
        exit(1)


def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO need an argument to pick up 'from_dir'
    parser.add_argument('from_dir', help='source dir')
    args = parser.parse_args()

    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    # +++your code here+++
    # Call your functions
    # if args.todir:
    # print(get_special_paths(args.todir))
    if args.todir:
        copy_to(args.from_dir, args.todir)

    elif args.tozip:
        zip_to(get_special_paths(args.from_dir), args.tozip)

    else:
        print('\n'.join(get_special_paths(args.from_dir)) + '\n')


if __name__ == "__main__":
    main()
