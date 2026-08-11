import sys


def read_make_dict(file):
    with open(file, "r") as f:
        f.readline()
        f.readline()
        value = [ 
            f.readline().rstrip("\n")
            for i in range(8) 
            ]
        d = {
            " " : value
        }
 
        for k in range(33, 127):
            value = [ 
                f.readline().rstrip("\n")
                for i in range(8) 
                ]
            d[chr(k)] = value
            f.readline()
        k += 1

    return d
standarD= read_make_dict("standard.txt")
shadoW= read_make_dict("shadow.txt")
thinkertoY= read_make_dict("thinkertoy.txt")

def print_ascii_art(to_print,file):
    result=""
    if len(to_print) >= 14:
        print("Too many characters. Please enter less than 14 characters.")
        to_print = "Too long"
    

    for i in range(8):
        line = ""
        for char in to_print:
            if char in file:
                line += file[char][i] + " "
        result += line + "\n"
    return result

def which_font(f= "standard"):
    if f.lower() == "shadow" :
        return shadoW
    elif f.lower() == "thinkertoy":
        return thinkertoY
    else :
        return standarD


to_print = sys.argv[1]
font = sys.argv[-1]
for_output = ""
if sys.argv[1].startswith("--output="):
    for_output = sys.argv[1].split("=")[1]
    to_print = sys.argv[2]

file = which_font(font)

if for_output=="":
    if "\\n" in to_print:
        words = to_print.split("\\n")
        for word in words:
            to_print = word
            print(print_ascii_art(to_print,file))
            print("\n")
    else:
        print(print_ascii_art(to_print,file))
else :
    with open(for_output,"w") as f:
        f.write(print_ascii_art(to_print,file))
    print("File " + for_output + " was created")



    









