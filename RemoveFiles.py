# A very simple script to remove files if they
# have the specified keyword, coded by Suaj

import shutil, sys, os

# Main function

def main_func(keyword, directory, extract, k_r, verbose, ask):
    if extract:  # Create the sub-directory
        try:
            shutil.copytree(directory, f"{directory}/Extracted")
            if verbose:
                print("Creating sub-directory \"Extracted\"...")

        # The program could just try a different name, but that
        # name could also be used, and the next one too...

        # TO-DO: Ask for the user if the program should copy
        # the files to that directory or abort the operation

        except FileExistsError:
            print("The sub-directory \"Extracted\" already \
exists. Aborting...")
            sys.exit(0)
        else:  # Change the directory to the sub-directory
            directory = directory + "/Extracted"

    if verbose:
        print(f"Removing all files in {directory}...")

    conf = True  # Default value for the "ask" block

    for i in os.listdir(directory):
        if (keyword not in i and k_r == "k") \
        or (keyword in i and k_r == "r"):
            # Only if the value is an existing file
            if os.path.isfile(f"{directory}/{i}"):
                if ask:  # Ask for confirmation
                    conf = input(f"Remove {i}? [Y/n] ")
                    if conf.lower() in ["yes", "y"]:
                        conf = True
                    elif conf.lower() in ["no", "n"]:
                        conf = False
                        if verbose:
                            print("{i} will not be removed.")
                    # Y is the default option
                    else:
                        conf = True
                if conf:
                    if verbose:  # Verbose argument
                        print(f"Removing {i}... ", end='')
                    try:
                        os.remove(f"{directory}/{i}")
                    # This is to avoid the program collapsing
                    # if a single file raises an exception
                    except Exception as id:
                        print(f"""
An exception occurred.
Exception details: {id}
""")
                    else:
                        print("Done.")
            # TO-DO: Allow the deletion of files recursively
            elif os.path.isdir(f"{directory}/{i}"):
                if verbose:
                    print(f"{i} is a directory. Skipping...")
            else:  # It probably doesn't exist
                if verbose:
                    print(f"ERROR: {i} doesn't exist.")
    if verbose:
        print("Done.")

# Default option values, they are handled like this instead
# of putting them directly in the function in case the user
# changes them

extract = False
verbose = False
ask = False
k_r = "r"

# C-style loop because I forgot about the range() function lol

# If there are no arguments, exit
if len(sys.argv) == 1:
    print("""No arguments were given.
For more information, use the \"-h\" argument.""")
    sys.exit(0)

i = 1
while i < len(sys.argv):
    # Help option
    if sys.argv[i] in ["-h", "--help"]:
        print("""
Remove the files inside of a directory that have the
specified keyword in their names.
Usage:

Terminal$ python3 RemoveFiles.py [arguments] [keyword] [directory]

If your directory has spaces or special characters in its name,
use quotes:

\"directory with spaces\"

Arguments/Options:

-h, --help     Get information about the program.
-e, --extract  Copy the given directory and its files
               into a subdirectory and manipulate the
               files inside of it.
-k, --keep     Instead of removing the files, keep them
               and remove the ones that don't have the
               keyword in their names.
-r, --remove   Default value, the opposite of --keep.
-a, --ask      Ask before deleting a file.
-v, --verbose  Print the action being done.
        """)
        sys.exit(0)

    # Extract argument
    elif sys.argv[i] in ["-e", "--extract"]:
        extract = True

    # Keep argument
    elif sys.argv[i] in ["-k", "--keep"]:
        k_r = "k"

    # Remove argument (Default)
    elif sys.argv[i] in ["-r", "--remove"]:
        pass

    elif sys.argv[i] in ["-a", "--ask"]:
        ask = True

    # Verbose argument
    elif sys.argv[i] in ["-v", "--verbose"]:
        verbose = True

    # Invalid argument
    else:
        # It could be the directory
        if i == (len(sys.argv)-1):
            if not os.path.isdir(sys.argv[i]):
                print(f"The directory {sys.argv[i]} doesn't exist.")
                sys.exit(0)
        # Or it could be the keyword
        elif i == (len(sys.argv)-2):
            pass
        else:
            print(f"Invalid argument: \"{sys.argv[i]}\"")

    i += 1  # This is the increment value of the loop

# The last two arguments should be the keyword and the dir
main_func(sys.argv[(len(sys.argv)-2)], sys.argv[(len(sys.argv)-1)],
          extract, k_r, verbose, ask)

# Did you really read all of this code?...
# Thank you!

