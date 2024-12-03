#include <stdlib.h>
#include <stdio.h>

#define A 14
#define K 13
#define Q 12
#define J 11
#define T 10

#define LEN 1000

int cards[] = {A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2};

int getCardValue(char card) {
    switch (card) {
        case 'A':
            return A;
        case 'K':
            return K;
        case 'Q':
            return Q;
        case 'J':
            return J;
        case 'T':
            return T;
        default:
            return card - '0';
    }
}

int getTypeFromHand(char* hand) {

    int* cardCounts = malloc(15 * sizeof(int));
    for (int i = 0; i < 15; i++) {
        cardCounts[i] = 0;
    }

    for (int i = 0; i < 5; i++) {
        int card = getCardValue(hand[i]);
        cardCounts[card]++;
    }

    int fiveOfAKind = 0;
    int fourOfAKind = 0;
    int fullHouse = 0;
    int threeOfAKind = 0;
    int twoPairs = 0;
    int onePair = 0;

    for (int i = 0; i < 15; i++) {
        if (cardCounts[i] == 5) {
            fiveOfAKind = 1;
        } else if (cardCounts[i] == 4) {
            fourOfAKind = 1;
        } else if (cardCounts[i] == 3) {
            threeOfAKind = 1;
        } else if (cardCounts[i] == 2) {
            if (onePair == 1) {
                twoPairs = 1;
                onePair = 0;
            } else {
                onePair = 1;
            }
        }
    }

    if (fiveOfAKind == 1) {
        return 0;
    } else if (fourOfAKind == 1) {
        return 1;
    } else if (fullHouse == 1) {
        return 2;
    } else if (threeOfAKind == 1) {
        return 3;
    } else if (twoPairs == 1) {
        return 4;
    } else if (onePair == 1) {
        return 5;
    } else {    // high card
        return 6;
    }

}

char** orderHands(char** hands, int len) {

    // handTypes[i][0] = hand type
    // handTypes[i][1] = hand index in hands array
    int** handTypes = malloc(len * sizeof(int*));
    for (int i = 0; i < len; i++) {
        handTypes[i] = malloc(2 * sizeof(int));
    }

    // get hand types
    for (int i = 0; i < len; i++) {
        int handType = getTypeFromHand(hands[i]);
        handTypes[i][0] = handType;
        handTypes[i][1] = i;
        // printf("%d\n", handType);
    }

    // sort hand types in ascending order (break ties with first card in hand)
    // using simple bubble sort (n is small enough)
    for (int i = 0; i < len; i++) {
        for (int j = 0; j < len - i - 1; j++) {

            // if hand type is greater, swap
            if (handTypes[j][0] > handTypes[j+1][0]) {
                int* temp = handTypes[j];
                handTypes[j] = handTypes[j+1];
                handTypes[j+1] = temp;
            } 
            
            // if hand type is equal, compare first card in hand
            else if (handTypes[j][0] == handTypes[j+1][0]) {
                int handIndex1 = handTypes[j][1];
                int handIndex2 = handTypes[j+1][1];
                int card1 = getCardValue(hands[handIndex1][0]);
                int card2 = getCardValue(hands[handIndex2][0]);
                if (card1 < card2) {
                    int* temp = handTypes[j];
                    handTypes[j] = handTypes[j+1];
                    handTypes[j+1] = temp;
                }
            }
        }
    }

    // reorder hands array
    char** newHands = malloc(len * sizeof(char*));
    for (int i = 0; i < len; i++) {
        int handIndex = handTypes[i][1];
        newHands[i] = hands[handIndex];
    }

    return newHands;
}

int main(int argc, char** argv) {

    if (argc != 2) {
        printf("Usage: %s <input file>\n", argv[0]);
        return 1;
    }

    FILE *fp = fopen(argv[1], "r");
    if (fp == NULL) {
        printf("Could not open file %s\n", argv[1]);
        return 1;
    }

    // read in data
    char* line = {NULL};
    size_t len = 0;
    ssize_t read;
    char** hands = malloc(LEN * sizeof(char*));
    int* bets = malloc(LEN * sizeof(int));
    int index = 0;
    while ((read = getline(&line, &len, fp)) != -1) {

        // get first 5 characters and store in array
        char* hand = malloc(5 * sizeof(char));
        for (int i = 0; i < 5; i++) {
            hand[i] = line[i];
        }

        // get bet
        char* betStr = malloc(3 * sizeof(char));
        for (int i = 6; i < 9; i++) {
            betStr[i-6] = line[i];
        }
        int bet = atoi(betStr);

        printf("%s %d\n", hand, bet);
        
        hands[index] = hand;
        bets[index] = bet;

        index++;
    }


    // order hands by type (five of a kind, four of a kind, full house, etc.)  
    char** ordered = orderHands(hands, LEN);

    // get ordered bets from ordered hands
    int* orderedBets = malloc(LEN * sizeof(int));
    for (int i = 0; i < LEN; i++) {
        int handIndex = 0;
        for (int j = 0; j < LEN; j++) {
            if (hands[j] == ordered[i]) {
                handIndex = j;
                break;
            }
        }
        orderedBets[i] = bets[handIndex];
    }

    // print ordered hands
    printf("\n");
    for (int i = 0; i < LEN; i++) {
        printf("%s %d\n", ordered[i], orderedBets[i]);
    }

    // loop through ordered hands and bets and get winnings by adding each bet multiplied by its index
    int winnings = 0;
    for (int i = 0; i < LEN; i++) {
        int rank = LEN - i;
        winnings += orderedBets[i] * rank;
    }

    printf("%d\n", winnings);



    fclose(fp);
    return 0;

}