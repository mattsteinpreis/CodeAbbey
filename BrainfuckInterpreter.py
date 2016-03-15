__author__ = 'matt'

ARRAY_SIZE = 128


def find_brackets(command_str):
    bracket_dict = {'l': {}, 'r': {}}
    lefts = []
    for i, ch in enumerate(command_str):
        if ch == '[':
            lefts.append(i)
        elif ch == ']':
            left = lefts.pop()
            right = i
            bracket_dict['r'][right] = left
            bracket_dict['l'][left] = right
    return bracket_dict


def run_commands(command_str):
    brackets = find_brackets(command_str)
    memory = [0]*ARRAY_SIZE
    memory_pos = 0
    command_pos = 0
    while command_pos < len(commands):
        c = commands[command_pos]
        if c == ';':
            memory[memory_pos] = numbers.pop(0)
        elif c == ':':
            print memory[memory_pos],
        elif c == ">":
            memory_pos += 1
        elif c == "<":
            memory_pos -= 1
        elif c == "+":
            memory[memory_pos] += 1
        elif c == '-':
            memory[memory_pos] -= 1
        elif c == '[':
            if not memory[memory_pos]:
                command_pos = brackets['l'][command_pos]
        else:
            command_pos = brackets['r'][command_pos]
            continue
        command_pos += 1


commands = raw_input()
numbers = [int(j) for j in raw_input().split()]
run_commands(commands)

# test example
#commands = ';>;<[->+<]:>:'
#numbers = [3, 5]
#run_commands(commands)





