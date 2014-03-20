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
    state = "out-of-block"
    token = ""
    whitespace_char = re.compile(r'\s')
    newline_char = re.compile(r'\n')
    for c in text:
        if state == "out-of-block":
            result_str += c
            if re.match(whitespace_char, c) is None:
                token += c
            elif re.match(newline_char, c):
                if token == "START_BODY":
                    state = "out-of-par"
                token = ""
        elif state == "out-of-par":
            if re.match(newline_char, c):
                result_str += "<br \>\n"
            elif re.match(whitespace_char, c) is None:
                result_str += "<p>" + c
                state = "in-par"
        elif state == "in-par":
            if re.match(newline_char, c):
                result_str += "</p>\n"
                state = "out-of-par"
            else:
                result_str += c
    # add closing </p> after input ends
    if state == "in-par":
        result_str += "</p>\n"
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
