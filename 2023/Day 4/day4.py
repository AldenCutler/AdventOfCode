import os
from pathlib import Path

SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH = SCRIPT_PATH.parent.parent/Path(SCRIPT_PATH.parent.name,"input.txt")
with open(INPUT_PATH) as file:
    lines = file.read().splitlines()


def part1():
    sum = 0
    for line in lines:
        count = 0
        
        # get numbers
        winning_numbers = line.split("|")[0].split(" ")[2:]
        numbers = line.split("|")[1].split(" ")
        
        # filter out whitespace
        winning_numbers = list(filter(lambda a: a != '', winning_numbers))
        numbers = list(filter(lambda a: a != '', numbers))

        for num in numbers:
            if num in winning_numbers:
                count += 1
                winning_numbers.remove(num)     # I'm not sure if there's an edge case where they don't want a number to count twice, but this works so I'm leaving it
                
        if count > 0:
            sum += 2 ** (count - 1)
        
    print(sum)
   
   
   
def part2():
    
    # build a dictionary to store the number of copies of each card
    dct = {i:1 for i in range(1, len(lines) + 1)}
    print(dct)

    for i, row in enumerate(lines, start=1):
        count = 0

        # parse the winning numbers and the hand
        winning_numbers = row.split("|")[0].split(" ")[2:]
        hand = row.split("|")[1]

        # filter out whitespace (might not be needed, I'm not sure, it seems to work either way on the test cases)
        winning_numbers = list(filter(lambda a: a != '', winning_numbers))

        # count the number of winning numbers in the hand
        for card in hand.split():
            if card in winning_numbers:
                count += 1
        
        # add the number of copies of the card to the dictionary
        for j in range(i + 1, i + count + 1):
            dct[j] = dct.get(j,0) + dct[i]

    # the sum of the values in the dictionary is the total number of cards
    print(sum(dct.values()))