#5>First Ace
import math
from fractions import Fraction

# Define a function to compute factorial of a given number n using math.factorial
def fact(n):
    return math.factorial(n)

# Total number of cards in a deck
N = 52
# Number of aces in the deck
A = 4
# Number of non-aces in the deck
nA = N - A

# List to store probabilities of first ace appearing at each position
L1 = []
# Variable to store the expected number of cards drawn to get the first ace
Sum = 0

# Calculate the probability of the first ace appearing at each position
for i in range(nA):
    # Calculate probability using combinations and adjust for non-aces picked before the first ace
    prob = Fraction((fact(nA) / fact(N)) * (fact(51 - i) / fact(nA - i)) * 4).limit_denominator()
    L1.append(prob)

# Calculate the expected number by multiplying each position by its probability and summing up
for i in range(len(L1)):
    Sum += (i + 1) * L1[i]

# Output the expected number of cards to be drawn to see the first ace
print(Sum)

