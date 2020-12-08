import json
import string

def passport_to_json(passport_string):
    return '{"' + passport_string.replace('\n',' ').strip().replace(' ','","').replace(':','":"') + '"}'

def main():
    text_file = open("day4.txt",'r')

    passport_list = []
    passport_line = ""
    for line in text_file:
        #print(line)
        if line == "\n":
            # Add line to array
            passport_list.append(passport_to_json(passport_line))
            passport_line = ""
        else:
            passport_line += line
    
    # Add last passport
    passport_list.append(passport_to_json(passport_line))

    text_file.close()

    # define list of required fields
    valid_set = set(['byr','iyr','eyr','hgt','hcl','ecl','pid'])

    valid = 0
    invalid = 0
    for passport in passport_list:
        passport_dict = json.loads(passport)

        # confirm list of required fields is present
        if valid_set.issubset(passport_dict.keys()):
            byr = passport_dict["byr"]
            iyr = passport_dict["iyr"]
            eyr = passport_dict["eyr"]
            hgt = passport_dict["hgt"]
            hcl = passport_dict["hcl"]
            ecl = passport_dict["ecl"]
            pid = passport_dict["pid"]

            # perform field level validations
            if len(byr)==4 and 1920 <= int(byr) <= 2002 and \
                len(iyr)==4 and 2010 <= int(iyr) <= 2020 and \
                len(eyr)==4 and 2020 <= int(eyr) <= 2030 and \
                (("cm" in hgt and 150 <= int(hgt[0:-2]) <= 193) or ("in" in hgt and 59 <= int(hgt[0:-2]) <= 76)) and \
                hcl[0] == '#' and len(hcl) == 7 and all(c in string.hexdigits for c in hcl[1:]) and \
                ecl in ('amb','blu','brn','gry','grn','hzl','oth') and \
                len(pid)==9 and pid.isnumeric():
                #print("VALID: " + passport)
                valid +=1
            else:
                invalid += 1
        else:            
            #print("INVALID: " + passport)
            invalid += 1

    print(f'{len(passport_list)=} {valid=} {invalid=}')


if __name__ == "__main__":
    main()