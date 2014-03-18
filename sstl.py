import sys
import re

def read_file(filename):
    try:
        f = open(filename, 'r')
        return f.read()
    except:
        print("Error, {} does not exist".format(filename))
        return None

def gen_template(text):
    result_str = ""
    index = 0
    state = "out-of-par"
    whitespace_char = re.compile(r'\s')
    newline_char = re.compile(r'\n')
    for c in text:
        if state == "out-of-par":
            if re.match(newline_char, c) is not None:
                result_str += "<br \>\n"
            elif re.match(whitespace_char, c) is None:
                result_str += "<p>" + c
                state = "in-par"
        elif state == "in-par":
            if re.match(newline_char, c) is not None:
                result_str += "</p>\n"
                state = "out-of-par"
            else:
                result_str += c
    return result_str
        
def main(args):
    if type(args) is str: # for debugging, to be removed
        args = ["sstl.py", args]
    if len(args) != 2:
        print("Error, wrong number of args.")
        exit(1)
    file_str = read_file(args[1])
    html = gen_template(file_str)
    print(html)

if __name__ == '__main__':
    main(sys.argv)
