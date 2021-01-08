rules = {}
messages = []

def setup():
    global rules, messages
    text_file = open("day19.txt", "r")
    sections = text_file.read().split('\n\n')
    text_file.close()
    
    rules = {int(item.split(': ')[0]) : item.split(': ')[1].strip('"').split(' | ') for item in sections[0].split('\n')}
    messages = sections[1].split('\n')

    return rules, messages


def getTree(value_list):
    result = []
    for item in value_list:
        text = []
        if item in ('a','b'): return item
        #print(item)
        for value in item.split(' '):
            text.append(getTree(rules[int(value)]))
        result.append(''.join(text))
        print(f'{item=} {text=} {result=}')
    return ''.join(result)


def part1():
    rules, messages = setup()

    print(rules)
    print(messages)

    # Create list of valid messages
    messages = []
    for key, rule in rules.items():
        tree = getTree(rule)
        print(f'{key=} {tree=}')
        input()

    return

def part2():

    return

def main():
    setup()
    part1()
    part2()

if __name__ == "__main__":
    main()