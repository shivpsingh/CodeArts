#!/usr/bin/env python3.8
"""
    Author: Shiv Pratap Singh
"""

import sys


def main(file_name):

    parsed_dict = dict()

    with open(file_name, 'r') as fh:
        lines_w_nl = fh.readlines()

        for word_w_nl in lines_w_nl:
            word = word_w_nl.strip('\n')

            if word in parsed_dict:
                parsed_dict[word] += 1
            else:
                parsed_dict[word] = 1

    for word in parsed_dict.keys():
        print(word)


if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except IndexError:
        print('Usage: UniqKeyFinder.py <file_name>')
    else:
        main(file_name)
