def setup():
    text_file = open("day13.txt", "r")
    lines = text_file.read().splitlines()
    text_file.close()
    return lines

def part1():
    lines = setup()

    time = int(lines[0])
    buses = lines[1].split(',')

    bus_number = 0
    depart = 999
    for bus in buses:
        if bus != 'x':
            # Take the ceiling of the division multiplied by the bus number to 
            new_depart = -(-time // int(bus))*int(bus)
            if new_depart - time < depart:
                depart = new_depart - time
                bus_number = int(bus)

    print(bus_number*depart)

    return

def part2():
    lines = setup()
    buses = lines[1].split(',')

    min_value = 0
    product = 1

    for i in range(len(buses)):
        if buses[i] != 'x':
            time = i
            bus = int(buses[i])
            
            # Keep adding until (t + time) mod bus == 0
            while (min_value + time) % bus != 0:
                min_value += product
            product *= bus
            print(f'{i=} {bus=} {min_value=} {product=}')

    return

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()