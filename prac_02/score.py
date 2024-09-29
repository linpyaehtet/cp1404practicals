"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50

def main():
    score = float(input("Enter score: "))
    print(determine_result(score))
    random_score = random.randint(MINIMUM_SCORE, MAXIMUM_SCORE)
    print(f"Random generated score is {random_score} and the result is {determine_result(random_score)}")


def determine_result(score):
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        return "Invalid score"
    elif score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    elif score >= PASSABLE_THRESHOLD:
        return "Passable"
    else:
        return "Bad"


main()