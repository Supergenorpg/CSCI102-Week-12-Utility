# https://github.com/Supergenorpg/CSCI102-Week-12-Utility.git
# Seth Deibert
# CSCI 102 - Section E
# Week 12 - Part B

def PrintOutput(input_string):
    print("OUTPUT", input_string)

def LoadFile(file_name):
    f = open(file_name, 'r')
    content = f.read().splitlines()
    f.close()
    return content

def UpdateString(string1, string2, index):
    new = ''
    for i in range(len(string1)):
        if i == index:
            new += string2
        else:
            new += string1[i]
    PrintOutput(new)
