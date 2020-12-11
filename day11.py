import copy

dirs = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1]
]

def setup():
    text_file = open("day11.txt", "r")
    lines = text_file.read().splitlines()
    text_file.close()

    seats = []
    for line in lines:
        row = list(line)
        seats.append(row)
        #print(row)

    return seats


def valid(seats, row, col):
    return (0 <= row < len(seats)) and (0 <= col < len(seats[0]))

def count_occupied(seats):
    occupied = 0
    for row in seats:
        occupied +=row.count('#')
    return occupied

def part1(seats):
    change = True
    
    while change:
        change = False
        new_seats = copy.deepcopy(seats)
        for i in range(len(seats)):
            for j in range(len(seats[i])):
                occupied = 0
                
                # Look in every direction
                for dir in dirs:
                    nr = i + dir[0]
                    nc = j + dir[1]
                    if valid(seats, nr,nc) and seats[nr][nc]=='#': occupied +=1

                if seats[i][j] == 'L' and occupied == 0: 
                    new_seats[i][j] = '#'
                    change = True
                elif seats[i][j] == '#' and occupied >= 4: 
                    new_seats[i][j] = 'L'
                    change = True

        seats = new_seats
    
    print(count_occupied(seats))

def part2(seats):
    change = True
    
    while change:
        change = False
        new_seats = copy.deepcopy(seats)
        for i in range(len(seats)):
            for j in range(len(seats[i])):
                occupied = 0

                # Look in every direction
                for dir in dirs:
                    nr = i + dir[0]
                    nc = j + dir[1]
                    # Keep looking in that direction
                    while valid(seats, nr,nc) and seats[nr][nc]=='.': 
                        nr += dir[0]
                        nc += dir[1]
                    if valid(seats, nr,nc) and seats[nr][nc]=='#': 
                        occupied +=1

                if seats[i][j] == 'L' and occupied == 0: 
                    new_seats[i][j] = '#'
                    change = True
                elif seats[i][j] == '#' and occupied >= 5: 
                    new_seats[i][j] = 'L'
                    change = True

        seats = new_seats
    
    print(count_occupied(seats))
    return

def main():
    seats = setup()
    part1(seats)
    part2(seats)

if __name__ == "__main__":
    main()