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

import sys, os
from os.path import isdir as is_dir
from os.path import isfile as is_file
from os.path import join as join_dir
from datetime import datetime, date
from shutil import copytree

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
        try:
            copytree(path, ext_dir)
            vprint("Creating sub-directory \"Extracted\"...")
        except FileExistsError:
            # We could try a different name, but it could be used too, and
            # the next one too...
            conf = input("The sub-directory \"Extracted\" already exists, \
use it instead? [y/N (abort)]")
            path = ext_dir if conf.lower() in ("y", "yes") else sys.exit(0)
        else:  # If no exceptions raised, change the path to the sub-dir
            path = ext_dir
    # These empty else blocks are just for readability and to make sure the
    # code doesn't do anything weird later
    else:
        pass
    vprint(f"Removing all files in {path}...")

    if ncs:  # NoCaseSensitivity argument
        kw = kw.lower()
    else:
        pass

    removed_files = []  # For the log argument

    # Iterate over the files in the path
    for i in [ j for j in os.listdir(path) if is_file( join_dirs(path, j) ) ]:
        # We use a different variable called "file_name" instead of applying
        # str.lower to i itself so we can use the os.remove method with it
        fname = i.lower() if ncs else i

        # These conditions are simpler than they look
        if (kw in fname and k_r == "r") or (kw not in fname and k_r == "k"):
            # If the ask arg is False, the conf becomes True by default
            conf = input("Remove {i}? [Y/n] ") if ask else True
            if conf.lower() in ("n", "no"):
                vprint("{i} will not be removed.")
            else:
                # The end parameter is there for printing sugar, see the next
                # print functions to see what I'm referring to
                vprint(f"Removing {i}...", end= '')
                try:  # Try to remove the file
                    os.remove(join_dirs(path, i))
                # This is to avoid collapsing if a file raises an exception
                except Exception as id:
                    print(f"An exception occurred.\nException Details: {id}")
                else:  # If it didn't, register the removed file
                    removed_files.append(i)
                    vprint("Done.")
        else:  # Again, just for readability and to avoid weird stuff
            pass

    # If the rec argument is True, iterate over the directories in the path
    sub_dirs = [ j for j in os.listdir(path) if is_dir( join_dirs(path, j) ) ]
    if rec and len(sub_dirs) > 0:
        for i in sub_dirs:
        # The function calls itself with the path being the sub-directory
            main( kw, join_dirs(path, i), k_r, ext, ext_dir, verb, ask, rec,
                ncs, log, log_dir )
    else:
        vprint("Finished.")

    if log and len(removed_files) > 0:
        # Name of the log file with the current date and time
        log_name = "{} {} log.txt".format(date.today().strftime("%Y-%m-%d"),
            datetime.now().strftime("%H:%M"))
        with open(log_file_name, "a") as f:
            f.write(f"List of files removed in {path}:\n")
            f.writelines(removed_files)
    else:
        pass
# End of the main function


# Check for the arguments
del(sys.argv[0])  # It's the program's name, we don't need it
args, argc = sys.argv, len(sys.argv)  # This just improves readability

# Check if we have enough arguments
if argc == 0:
    print("No arguments were given.\nUse \"-h\" for more details.")
    sys.exit(0)

# Check if it's the help argument
elif argc == 1:
    if args[0] == "-h" or args[0] == "--help":
        print("""
Remove the files inside a directory that have the specified
keyword in their name. Usage:

CLI> python3 RemoveFiles.py [arguments] [keyword] [directory]

Some arguments can also have sub-arguments. For example:

CLI> python3 RemoveFiles.py -e /my/dir -da hello /foo/bar
                            ^     ^
Could be interpreted as: extract here
If your directory has spaces, use quotes:

\"/dire c/tory w/ith s/pa ces/\"

Unrecognized arguments will be ignored.

Arguments/Options:

-h, --help       Get information about the program.

-e, --extract    Copy the given directory and its files
                 into a sub-directory and manipulate the
                 files inside of it.
                 Optional: If an existing directory is
                 specified after the argument, use it
                 instead of creating a sub-directory.

-k, --keep       Instead of removing the files, keep them
                 and remove the ones that don't have the
                 keyword in their name.

-v, --verbose    Print the action being done.

-da, --dont-ask  Don't ask before deleting a file.

-r, --recursive  Also manipulate the files inside
                 sub-directories.

-ncs, --no-case-sens  Ignore all uppercase letters,
                      including the ones in the keyword.

-l, --log        Write the list of removed files to a
                 TXT file in the same directory where
                 the script is located.
                 Optional: If an existing directory is
                 specified after the argument, write the
                 log to it instead of using the
                 directory where the script is located.

""")
        sys.exit(0)
    else:
        print("Missing argument: keyword\nUse \"-h\" for more details.")
        sys.exit(0)

# The last 2 arguments should be the keyword and the path
# Now check if path exists and keyword is valid
else:
    path = args[argc - 1]
    kw = args[argc - 2]
    if not is_dir(path):
        print(f"The directory {args[argc - 1]} does not exist.")
        sys.exit(0)
    else:
        pass

    if "/" or "\\" in kw:
        print(f"The keyword cannot have the \"/\" or \"\\\" characters.")
        sys.exit(0)
    else:
        pass

# Iterate over the arguments
# TO-DO: Change this method, it is horribly unoptimized
#    We could use something like "if arg in args arg else default"
# TO-DO: Add an argument to print the total execution time
# TO-DO: Allow the user to change these values with a file
for i in args:
    # Structure:
    # value if: (short argument is set or long argument is set) else: default

    k_r = "k" if i == "-k" or i == "--keep" else "r"
    ext = True if i == "-e" or i == "--extract" else False
    # Only valid if the previous argument was -e or --extract
    ext_dir = i if ( args[i - 1] == "-e" or args[i - 1] == "--extract" ) \
        and is_dir(i) else join_dirs(args[argc - 1], "Extracted")
    verb = True if i == "-v" or i == "--verbose" else False
    ask = False if i == "-da" or i == "--dont-ask" else True
    rec = True if i == "-r" or i == "--recursive" else False
    ncs = True if i == "-ncs" or i == "--no-case-sens" else False
    log = True if i == "-l" or i == "--log" else False
    # Only valid if the previous argument was -l or --log
    log_dir = i if ( args[i - 1] == "-l" or args[i - 1] == "--log" ) \
        and is_dir(i) else os.getcwd()

# Call the main function with the collected arguments
main( kw, path, k_r, ext, ext_dir, verb, ask, rec, ncs, log, log_dir )

# End of boring code, thanks for stopping by!

