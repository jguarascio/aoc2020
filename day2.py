from numpy import loadtxt

def main():
    day2 = loadtxt("day2.txt",delimiter=" ",dtype='str')

    valid = 0

    for entry in day2:
        min = int(entry[0].split('-')[0])
        max = int(entry[0].split('-')[1])
        char = entry[1][0]
        pwd = entry[2]
        #if pwd.count(char) >= min and pwd.count(char) <= max:
        if (pwd[min-1] == char) ^ (pwd[max-1] == char):
            valid +=1
    
    print(valid)

if __name__ == "__main__":
    main()        