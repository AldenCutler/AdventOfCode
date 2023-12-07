#include <stdlib.h>
#include <stdio.h>

void part1(FILE* fp, int* times, int* distances) {
    
    // find the number of ways to beat the record: loop over every race and multiply num of ways together to get answer
    int ans = 1;
    for (int i = 0; i < 4; i++) {
        int record = distances[i];

        // check the distance for each time from 0 to times[i]
        //  - if the distance is greater than the record, increment ways
        //  note: we don't need to check the distance for times[i] because that would mean we never let go of the button.
        //        similarly, we don't need to check the distance for 0 because that would mean we never pressed the button.
        int ways = 0;
        for (int j = 1; j < times[i]; j++) {
            
            // distance = timePressed * timeRemaining
            int dist = j * (times[i] - j);
            if (dist > record) {
                ways++;
            }

        }

        ans *= ways;

    }

    printf("Part 1 Answer: %d\n", ans);
}

void part2(FILE* fp) {
    
    // distance now holds the record. We need to find the number of ways to beat the record.
    // in this case, we don't need to brute force the answer:
    // we just have to find the least amount of time we can hold the button to beat the record.
    // the number of ways to beat the record is:
    /*
    upperBound = raceTime - lowestTime
    lowerBound = lowestTime
    ways = upperBound - lowerBound + 1
    */

    // these are the values for my input, yours may be different
    long time = 46807866;
    long long distance = 214117714021024;

    
    // find the lowest time that we can hold the button to beat the record
    long lowestTime = 0;
    while (lowestTime * (time - lowestTime) < distance) {
        lowestTime++;
    }

    // find the upper bound
    long upperBound = time - lowestTime;

    // find the number of ways to beat the record
    long ways = upperBound - lowestTime + 1;

    printf("Part 2 Answer: %ld\n", ways);
}




int main(int argc, char *argv[]) {

    // check for correct usage
    if (argc != 2) {
        printf("Usage: ./day6 <input file>\n");
        return 1;
    }

    // open file
    FILE *fp = fopen(argv[1], "r");

    // check if file opened correctly
    if (fp == NULL) {
        printf("Error opening file %s\n", argv[1]);
        return 1;
    }


    // comment out the following lines if you want to use the sample input
    int* times = malloc(4 * sizeof(int));
    int* distances = malloc(4 * sizeof(int));

    fscanf(fp, "Time: %d %d %d %d\n", &times[0], &times[1], &times[2], &times[3]);
    fscanf(fp, "Distance: %d %d %d %d\n", &distances[0], &distances[1], &distances[2], &distances[3]);

    // uncomment the following lines if you want to use the sample input
    // int * times = malloc(3 * sizeof(int));
    // int * distances = malloc(3 * sizeof(int));

    // fscanf(fp, "Time: %d %d %d\n", &times[0], &times[1], &times[2]);
    // fscanf(fp, "Distance: %d %d %d\n", &distances[0], &distances[1], &distances[2]);

    part1(fp, times, distances);
    part2(fp);

    // close file
    fclose(fp);

    exit(EXIT_SUCCESS);
}

