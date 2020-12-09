import string

def part1():
    text_file = open("day6.txt",'r')

    answer_list = []
    answer_group = ""
    for line in text_file:
        #print(line)
        if line == "\n":
            # Add line to array
            answer_list.append(answer_group.replace("\n",""))
            answer_group = ""
        else:
            answer_group += line
    
    # Add last answer group
    answer_list.append(answer_group.replace("\n",""))

    text_file.close()

    total = 0
    for group in answer_list:
        total += len(set(group))

    print(total)
    return

def part2():
    text_file = open("day6.txt",'r')

    group_list = []
    group = []
    for line in text_file:
        #print(line)
        if line == "\n":
            # Add line to array
            group_list.append(group)
            group = []
        else:
            group.append(line.strip("\n"))
    
    # Add last answer group
    group_list.append(group)

    text_file.close()

    total = 0
    for group in group_list:
        #print(group)
        # initialize the result with all lower case letters
        result = string.ascii_lowercase
        for person in group:
            result = set(person).intersection(result) 
        #print(result)
        total += len(result)

    print(total)        
    return

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()