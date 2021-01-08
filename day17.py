def part1():
    text_file = open("day17.txt", "r")
    lines = text_file.read().splitlines()
    text_file.close()

    x = 0
    z = 0
    active_points = set()
    for line in lines:
        for y in [pos for pos, char in enumerate(line) if char == '#']:
            active_points.add((x,y,z))
        x +=1
    #print(active_points)

    # Build offset list
    offsets = [(i,j,k) for i in range(-1,2) for j in range(-1,2) for k in range(-1,2)]
    offsets.remove((0,0,0))
    #print(offsets)

    for i in range(6):        
        print(active_points)
        # Check for active neighbors
        new_active_points = set()
        inactive_points = set()
        for point in active_points:
            active_neighbors = 0
            for dir in offsets:
                nx = point[0] + dir[0]
                ny = point[1] + dir[1]
                nz = point[2] + dir[2]
                if (nx, ny, nz) in active_points: 
                    active_neighbors += 1
                else:
                    inactive_points.add((nx, ny, nz))
            if active_neighbors in (2,3):
                new_active_points.add(point)
                #print(f'Keep: {point=} {active_neighbors=}')

        # check for inactive points
        for point in inactive_points:
            active_neighbors = 0
            for dir in offsets:
                nx = point[0] + dir[0]
                ny = point[1] + dir[1]
                nz = point[2] + dir[2]
                if (nx, ny, nz) in active_points: 
                    active_neighbors += 1
            if active_neighbors == 3:
                new_active_points.add(point)
                #print(f'Add: {point=} {active_neighbors=}')

        active_points = new_active_points.copy()

    print(len(active_points))
    return

def part2():
    text_file = open("day17.txt", "r")
    lines = text_file.read().splitlines()
    text_file.close()

    x = 0
    z = 0
    w = 0
    active_points = set()
    for line in lines:
        for y in [pos for pos, char in enumerate(line) if char == '#']:
            active_points.add((x,y,z,w))
        x +=1

    #print(active_points)

    # Build offset list
    offsets = [(i,j,k,l) for i in range(-1,2) for j in range(-1,2) for k in range(-1,2) for l in range(-1,2)]
    offsets.remove((0,0,0,0))
    #print(offsets)

    for i in range(6):        
        print(active_points)
        # Check for active neighbors
        new_active_points = set()
        inactive_points = set()
        for point in active_points:
            active_neighbors = 0
            for dir in offsets:
                nx = point[0] + dir[0]
                ny = point[1] + dir[1]
                nz = point[2] + dir[2]
                nw = point[3] + dir[3]
                if (nx, ny, nz, nw) in active_points: 
                    active_neighbors += 1
                else:
                    inactive_points.add((nx, ny, nz, nw))
            if active_neighbors in (2,3):
                new_active_points.add(point)
                #print(f'Keep: {point=} {active_neighbors=}')

        # check for inactive points
        for point in inactive_points:
            active_neighbors = 0
            for dir in offsets:
                nx = point[0] + dir[0]
                ny = point[1] + dir[1]
                nz = point[2] + dir[2]
                nw = point[3] + dir[3]
                if (nx, ny, nz, nw) in active_points: 
                    active_neighbors += 1
            if active_neighbors == 3:
                new_active_points.add(point)
                #print(f'Add: {point=} {active_neighbors=}')

        active_points = new_active_points.copy()

    print(len(active_points))
    return

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()