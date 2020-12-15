def part1():

    start = [5,1,9,18,13,8,0]
    n = len(start)
    
    spoken = start[:]

    for turn in range(n, 2020):
        diff = 0
        last_spoken = spoken[len(spoken)-1]
        if last_spoken in spoken[0:-1]:
            last_time = len(spoken)-2
            while spoken[last_time] != last_spoken: last_time -=1
            diff = turn - 1 - last_time
        spoken.append(diff)

    print(spoken)
    return

def part2():
    input_list = [5,1,9,18,13,8,0]
    n = len(input_list)
    last_number = input_list[n-1]
    
    last_spoken = {}
    for i in range(n):
        last_spoken[input_list[i]] = i + 1
    
    turn = n+1
    while turn <= 30000000:
        #print(f'{turn=} {last_number=} {last_spoken=}', end=' ')
        if last_number not in last_spoken:
            last_spoken[last_number] = turn - 1
            spoken = 0
        elif last_spoken[last_number] == turn - 1:
            spoken = 0
        else:
            spoken = turn - 1 - last_spoken[last_number]
            last_spoken[last_number] = turn - 1        
        #print(f'{spoken=}')
        last_number = spoken
        turn +=1

    print(last_number)
    
    return

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()