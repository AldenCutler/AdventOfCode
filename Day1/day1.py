import re


def part1():

    # read input file
    file = open("C:/Users/alden/Downloads/input.txt", "r")
    lines = file.readlines()
    file.close()

    sum = 0

    for i in range(len(lines)):
        line = lines[i]
        n = len(line)
        
        # remove newline character
        if line[n-1] == "\n":
            line = line[:n-1]
            n -= 1
        
        # start and end indices of each line
        j = 0
        k = n - 1
        
        # to store first and last digits
        first = 0
        last = 0
        
        # find first digit index and store in j
        while j < n:
            if line[j].isdigit():
                first = line[j]
                break
            j += 1

        # find last digit index and store in k
        while k >= 0:
            if line[k].isdigit():
                last = line[k]
                break
            k -= 1
            
        num = ""
        num += str(first)
        num += str(last)
        
        # print(num)
        # print(str(i+1) + ": " + num + "  --  " + line)    --> for debugging
        
        # concatenate the two digits into an int and add to sum
        sum += int(num)
    return sum
    #print(sum)
            

# part 2 is similar to part 1, but digits can be spelled out as a word (one, two, three, etc.)
# my approach finds the indices of all digits and then all words, and then compares the indices,
# but you could also go through the line and replace all words with digits, and then do the same
# thing as part 1
def part2():

    # read input file
    file = open('C:/Users/alden/Downloads/input.txt', "r")
    lines = file.readlines()
    file.close()
    
    sum = 0

    for i in range(len(lines)):
        line = lines[i]
        n = len(line)
        
        # remove newline character
        if line[n-1] == "\n":
            line = line[:n-1]
            n -= 1
        
        # start and end indices of each line
        j = 0
        k = n - 1
        
        # find first digit index and store in j
        while j < n:
            if line[j].isdigit():
                break
            j += 1
        # find last digit index and store in k
        while k >= 0:
            if line[k].isdigit():
                break
            k -= 1

        # find indices of all words
        words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        indices = []
        occurrences = []
        for word in words:
            if word in line:
                index = [m.start() for m in re.finditer(word, line)]
                for l in index:
                    indices.append(l)
                for _ in range(line.count(word)):
                    occurrences.append(word)

        first = 0
        last = 0

        if len(indices) != 0:
            
            # if first word comes before first digit, store index of first word in outsideIndices
            if min(indices) < j:
                first = occurrences[indices.index(min(indices))]
            else: # otherwise, store index of first digit in outsideIndices
                first = line[j]
            
            # if last word comes after last digit, store index of last word in outsideIndices
            if max(indices) > k:
                last = occurrences[indices.index(max(indices))]
            else: # otherwise, store index of last digit in outsideIndices
                last = line[k]

        else: 
            first = line[j]
            last = line[k]

        # convert words to digits
        if first == "zero":
            first = 0
        elif first == "one":
            first = 1
        elif first == "two":
            first = 2
        elif first == "three":
            first = 3
        elif first == "four":
            first = 4
        elif first == "five":
            first = 5
        elif first == "six":
            first = 6
        elif first == "seven":
            first = 7
        elif first == "eight":
            first = 8
        elif first == "nine":
            first = 9

        if last == "zero":
            last = 0
        elif last == "one":
            last = 1
        elif last == "two":
            last = 2
        elif last == "three":
            last = 3
        elif last == "four":
            last = 4
        elif last == "five":
            last = 5
        elif last == "six":
            last = 6
        elif last == "seven":
            last = 7
        elif last == "eight":
            last = 8
        elif last == "nine":
            last = 9
            
        num = ""
        num += str(first)
        num += str(last)
        
        # print(str(i+1) + ": " + num + "  " + "j: " + str(j) + "  k: " + str(k) + "  --  " + line)     --> for debugging
        
        # concatenate the two digits into an int and add to sum
        sum += int(num)

    return sum
    #print(sum)

part1()
part2()