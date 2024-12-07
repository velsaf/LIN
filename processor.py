file_count = open('lin.txt')
codelen = len(file_count.readlines())
file_count.close()
file_code = open('lin.txt')

import console
from console import get_input
import random
variables = {}
path = 'output:'


def runString():
    command = file_code.readline()
    if 'prompt' in command:
        index = 7
        if 'int' in command:
            index2 = command.find('int')
            var_name = command[index:index2]
            var_value = int((input('_>')))
            variables[var_name[:-1]] = var_value
            output = variables
            print(output)

        elif 'str' in command:
            index2 = command.find('str')
            var_name = command[index:index2]
            var_value = str((input('_>')))
            variables[var_name[:-1]] = var_value
            output = variables
            print(output)

    elif 'var' in command:
        if 'set' in command:
            index = 8
            index2 = command.find(':')-1
            if 'int' in command:
                index3 = command.find('int')
                var_name = command[index:index2]
                var_value = command[index2+2:index3-1]
                variables[var_name] = int(var_value)
                output = 'Variable succefly updated!'
                print(path+f'{output}')

            elif 'str' in command:
                index3 = command.find('str')
                var_name = command[index:index2]
                var_value = command[index2+2:index3-1]
                variables[var_name] = str(var_value)
                output = 'Variable succefly updated!'
                print(path+f'{output}')

        elif 'show' in command:
            index = 9
            var_name = command[index:]
            output = variables.get(var_name)
            print(path+str(f'{output}'))

        #elif 'type' in command:
        #    index = 9
        #    var_name = command[index:]
        #    var_value = variables.get(str(var_name))
        #    output = type(var_value)
        #    print(path+f'{output}')

    elif 'random' in command:
        if 'input' in command:
            index = 7
            index2 = command.find('input')
            var_name = command[index:index2]
            min = int(input('min>'))
            max = int(input('max>'))
            var_name = var_name[:-1]
            randomint = random.randint(min, max)
            variables[var_name] = randomint
            output = f'{randomint} was write to {var_name}'
            print(path + f'{output, var_name}')

        else:
            index = 8
            index2 = command.find('/')
            index3 = command.find(':')
            var_name = command[index - 1:index2]
            min = command[index2 + 1:index3]
            max = command[index3 + 1:]
            var_name = var_name[:-1]
            randomint = random.randint(int(min), int(max))
            variables[var_name] = randomint
            output = f'{randomint} was write to {var_name}'
            print(path + f'{output}')

    elif 'console' in command:
        get_input()


for w in range(codelen):
    runString()
