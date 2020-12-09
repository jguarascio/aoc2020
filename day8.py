import string

input_list = []

def setup():
    text_file = open("day8.txt", "r")
    lines = text_file.read().splitlines()
    text_file.close()
    
    for line in lines:
        input_list.append(line.split(" "))


def part1(program):

    i = 0
    accumulator = 0
    visited = []

    while i not in visited:
        visited.append(i)
        opcode = program[i][0]
        arg = int(program[i][1])
        
        if opcode == 'acc':
            accumulator += arg
            i += 1
        elif opcode == 'jmp':
            i += arg
        elif opcode == 'nop':
            i += 1
        if i > len(program)-1:
            print("Program completed normally")
            print(f'{accumulator=}')
            return True

    print("Program failed to complete")
    print(f'{accumulator=}')

    return False

def part2():
    
    j = 0
    program = input_list.copy()
    while True:
        if program[j][0] == 'jmp':
            program[j][0] = 'nop'
            if part1(program): 
                break
            else: 
                program[j][0] = 'jmp'
        elif program[j][0] == 'nop':
            program[j][0] = 'jmp'
            if part1(program): 
                break
            else: 
                program[j][0] = 'nop'
        j += 1

    return

def main():
    setup()
    part1(input_list)
    part2()

if __name__ == "__main__":
    main()