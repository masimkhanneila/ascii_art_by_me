import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--output", help="Output file")
parser.add_argument("--color", choices=["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white", "orange", "pink", "purple", "light_blue"], help="Color of the ASCII art")
parser.add_argument("letters", nargs="?", help="Letters to convert to color")
parser.add_argument("--align", choices=["left", "center", "right"], default="left", help="Alignment of the ASCII art")
parser.add_argument("--reverse", action="store_true", help="Reverse the order of the ASCII art")
parser.add_argument("text", help="Text to convert to ASCII art")
parser.add_argument("font",nargs="?",choices=["standard", "shadow", "thinkertoy"],default="standard")
args = parser.parse_args()

colors = {
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "orange": "\033[38;5;208m",
    "pink": "\033[38;5;13m",
    "purple": "\033[38;5;93m",
    "light_blue": "\033[38;5;117m",
    "reset": "\033[0m"
}

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


to_print = args.text
font = args.font
for_output = args.output
color = args.color
letters = args.letters
align = args.align
reverse = args.reverse

print(for_output, color, letters, align, reverse, to_print, font)

file = which_font(font)

if for_output==None:
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



    









