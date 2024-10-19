COLOUR_TO_HEXADECIMAL = {"aliceblue": "#b0bf1a", "black": "#000000", "pink": "#ffc0cb", "ruby": "#e0115f", "lavender": "#e6e6fa",
                         "iris": "#5a4fcf", "indigo": "#4b0082", "floralwhite": "#fffaf0", "electricblue": "#7df9ff", "deeppeach": "#ffcba4"}
colour = input("Please enter a colour: ").lower()
while colour != "":
    try:
        print(f"The colour {colour} is {COLOUR_TO_HEXADECIMAL[colour]}.")
    except KeyError:
        print("The colour entered is invalid, please try again.")
    colour = input("Please enter a colour: ").lower()
