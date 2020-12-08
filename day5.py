def ticket_to_id(ticket):
    bin = ticket
    bin = bin.replace("F","0")
    bin = bin.replace("B","1")
    bin = bin.replace("L","0")
    bin = bin.replace("R","1")
    row = int(bin[0:7],2)
    seat = int(bin[-3:],2)
    return row*8 + seat

def main():
    text_file = open("day5.txt", "r")
    tickets = text_file.read().splitlines()
    text_file.close()

    # part 1
    min_id = 1023
    max_id = 0
    ticket_sum = 0
    for ticket in tickets:
        ticket_id = ticket_to_id(ticket)
        min_id = min(min_id, ticket_id)
        max_id = max(max_id, ticket_id)
        ticket_sum += ticket_id
    
    # part 2
    total = sum(range(min_id, max_id+1))
    print(f'{max_id=} {min_id=} {total=} {ticket_sum=}')
    print(total-ticket_sum)


if __name__ == "__main__":
    main()