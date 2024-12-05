data = []
with open('test.txt') as f:
    data = f.read().splitlines()
    
# Part 1 
def part1(data):
    safe = 0
    for report in data:
        report = report.split(' ')
        report = [int(level) for level in report]
        print(report)
        
        if all(report[i] < report[i+1] for i in range(len(report)-1)):
            # increasing - check if difference between each number is between 1 and 3
            diff = [report[i+1] - report[i] for i in range(len(report)-1)]    
            if all(d in [1,2,3] for d in diff):
                safe += 1
        elif all(report[i] > report[i+1] for i in range(len(report)-1)):
            # decreasing - check if difference between each number is between 1 and 3
            diff = [report[i] - report[i+1] for i in range(len(report)-1)]
            if all(d in [1,2,3] for d in diff):
                safe += 1
                            
    return safe

print('\nPart 1:', part1(data), '\n')


# Part 2
def part2(data):
    # part 2 is same as part 1 but with 1 extra condition:
    # - if only one level is causing a report to be unsafe, then it can be counted as safe
    safe = 0
    for report in data:
        report = report.split(' ')
        report = [int(level) for level in report]
        print(report)
        
        if all(report[i] < report[i+1] for i in range(len(report)-1)):
            # increasing - check if difference between each number is between 1 and 3
            diff = [report[i+1] - report[i] for i in range(len(report)-1)]    
            if all(d in [1,2,3] for d in diff):
                safe += 1
        elif all(report[i] > report[i+1] for i in range(len(report)-1)):
            # decreasing - check if difference between each number is between 1 and 3
            diff = [report[i] - report[i+1] for i in range(len(report)-1)]
            if all(d in [1,2,3] for d in diff):
                safe += 1
                
        # extra condition
        
                
    return safe

print('\nPart 2:', part2(data), '\n')