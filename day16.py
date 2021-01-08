rules = {}
my_ticket = ''
nearby_tickets = []

def setup():
    global rules, my_ticket, nearby_tickets

    text_file = open("day16.txt",'r')

    # Read requirements
    line = 'x'
    while line:
        line = text_file.readline().replace('\n','')
        if line == '': break
        rule = line.split(': ')[0]
        values = line.split(': ')[1].split(' or ')
        rules[rule] = values

    # Get my ticket
    while line !='your ticket:':
        line = text_file.readline().replace('\n','')      

    my_ticket = [int(i) for i in text_file.readline().replace('\n','').split(',')]

    # Get nearby tickets
    while line !='nearby tickets:':
        line = text_file.readline().replace('\n','')
 
    while line:
        line = text_file.readline().replace('\n','')
        if line: 
            arr = [int(i) for i in line.split(',')]
            nearby_tickets.append(arr)

    text_file.close()

    return


def part1():
    error_sum = 0
    all_ranges = [[int(r.split('-')[0]),int(r.split('-')[1])] for val in rules.values() for r in val]
    for ticket in nearby_tickets:
        valid = True
        for item in ticket:
            if not any(r for r in all_ranges if r[0] <= item <= r[1]): 
                error_sum += item
                valid = False

    print(error_sum)

    return

def part2():
    # get list of valid tickets
    valid_tickets = []
    all_ranges = [[int(r.split('-')[0]),int(r.split('-')[1])] for val in rules.values() for r in val]
    for ticket in nearby_tickets:
        valid = True
        for item in ticket:
            if not any(r for r in all_ranges if r[0] <= item <= r[1]): 
                valid = False
        if valid:
            valid_tickets.append(ticket)

    # Now find the rule that is valid for every item in every ticket
    rule_position = {}
    for i in range(len(valid_tickets[0])):
        possible_rules = [key for key in rules]
        # check each ticket at position i
        for item in valid_tickets:
            value = item[i]
            for rule_name, rule in rules.items():
                lo0 = int(rule[0].split('-')[0])
                hi0 = int(rule[0].split('-')[1])
                lo1 = int(rule[1].split('-')[0])
                hi1 = int(rule[1].split('-')[1])        
                if not (lo0 <= value <= hi0 or lo1 <= value <= hi1):  
                    possible_rules.remove(rule_name)
        rule_position[i] = possible_rules
    
    for i in range(len(valid_tickets[0])):
        for key in rule_position:
            if len(rule_position[key]) == 1:
                #print('remove ' + str(rule_position[key]))
                for other_key in rule_position:
                    if key != other_key and rule_position[key][0] in rule_position[other_key]:
                        rule_position[other_key].remove(rule_position[key][0])
        
    #print(my_ticket.split(','))
    product = 1
    for position in rule_position:
        print(f'{position=} {rule_position[position]=}')
        if rule_position[position][0][0:3] == 'dep':
            product = product * my_ticket[position]

    print(product)
    return

def main():
    setup()
    part1()
    part2()

if __name__ == "__main__":
    main()