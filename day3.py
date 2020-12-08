def count_trees(lines, right_step, down_step):
    total_rows = len(lines)
    col_length = len(lines[0]) - 1 # Remove carriage return
    row = 0
    col = 0
    trees = 0
    while row < total_rows:
        #input(str(row) + " " + lines[row][col % col_length])
        if lines[row][col % col_length] == '#': trees += 1
        col += right_step
        row += down_step
    
    return trees


def main():
    text_file = open("day3.txt", "r")
    lines = text_file.readlines()
    text_file.close()

    product = count_trees(lines, 1, 1)
    product *= count_trees(lines, 3, 1)
    product *= count_trees(lines, 5, 1)
    product *= count_trees(lines, 7, 1)
    product *= count_trees(lines, 1, 2)

    print(f'{product=}')


if __name__ == "__main__":
    main()