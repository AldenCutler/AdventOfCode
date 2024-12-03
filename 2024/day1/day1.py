left = []
right = []
with open('input.txt') as f:
    for line in f:
        line = line.split()
        left.append(int(line[0]))
        right.append(int(line[1]))
        
### Part 1 ###
# pair up the numbers abd measure how far apart they are:
# sort both lists
# sum up differences
left.sort()
right.sort()

total = 0
for i in range(len(left)):
    total += abs(left[i] - right[i])
    
print('Part 1:', total)

### Part 2 ###
# need to calculate how often each number from the left list appears in the right list
# calculate a 'similarity score' by adding up each number in the left list after multiplying it
# by the number of times that number appears in the right list
left = []
right = []
with open('input.txt') as f:
    for line in f:
        line = line.split()
        left.append(int(line[0]))
        right.append(int(line[1]))
        
freq = {}
for num in right:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
        
score = 0
for num in left:
    if num in freq:
        score += num * freq[num]
    
print('Part 2:', score)