def setup():
    text_file = open("day14.txt", "r")
    lines = text_file.read().splitlines()
    text_file.close()

    return lines

def part1():
    code = setup()
    mask = ''
    mem = {}
    for i in code:
        op = i.split(' = ')[0]
        value = i.split(' = ')[1]
        #print(f'{op=} {value=}')
        if op == 'mask':
            mask = value
            and_mask = int(value.replace('1','0').replace('X','1'),2)
            or_mask = int(value.replace('X','0'),2)
            #print(f'{and_mask=} {or_mask=}')
        else:
            addr = int(op[4:-1])
            mem[addr] = (int(value) & and_mask) | or_mask
    
    print(sum(mem.values()))
    return

def part2():
    code = setup()
    mask = ''
    mem = {}
    for i in code:
        op = i.split(' = ')[0]
        value = i.split(' = ')[1]
        if op == 'mask':
            mask = value
            and_mask = int(value.replace('0','1').replace('X','0'),2)
            floats = [i for i in range(len(value)) if value[i]=='X']
            all_masks = []
            for x in range(pow(2,int(len(floats)))):
                new_mask = list(value)
                binary = format(x,"0" + str(len(floats)) + "b")
                for y in range(len(floats)):
                    new_mask[floats[y]] = binary[y]
                all_masks.append("".join(new_mask))
        else:
            addr = int(op[4:-1])

            for sub_mask in all_masks:
                mem[(addr & and_mask) | int(sub_mask,2)] = int(value)
            
    print(sum(mem.values()))

    return

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()