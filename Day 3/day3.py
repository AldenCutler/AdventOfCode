import os
from pathlib import Path

SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH = SCRIPT_PATH.parent.parent/Path(SCRIPT_PATH.parent.name,"input.txt")
with open(INPUT_PATH) as file:
    lines = file.read().splitlines()


#################################################################
### Part 1 - Find the sum of all numbers adjacent to a symbol ###
#################################################################
'''
The engine schematic (your puzzle input) consists of a visual representation of the engine. 
There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, '
is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). 
Every other number is adjacent to a symbol and so is a part number; their sum is 4361.
'''
symbols = ['#', '/', '*', '-', '+', '&', '$', '=', '@', '%']
def part1():
    sum = 0
    num_str = ''

    for row, line in enumerate(lines):
        line += '.'
        for col, char in enumerate(line):
            if char.isdigit():                                          # if char is a digit, add it to the number string
                num_str += char

            elif num_str:                                               # if char is not a digit, check if the number string is adjacent to a symbol
                if (check_lines(line, row, col, num_str)):
                    sum += int(num_str)

                num_str = ''                                            # reset the number string for the next number

    print("Part 1:", sum)


def check_lines(line, row, col, num_str):
    row_start = max(0, row - 1)
    row_end = min(len(lines), row + 2)

    col_start = max(0, col - 1 - len(num_str))
    col_end = min(len(line) - 1, col + 1)

    for row_mod in range(row_start, row_end):                           # check the line above and below
        for col_mod in range(col_start, col_end):                       # check the column to the left and right
            if lines[row_mod][col_mod] in symbols:                      # the number string is adjacent to this symbol so return True
                return True
    return False




####################################################
### Part 2 - Find the sum of all the gear ratios ###
####################################################
'''
A gear is any * symbol that is adjacent to exactly two part numbers. 
Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer 
can figure out which gear needs to be replaced.

Consider the same engine schematic again:
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so 
its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. 
(The * adjacent to 617 is not a gear because it is only adjacent to one part number.) 
Adding up all of the gear ratios produces 467835.
'''
from collections import defaultdict
dct = defaultdict(list)
def part2():
    gearSum = 0
    num_str = ''

    for row, line in enumerate(lines):
        line += '.'

        for col, char in enumerate(line):
            if char.isdigit():                                          # if char is a digit, add it to the number string
                num_str += char

            elif num_str:                                               # if char is not a digit, check if the number string is adjacent to a symbol
                
                row_start = max(0, row - 1)
                row_end = min(len(lines), row + 2)

                col_start = max(0, col - 1 - len(num_str))
                col_end = min(len(line) - 1, col + 1)

                for row_mod in range(row_start, row_end):
                    for col_mod in range(col_start, col_end):
                        if lines[row_mod][col_mod] == '*':
                            dct[row_mod, col_mod].append(int(num_str))

                num_str = ''                                            # reset the number string for the next number

    for num in dct.values():                                            # sum the gear ratios
        if len(num) == 2:                                               # only consider gears with exactly two adjacent numbers
            gearSum += num[0] * num[1]

    print("Part 2:", gearSum)

#################################################################
part1()
part2()