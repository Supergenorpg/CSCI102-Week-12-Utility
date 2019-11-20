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

def FindWordCount(user_list, user_string):
    count = 0
    for i in user_list:
        split = i.split()
        if user_string in split:
            count += 1
    return count

def ScoreFinder(players, scores, name):
    player_exists = False
    for i in range(len(players)):
        if name.lower() == players[i].lower():
            player_exists = True
            index = i
    if player_exists:
        PrintOutput(str(players[index]) + " got a score of " + str(scores[index]))
    elif not player_exists :
        PrintOutput("player not found")
