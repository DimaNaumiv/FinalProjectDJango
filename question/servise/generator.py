import random

def creat_question(patterns,min_value,max_value):
    pattern = random.choice(patterns)
    constants = []

    adding_constants(pattern.ignorance,min_value,max_value,constants)

    return {
        "value" :build_question(pattern.value,constants),
        "pattern": pattern.value,
        "constants": constants
        }
    #5+7+8-10*5
    #?+?+?-?*?

def adding_constants(ignorance,min_value,max_value,constants):
    number = 0

    for i in range(ignorance):
        number = random.randint(min_value,max_value)

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