MENU = "(G)et a valid score (must be 0-100 inclusive) \n(P)rint result \n(S)how stars \n(Q)uit"
GET_SCORE_OPTION = 'G'
PRINT_RESULT_OPTION = 'P'
SHOW_STAR_OPTION = 'S'
QUIT_OPTION = 'Q'

def main():
    print(MENU)
    choice = input("Please enter your option: ")
    while choice != QUIT_OPTION:
        if choice == GET_SCORE_OPTION:
            score = get_valid_score()
        elif choice == PRINT_RESULT_OPTION:
            print(determine_result(score))
        elif choice == SHOW_STAR_OPTION:
            display_asterisks()
        else:
            print("Invalid option")
        print(MENU)
        choice = input("Please enter your option: ")


def get_valid_score():
    score = float(input("Enter your score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter your score: "))
    return score


main()