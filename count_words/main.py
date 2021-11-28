import argparse
import os
import string
import re
from collections import Counter

def main(args):
    file_path = os.path.join(os.getcwd(), args.filename)
    with open(file_path, 'r') as file:
        content = file.read()
        excluded_punctuation = []
        for i in content.split():
            word = re.sub(r'[^\w\d\s]+', '', i)
            if word:
                excluded_punctuation.append(word)
        print(excluded_punctuation)
        counted = dict(Counter(excluded_punctuation))
        print(counted)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process N primes')
    parser.add_argument("-f", "--f", dest="filename", type=str,
                        help="File name that used to count words", metavar="filename", required=True)
    args = parser.parse_args()
    main(args)
