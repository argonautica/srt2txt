import re

from future.types import newint


def main(file_name, file_encoding):
    with open(file_name, encoding=file_encoding, errors='replace') as f:
        lines = f.readlines()
        f.close()
        out = clean(lines)
        file_name = "texts/" + file_name[5:-4] + ".txt"
        f = open(file_name, "w+")
        for line in out:
            f.write(line)
        f.close()




def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]


def clean(lines):
    newlines = []
    i = 0
    for a in lines:
        if str(i) in a and "-->" not in a:
            i += 1
        elif "-->" not in a:
            if len(a) > 1:
                newlines.append(re.sub("<\/?i>", "", a))
    return newlines



main("subs/the-avengers-en1.srt", 'utf-8')
