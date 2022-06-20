"""
File: hangman.py
Name: Han Tsai
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program plays hangman game.
    Users sees a dashed word, trying to
    correctly figure the un-dashed word out
    by inputting one character each round.
    If the user input is correct, show the
    updated word on console. Players have N_TURNS
    chances to try and win this game.
    """
    n = N_TURNS
    s = random_word()
    # define answer
    answer = dash(s)
    print("THe word looks like " + answer)
    print("You have " + str(n) + " wrong guesses left.")
    while True:
        # stop the loop when win the game
        if answer == s:
            break
        # define number of loop
        i = -1
        # stop the loop when number of wrong guess = 7
        if n < 1:
            print("You are completely hung : (")
            print("The word was: " + s)
            break
        else:
            guess = input("Your guess: ")
            # judge if guess is a letter
            if guess.isalpha():
                if len(guess) == 1:
                    # case-insensitive
                    guess1 = guess.upper()
                    while True:
                        i += 1
                        # when loop is complete
                        if i > len(s)-1:
                            if guess1 in s:
                                print("You are correct!")
                                print("The word looks like " + answer)
                                print("You have " + str(n) + " wrong guesses left.")
                            else:
                                n -= 1
                                print("There is no " + guess1 + "'s in the word.")
                                if n > 0:
                                    print("The word looks like " + answer)
                                    print("You have " + str(n) + " wrong guesses left.")
                            break
                        # fill the correct guess in the dash
                        ch = s[i]
                        if ch == guess1:
                            answer = replace(answer, i, guess1)
                        # when word is correct
                        if answer == s:
                            print("You are correct!")
                            print("You win!!")
                            print("The word was: " + answer)
                            break
                else:
                    print("Illegal format.")
            else:
                print("Illegal format.")


def replace(old_s, num, new):
    """
    This is function that fill the correct guess in the dash.
    """
    ans = ""
    ans += old_s[:num]
    ans += new
    ans += old_s[(num + 1):]
    return ans


def dash(word):
    """
    This is function that calculate how many dashes will be printed.
    """
    ans = ""
    for i in range(len(word)):
        ans += "_"
    return ans


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


if __name__ == '__main__':
    main()

