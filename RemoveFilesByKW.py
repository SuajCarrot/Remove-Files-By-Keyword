# A script to remove files if they have the specified keyword in their
# name.
#
# Copyright (C) 2021 Suaj
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

import yaml, sys, os
from os.path import isdir as is_dir
from os.path import isfile as is_file
from os.path import join as join_dirs
from datetime import datetime, date
from shutil import copytree

from assets.lang import *

with open(join_dirs(os.getcwd(), "assets", "config.yaml"), "rb") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
msg = spanish_messages if config["lang"] == "Spanish" else english_messages

# Meaning of the name of the arguments that we'll use:
# dir is directory
# kw is keyword
# path instead of dir because dir is a built-in function
# k_r is keep_remove
# ext is extract
# ext_dir is extract_dir
# verb is verbose
# rec is recursive
# ncs is NoCaseSensitive

# This function is for the verbose argument, but can be used for other things
def void_function(*args):
    pass

# Main function
def main( kw, path, k_r, ext, ext_dir, verb, ask, rec, ncs, log, log_dir ):
    # Instead of using conditions each time we have to print something, we
    # make our variable an alias for print if the arg is true and if it's
    # not we make our variable an alias for void_function
    vprint = print if verb else void_function

    if ext:
        vprint(msg["creating_ext_dir"])
        try:
            copytree(path, ext_dir)
        except FileExistsError:
            # We could try a different name, but it could be used too, and
            # the next one too...
            conf = input(msg["ext_dir_already_exists"])
            path = ext_dir if conf.lower() in ("y", "yes") else sys.exit(0)
        else:
            path = ext_dir

    vprint(msg["removing_files_in_path"] % (path))
    kw = kw.lower() if ncs else kw  # NoCaseSensitive argument
    removed_files = []  # For the log argument

    # Iterate over the files in the path
    for i in [ j for j in os.listdir(path) if is_file( join_dirs(path, j) ) ]:
        # We use a different variable called "file_name" instead of applying
        # str.lower to i itself so we can use the os.remove method with it
        fname = i.lower() if ncs else i

        if (kw in fname and k_r == "r") or (kw not in fname and k_r == "k"):
            # If the ask arg is False, the conf becomes True by default
            conf = input(msg["remove_i?"] % (i)) if ask else True
            if conf.lower() in ("n", "no"):
                vprint(msg["i_not_removed"] % (i))
            else:
                vprint(msg["removing_i"] % (i), end='')
                try:
                    os.remove(join_dirs(path, i))
                # This is to avoid collapsing if a file raises an exception
                except Exception as identifier:
                    print(msg["exception_occurred"] % (identifier))
                else:
                    removed_files.append(i)
                    vprint(msg["done_msg"])

    # If the rec argument is True, iterate over the directories in the path
    sub_dirs = [ j for j in os.listdir(path) if is_dir( join_dirs(path, j) ) ]
    if rec and len(sub_dirs) > 0:
        for i in sub_dirs:
        # The function calls itself with the path being the sub-directory
            main( kw, join_dirs(path, i), k_r, ext, ext_dir, verb, ask, rec,
                ncs, log, log_dir )
    else:
        vprint(msg["finished_msg"])

    if log and len(removed_files) > 0:
        # Name of the log file with the current date and time
        log_name = "{} {} log.txt".format(date.today().strftime("%Y-%m-%d"),
            datetime.now().strftime("%H:%M"))
        with open(log_file_name, "a") as f:
            f.write(msg["list_of_files_removed_in_path"] % (path))
            f.writelines(removed_files)


# Check for the arguments
del(sys.argv[0])  # It's the program's name, we don't need it
args, argc = sys.argv, len(sys.argv)  # This just improves readability

# Check if we have enough arguments
if argc == 0:
    print(msg["no_args_were_given"])
    sys.exit(0)

# Check if it's the help argument
elif argc == 1:
    if args[0] == "-h":
        print(msg["help_msg"])
        sys.exit(0)
    else:
        print(msg["missing_arg"])
        sys.exit(0)

# The last 2 arguments should be the keyword and the path
# Now check if path exists and keyword is valid
else:
    path = args[argc - 1]
    kw = args[argc - 2]
    if not is_dir(path):
        print(msg["dir_does_not_exist"] % (path))
        sys.exit(0)

    if "/" or "\\" in kw:
        print(msg["keyword_cant_have_chars"])
        sys.exit(0)

# Check for the arguments
# Structure: arg = (DefaultValue, ValueIfTrue)[arg in args]
# The arguments that have sub-arguments are checked differently to allow
# nested conditions which are necessary/really convenient in this case
k_r = (config["k_r"], "k")["-k" in args]
if "-e" in args:
    ext = True
    poss_dir = args.index("-e") + 1
    ext_dir = args[poss_dir] if is_dir(poss_dir) else \
        join_dirs(args[argc - 1], "Extracted")
else:
    ext = config["ext"]
    ext_dir = join_dirs(args[argc - 1], "Extracted")
verb = (config["verb"], True)["-v" in args]
ask = (config["ask"], False)["-da" in args]
rec = (config["rec"], True)["-r" in args]
ncs = (config["ncs"], True)["-ncs" in args]
if "-l" in args:
    log = True
    poss_dir = args.index("-e") + 1
    log_dir = args[poss_dir] if is_dir(poss_dir) else os.getcwd()
else:
    log = config["ext"]
    log_dir = os.getcwd()

# Call the main function with the collected arguments
main( kw, path, k_r, ext, ext_dir, verb, ask, rec, ncs, log, log_dir )

# End of boring code, thanks for stopping by!

