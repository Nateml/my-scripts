#!/usr/bin/env python3

import sys
from os import scandir, getcwd

def main():

    if len(sys.argv) != 3:
        print("Invalid number of arguments.")
        print("USAGE:\t\tcount-words [dir] [file types]")
        print("E.g:\t\tcount-words . '.txt .md'")
        sys.exit()

    dir = sys.argv[1]
    if dir == ".":
        dir = getcwd()
    file_types = [x.split(".")[1] for x in sys.argv[2].split(" ")]

    total_word_count = 0

    for f in scandir(dir):
        if f.is_file():
            if f.path.split(".")[1] in file_types:
                with open(f.path, "r") as open_file:
                    word_count = len([word for line in [line.split(" ") for line in open_file.readlines()] for word in line])
                    total_word_count += word_count
                    open_file.close()

    print(f"{total_word_count} words")
    sys.exit()


if __name__ == "__main__":
    main()



