import numpy as np

with open('input.txt') as f:
    lines = f.readlines()
    
##############
### Part 1 ###
##############

# Found this on stackoverflow: https://stackoverflow.com/questions/24467972/calculate-area-of-polygon-given-x-y-coordinates/30408825
def PolyArea(x,y):
    return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))


location = (0,0)    # starting location
points = set()      # set of points visited
points.add(location)

x = []              # list of x coordinates
y = []              # list of y coordinates

directions_map = {"U": (1, 0), "D": (-1, 0), "R": (0, 1), "L": (0, -1)}

for line in lines:
    line = line.strip()
    dir, steps, hex_code = line.split()
    steps = int(steps)
    
    # dir = line[0]
    # steps = int(line[1])
    current_dir = directions_map[dir]
    
    for i in range(steps + 1):
        points.add((location[0] + i * current_dir[0], location[1] + i * current_dir[1]))
        
    location = (location[0] + steps * current_dir[0], location[1] + steps * current_dir[1])
    
    x.append(location[0])
    y.append(location[1])

area = PolyArea(x, y)
outer_length = len(points)
# A = i + b/2 - 1 -> i = A + 1 - b/2
# assert( % 2 == 0)
inner_area = area + 1 - outer_length // 2
print("\nPart 1 Solution: ", int(inner_area + outer_length), "\n")