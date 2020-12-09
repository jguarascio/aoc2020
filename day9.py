from numpy import loadtxt

lines = []

def setup():
    global lines
    lines = loadtxt("day9.txt")


def part1():
    for i in range(25,len(lines)):
        target = int(lines[i])
        picks = {}
        valid = False
        for j in range(i-25,i):
            if target - lines[j] in picks:
                valid = True
                break
            else:
                picks[lines[j]] = j

        if not valid:
            print(f'{target=}')
            break
       
    return target

def part2(target):
    # https://www.geeksforgeeks.org/find-subarray-with-given-sum/
    # Initialize curr_sum as 
    # value of first element 
    # and starting point as 0  
    n = len(lines)
    curr_sum = lines[0] 
    start = 0
  
    # Add elements one by  
    # one to curr_sum and  
    # if the curr_sum exceeds  
    # the sum, then remove  
    # starting element  
    i = 1
    while i <= n: 
          
        # If curr_sum exceeds 
        # the sum, then remove 
        # the starting elements 
        while curr_sum > target and start < i-1: 
          
            curr_sum = curr_sum - lines[start] 
            start += 1
              
        # If curr_sum becomes 
        # equal to sum, then 
        # return true 
        if curr_sum == target: 
            print ("Sum found between indexes") 
            print ("% d and % d"%(start, i-1)) 
            print ( min(lines[start:i-1]) + max(lines[start:i-1]) )
            return 1
  
        # Add this element  
        # to curr_sum 
        if i < n: 
            curr_sum = curr_sum + lines[i] 
        i += 1
  
    # If we reach here,  
    # then no subarray 
    print ("No subarray found") 
    return 0

def main():
    setup()
    badvalue = part1()
    part2(badvalue)

if __name__ == "__main__":
    main()