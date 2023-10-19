"""This program imports stdrandom.py and stdstats.py and uses them to simulate "n" poker hands.
and estimates the probabilities of getting one pair, two pair, three of a kind, a full house, a flush, a straight, and a straight flush through a simulation. 
Divide your program into appropriate functions and defend your design decisions."""

import stdstats
import stdarray
import stdrandom
import stdio
import sys

#Create arrays to store all suits and ranks, concatenate these values to create a full deck
deck = stdarray.create2D(52, 2, 0)
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

index = 0
for suit in suits:
    for rank in ranks:
        deck[index] = [suit, rank]
        index += 1

#create a copy of the deck so that we can remove cards that are selected for the hand
#simulate a poker hand by randomly selecting 5 cards from the deck

def generate_hand():
    hand = stdarray.create2D(5, 2, 0)
    deckcopy = deck[:] #create a copy of the deck so that we can remove cards that are selected for the hand
    for i in range(5):
        hand[i] = deckcopy[stdrandom.uniformInt(0, 51)]
        deckcopy.remove(hand[i])
    return hand

#set up a function to check if a hand has a pair, two pair, three of a kind, a straight, a flush, a full house, four of a kind, straight flush, and a royal flush
#running into issue where pair gets double counted and hand "rank" gets prematurely determined. Need to start with the highest check and descend down to the lowest check
def check_pairkind(hand):
    pair_record = set()
    pairs = 0
    three_kind = 0
    for i in range(4):
        for j in range(i + 1, 5):
            if hand[i][1] == hand[j][1]:
                if hand[i][1] not in pair_record:
                    pairs += 1
                    pair_record.add(hand[i][1])
                else:
                    three_kind += 1
    if three_kind >= 1:
        return three_kind
    if pairs >= 1:
        return pairs
    return 0

def check_royalflush(hand): #check if all suits are the same and contains all royal cards(royal flush)
    royal_flush = 0
    royalty = 0
    for i in range(0, 5):
        if hand[i][1] == ranks[9] or hand[i][1] == ranks[10] or hand[i][1] == ranks[11] or hand[i][1] == ranks[12]:
            royalty += 1
    if royalty == 5:
        if hand[1][0] == hand[2][0] == hand[3][0] == hand[4][0] == hand[5][0]:
            royal_flush += 1
    return royal_flush

def check_straightflush(hand): #check if all suits are the same and cards are in sequential order(straight flush)
    pass
 
def check_fourkind(hand): #check if 4 cards have the same rank
    pass

def check_fullhouse(hand): #check if 3 cards have the same rank and 2 cards have the same rank
    pass

def check_flush(hand): #check if all suits are the same
    flush = 0
    if hand[1][0] == hand[2][0] == hand[3][0] == hand[4][0] == hand[5][0]:
        flush += 1 
    return flush

def check_straight(hand): #check if all cards are in sequential order
    pass

def check_threekind(hand): #check if 3 cards have the same rank
    pass
def check_twopair(hand): #check if 2 cards have the same rank
    pass
def check_onepair(hand): #check if 2 cards have the same rank
    pass

#set up variables to store the counts of each hand type
one_pair = 0
two_pair = 0
three_kind = 0
straight = 0
flush = 0
full_house = 0
four_kind = 0
straight_flush = 0
royal_flush = 0

#set up a function to simulate "n" poker hands and count the number of each hand type

def simulate_poker(n):
    count = 0 
    while count < n:
        hand = generate_hand()
        if check_pairkind(hand) == 1:
            one_pair += 1
        elif check_pairkind(hand) == 2:
            two_pair += 1
        elif check_pairkind(hand) == 3:
            three_kind += 1
        elif check_pairkind(hand) == 4:
            four_kind += 1
        elif check_pairkind(hand) == 5:
            full_house += 1
        elif check_pairkind(hand) == 6:
            flush += 1
        elif check_pairkind(hand) == 7:
            straight += 1
        elif check_pairkind(hand) == 8:
            straight_flush += 1
        elif check_pairkind(hand) == 9:
            royal_flush += 1
        count += 1

#set up a function to print the probabilities of each hand type based on simulation

def print_probabilities(n):
    simulate_poker(n)
    stdio.writeln('One pair success: ' + str(one_pair/n))
    stdio.writeln('Two pair success: ' + str(two_pair/n))
    stdio.writeln('Three of a kind success: ' + str(three_kind/n))
    stdio.writeln('Straight success: ' + str(straight/n))
    stdio.writeln('Flush success: ' + str(flush/n))
    stdio.writeln('Full house success: ' + str(full_house/n))
    stdio.writeln('Four of a kind success: ' + str(four_kind/n))
    stdio.writeln('Straight flush success: ' + str(straight_flush/n))
    stdio.writeln('Royal flush success: ' + str(royal_flush/n))













testhand = [['Hearts', '2'], ['Hearts', '2'], ['Clubs', '3'], ['Hearts', '3'], ['Spades', '3']]
stdio.writeln(generate_hand())


    

