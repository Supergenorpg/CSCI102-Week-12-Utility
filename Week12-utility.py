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
