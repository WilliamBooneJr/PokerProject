import stdio
import stdarray
import random
import stdio
import sys

#Creates an array of all suits and array of all card ranks, cocoantes these arrays to create a full deck
SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = []
for suit in SUITS:
    for rank in RANKS:
        card = rank + ' of ' + suit
        deck += [card]

#Randomnly iterates and prints 5 cards for every n poker hands
hand = []
n = int(sys.argv[1])
for i in range(n):
    stdio.writeln('Hand Number ' + str(i+1) + ' is..')
    for i in range(0,5):
        x = random.randrange(0, 52)
        stdio.writeln(deck[x])
        hand += [x] 
    stdio.writeln()
