MENU = "(G)et a valid score (must be 0-100 inclusive) \n(P)rint result \n(S)how stars \n(Q)uit"

GET_SCORE_OPTION = 'G'
PRINT_RESULT_OPTION = 'P'
SHOW_STAR_OPTION = 'S'
QUIT_OPTION = 'Q'

MAXIMUM_SCORE = 100
MINIMUM_SCORE = 0
EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50

def main():
    print(MENU)
    choice = input("Please enter your option: ").upper()
    score = 0
    while choice != QUIT_OPTION:
        if choice == GET_SCORE_OPTION:
            score = get_valid_score()
            print()
        elif choice == PRINT_RESULT_OPTION:
            print(determine_result(score))
            print()
        elif choice == SHOW_STAR_OPTION:
            display_asterisks(score)
            print()
        else:
            print("Invalid option")
        print(MENU)
        choice = input("Please enter your option: ").upper()
    print("Farewell")


def get_valid_score():
    score = float(input("Enter your score: "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid score")
        score = float(input("Enter your score: "))
    return score


def determine_result(score):
    if score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    elif score >= PASSABLE_THRESHOLD:
        return "Passable"
    else:
        return "Bad"


def display_asterisks(score):
    print('*' * int(score))


main()