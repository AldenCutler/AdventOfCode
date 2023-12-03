from collections import defaultdict

# Read in the input
lines = [x for x in open("C:/Users/alden/OneDrive - Worcester Polytechnic Institute (wpi.edu)/Documents/projects/AdventOfCode/Day 2/input.txt").read().strip().split("\n")]

def part1():
    idSum = 0

    for line in lines:
        game_id = int(line.split(":")[0].split(" ")[1])
        line = line.split(":")[1]   # Remove the game id
        possible = True

        for colors in line.split(";"):      # colors is a string of the form "2 red, 3 green, 4 blue"
            counts = defaultdict(int)

            # Count the number of each color
            for review in colors.split(", "):
                
                # Remove whitespace
                review = review.strip() 
                
                # Add the number of that color to the count
                counts[review.split(" ")[1]] += int(review.split(" ")[0])

            # Check if the counts are valid
            if not (counts["red"] <= 12 and counts["green"] <= 13 and counts["blue"] <= 14):
                possible = False

        if possible:
            idSum += game_id
      
    print(idSum)
    return idSum

def part2():
    powerSum = 0
    
    for line in lines:
        line = line.split(":")[1]
        min_counts = defaultdict(int)

        for colors in line.split(";"):
            counts = defaultdict(int)

            for review in colors.split(", "):
                review = review.strip()
                counts[review.split(" ")[1]] += int(review.split(" ")[0])

            for k, v in counts.items():
                min_counts[k] = max(min_counts[k], v)

        powerSum += min_counts["red"] * min_counts["green"] * min_counts["blue"]
      
    print(powerSum)
    return powerSum
        
part1()
part2()