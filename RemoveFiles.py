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

from datetime import datetime, date
import shutil, sys, os

# Main function
def main_func(keyword, directory, extract, extract_dir, k_r,
              verbose, ask, recursive, ncs, log):
    if extract:  # Create the sub-directory
        try:
            shutil.copytree(directory, extract_dir)
            if verbose:
                print("Creating sub-directory \"Extracted\"...")

        # The program could try a different name, but that
        # name could also be used, and the next one too...

        except FileExistsError:
            conf = input("The sub-directory \"Extracted\" \
already exists.\nCopy the files to it? [Y/n (abort)]")
            if conf.lower() in ["n", "a", "no", "abort"]:
                print("Aborting...")
                sys.exit(0)
            else:  # Y is the default value
                directory = extract_dir

        else:  # Change the directory to the sub-directory
            directory = extract_dir

    if verbose:
        print(f"Removing all files in {directory}...")

    conf = True  # Default value for the "ask" block

    if ncs:  # NoCaseSensitivity argument
        keyword = keyword.lower()

    removed_files = []  # For the log argument
    # Name of the log file with the date and time
    fname = "{}/{} {}.txt".format(os.getcwd(),
            date.today().strftime("%Y-%m-%d"),
            datetime.now().strftime("%H:%M"))

    if log:  # Write the header of the log file
        with open(fname, "a") as f:
            f.write(f"List of files removed in {directory}:\n")

    for i in os.listdir(directory):  # Check each file
        if ncs:  # NoCaseSensitivity argument
            i = i.lower()
        # Conditions
        if (keyword not in i and k_r == "k") \
        or (keyword in i and k_r == "r"):
            # Only if the value is an existing file
            if os.path.isfile(f"{directory}/{i}"):
                if ask:  # Ask for confirmation
                    conf = input(f"Remove {i}? [Y/n] ")
                    if conf.lower() in ["no", "n"]:
                        conf = False
                        if verbose:
                            print("{i} will not be removed.")
                    else:  # Y is the default value
                        conf = True
                if conf:
                    if verbose:  # Verbose argument
                        print(f"Removing {i}... ", end='')
                    try:  # Remove the file
                        os.remove(f"{directory}/{i}")
                    # This is to avoid the program collapsing
                    # if a single file raises an exception
                    except Exception as id:
                        print(f"""
An exception occurred.
Exception details: {id}
""")
                    else:
                        # Register the removed file
                        removed_files.append(i)
                        if verbose:
                            print("Done.")
            # In case it is a directory, try recursivity
            elif os.path.isdir(f"{directory}/{i}"):
                if recursive:
                    # The function calls itself with the
                    # directory being the sub-directory
                    main_func(keyword, f"{directory}/{i}",
                              extract, k_r, verbose, ask,
                              recursive, ncs, log)
                    if verbose:
                        print(f"{i} is a directory. Removing \
files inside of it...")
                elif not recursive and verbose:
                    print(f"{i} is a directory. Skipping...")

            else:  # It probably doesn't exist
                if verbose:
                    print(f"ERROR: {i} doesn't exist.")
    if verbose:
        print("Done.")

    if log:  # Write to a file the list of removed files
        with open(fname, "a") as f:
            if len(removed_files) > 0:
                f.writelines(removed_files)
            else:
                f.write("No files were removed.\n\n")


# Default option values

# TO-DO: Allow the user to change the default values with a
# file

# TO-DO: Add a sub-argument for the log argument that allows
# the user to specify the directory where the file will be
# written to.

extract_dir = "unknown"
recursive = False
extract = False
verbose = False
ncs = False
log = False
ask = True
k_r = "r"  # Keep_Remove

argc = len(sys.argv)  # This just improves readability

if argc == 1:  # If there are no arguments, exit
    print("""No arguments were given.
For more information, use the \"-h\" argument.""")
    sys.exit(0)

# If there is only one argument, except for the -h one
elif argc == 2 and sys.argv[1] not in ["-h", "--help"]:
    print("""Missing argument: keyword
For more information, use the \"-h\" argument.""")
    sys.exit(0)

# Check in sys.argv for the arguments
for i in range(1, argc):
    # Help option
    if sys.argv[i] in ["-h", "--help"]:
        print("""
Remove the files inside a directory that have the specified
keyword in their name. Usage:

CLI> python3 RemoveFiles.py [arguments] [keyword] [directory]

Some arguments can also have sub-arguments. For example:

CLI> python3 RemoveFiles.py -e /my/dir -da hello /foo/bar
                            ^    ^
Could be interpreted as: extract here

If your directory has spaces, use quotes:

\"/dire c/tory w/ith s/pa ces/\"

Arguments/Options:

-h, --help       Get information about the program.

-e, --extract    Copy the given directory and its files
                 into a sub-directory and manipulate the
                 files inside of it.
                 (Optional): If an existing directory is
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
""")
        sys.exit(0)

    # Extract argument
    elif sys.argv[i] in ["-e", "--extract"]:
        extract = True
        # Check if the user also specified the directory
        # to extract the files
        if os.path.isdir(sys.argv[i + 1]):
            extract_dir = sys.argv[i + 1]
            i += 1  # So we don't check it again.

    # Keep argument
    elif sys.argv[i] in ["-k", "--keep"]:
        k_r = "k"

    # Verbose argument
    elif sys.argv[i] in ["-v", "--verbose"]:
        verbose = True

    # Ask argument
    elif sys.argv[i] in ["-da", "--dont-ask"]:
        ask = False

    # Recursive argument
    elif sys.argv[i] in ["-r", "--recursive"]:
        recursive = True

    # NoCaseSensitivity argument
    elif sys.argv[i] in ["-ncs", "--no-case-sens"]:
        ncs = True

    # Log argument
    elif sys.argv[i] in ["-l", "--log"]:
        log = True

    # Unregonized argument
    else:
        if i == (argc - 1):  # It could be the directory
            if not os.path.isdir(sys.argv[i]):
                print(f"The directory {sys.argv[i]} doesn't exist.")
                sys.exit(0)
        elif i == (argc - 2):  # It could be the keyword
            pass

        else:  # Invalid argument
            print(f"Invalid argument: {sys.argv[i]}")

# If extract_dir wasn't changed, convert it into a sub-directory
if extract_dir == "unknown":
    extract_dir = sys.argv[argc - 1] + "/Extracted"

# Call the main function with the collected arguments
# The last two arguments should be the keyword and the dir
main_func(sys.argv[(argc - 2)], sys.argv[(argc - 1)], extract,
          extract_dir, k_r, verbose, ask, recursive, ncs, log)

# End of boring code, thanks for reading!

