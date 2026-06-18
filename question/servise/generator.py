import random

def creat_question(patterns,difficulty):
    pattern = random.choice(patterns)
    constants = []

    adding_constants(pattern.ignorance,difficulty,constants)

    return {
        "value" :build_question(pattern.value,constants),
        "pattern": pattern.value,
        "constants": constants
        }
    #5+7+8-10*5
    #?+?+?-?*?

def adding_constants(ignorance,difficulty,constants):
    number = 0

    for i in range(ignorance):
        if(difficulty == 0):
            number = random.randint(1,10)
        elif(difficulty == 1):
             number = random.randint(1,100)
        else:
            number = random.randint(1,300)

        if(number == 0):
            number=number+1

        constants.append(number)

def build_question(value,constants):
    index = 0
    question = ""
    for char in value:
        if(char != '?'):
            question = question + char
        else:
            question = question + str(constants[index])
            index = index + 1

    return question