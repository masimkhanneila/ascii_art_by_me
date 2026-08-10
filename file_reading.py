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
standard= read_make_dict("standard.txt")
shadow= read_make_dict("shadow.txt")
thinkertoy= read_make_dict("thinkertoy.txt")
"""
for key, value in thinkertoy.items():
    print(f"Character: {repr(key)}")
    for line in value:
        print(line)
    print("-" * 20)
"""

def print_ascii_art():
    
    for i in range(8):
        line = ""
        for char in to_print:
            if char in standard:
                line += standard[char][i] + " "
        print(line)
print("Enter exit to quit the program.")
while True:
    to_print = input("Please enter what you want to print: ")

    if len(to_print) >= 14:
        print("Too many characters. Please enter less than 14 characters.")
        to_print = "Too long" 
    print_ascii_art()
    if to_print.lower() == "exit":
        break


