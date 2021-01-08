import re

def setup():
    text_file = open("day18.txt", "r")
    lines = text_file.read().splitlines()
    text_file.close()

    return lines

def find_matching_parens(text):
    istart = []
    d = {}
    for i, c in enumerate(text):
        if c == '(': istart.append(i)
        if c == ')': d[istart.pop()] = i

    return d

def evaluate(exp):
    sum = 0
    action = '+'
    i = 0
    parens = find_matching_parens(exp)
    while i in range(len(exp)):
        c = exp[i]
       # print(f'{i=} {c=}')
        if c == '(': 
            num = evaluate(exp[i+1:parens[i]])
            i = parens[i]
            if action == '+':
                sum += num
            else:
                sum *= num
            #return sum
        elif c == ')': 
            return sum
        elif c == '+': 
            action = '+'
        elif c == '*': 
            action = '*'
        elif c != ' ':
            num = int(c)
            if action == '+':
                sum += num
            else:
                sum *= num
        i += 1
    
    return sum


def part1():
    problems = setup()

    total = 0
    for exp in problems:
        answer = evaluate(exp)
        total += answer
        print(f'{exp=} {answer=}')

    print(total)
    return




def part2():
    class num(int):
        def __sub__(self, b):
            return num(int(self) * int(b))
        def __mul__(self,b):
            return num(int(self) + int(b))

    problems = setup()

    total = 0
    for exp in problems:
        exp = exp.replace('*','-')
        exp = exp.replace('+','*')
        exp = re.sub('(\d+)',r'num(\1)', exp)
        print(exp)
        total += eval(exp)

    print(total)
    return

def main():
    #part1()
    part2()

if __name__ == "__main__":
    main()