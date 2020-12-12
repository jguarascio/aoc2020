lines = []

def setup():
    global lines
    text_file = open("day12.txt", "r")
    lines = text_file.read().splitlines()
    text_file.close()


def part1():
    eastwest = 0
    northsouth = 0
    facing = 90

    for dir in lines:
        direction = dir[0]
        amount = int(dir[1:])
        if direction == 'N': northsouth += amount
        if direction == 'S': northsouth -= amount
        if direction == 'E': eastwest += amount
        if direction == 'W': eastwest -= amount
        if direction == 'R': facing += amount
        if direction == 'L': facing -= amount
        if facing >= 360: facing -= 360
        if facing < 0: facing += 360
        if direction == 'F':
            if facing==0: northsouth += amount
            if facing==90: eastwest += amount
            if facing==180: northsouth -= amount
            if facing==270: eastwest -= amount
        

    dist = abs(eastwest) + abs(northsouth)

    print(dist)

    return

def part2():
    eastwest_travel = 0
    northsouth_travel = 0
    eastwest = 10
    northsouth = 1

    for dir in lines:
        direction = dir[0]
        amount = int(dir[1:])
        if direction == 'N': northsouth += amount
        if direction == 'S': northsouth -= amount
        if direction == 'E': eastwest += amount
        if direction == 'W': eastwest -= amount
        if direction == 'R' and amount == 90: 
            eastwest, northsouth = northsouth, -eastwest
        if (direction == 'L' and amount == 90) or (direction == 'R' and amount == 270): 
            eastwest, northsouth = -northsouth, eastwest
        if direction in ('R','L') and amount == 180: 
            northsouth = -northsouth
            eastwest = -eastwest
        if direction == 'F':
            northsouth_travel += amount * northsouth
            eastwest_travel += amount * eastwest
        #print(f'{dir=} {northsouth=} {eastwest=}')
    
    dist = abs(eastwest_travel) + abs(northsouth_travel)
    print(dist)

    return

def main():
    setup()
    part1()
    part2()

if __name__ == "__main__":
    main()