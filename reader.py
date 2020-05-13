import re

from future.types import newint


def main(file_name, file_encoding):
    with open(file_name, encoding=file_encoding, errors='replace') as f:
        lines = f.readlines()
        f.close()
        clean(lines)

def match(a):
    return not bool(re.compile(r'[A-Za-z0-9.]').search)


def clean(lines):
    newlines = []
    i = 0
    for a in lines:
        if str(i) in a and "-->" not in a:
            i += 1
        elif "-->" not in a:
            if len(a) > 1:
                newlines.append(re.sub("<\/?i>", "", a))

    for lines in newlines:
        print(lines)


main("the-avengers-en1.srt", 'utf-8')
