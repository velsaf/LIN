import random

variables = {}
path = 'output: '

def get_input():
    command = str(input('>>>'))
    if 'print' in command:
        output = command[6:]
        print(path+output)

    elif 'calc' in command:
        output = eval(command[5:])
        print(path+str(output))
