#!/usr/bin/python

"""
A quize game
"""


def game():
    """
    Main function of the game
    """

    guesses = []
    correct_guesses = 0
    question_number = 1

    for key in questions:  # Prints the keys in our dictionary
        print("\n...................................................................................\n")
        print(key)

        for answers in options[question_number - 1]:  # Prints the value of a key
            print(answers)

        guess = input("\nChoose:\nA, B, C or D: ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)  # Answer should be the same asour options

        question_number += 1

    score(correct_guesses, guesses)



def check_answer(answer, guess):
    """
    Checks answers to our questions
    """

    if answer == guess:
        print("Correct!!")
        return 1
    else:
        print("Incorrect!")
        return 0



def score(correct_guesses, guesses):
    """
    Checks our final score after the game
    """

    print("\n....................................................................................")
    print("RESULTS")
    print("....................................................................................\n")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for x in guesses:
        print(x, end=" ")
    print()

    score = int((correct_guesses / len(questions)) * 100)
    print(f"\nYour score is {score}%")

def play_again():
    """
    Asks if the user wants ti play again
    """

    response = input("\nDo you want to play again? (yes/no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False


questions = {
    #            "Who created Python? \n": "A",
    #       "What year was Python created? \n": "B",
    #       "Python is tributed to which comedy group? \n": "C",
            "Who created this game? \n": "A",
            "How long have we been dating now? \n": "C",
    #        "Which national team has the most Rugby World cups? \n": "D",
            "In what year did we start dating? \n": "C",
            "Where did we go to on our first date? \n": "D",
            "Do you still remember what I was wearing when we first met? \n": "A",
            "What happened the night of our 1st annivesary? \n": "B",
            "What show(s) do we enjoy watching together? \n": "D",
            "Do you like my game? \n": "D"
}

options = [
    #    ["A. Guido Van Rossum", "B. David Mulan", "C. Amahle Dlamini", "D.Xolani Nkonzo"],
    #    ["A. 10 000BC", "B. 1991", "C. 2020", "D. None of the above"],
    #    ["A. D.SNL", "B. Lonely Island", "C. Monty Python", "D. Regular Show"],
    ["A. Tafara Nyamhunga", "B. Guido Van Rossum", "C. Franklin Saint", "D. None of the above"],
    ["A. 10 years on the dot", "B. We are not dating please!!", "C. 5 years on 31/12/23", "D. 'Ewww', in Seemah's voice"],
    #    ["A. New Zealand", "B. Brazil", "C. Germany", "D. South Africa"],
    ["A. We never dated.", "B. 2021", "C. 2018", "D. You too broke for me."],
    ["A. Your place", "B. I don't remember", "C. None of the above", "D. SunCoast in Durban"],
    ["A. Yes I do, 'Black adidas bottoms, black airforce and a creme tee'", "B. Nothing", "C. I have forgotten", "D. Didn't pay attention"],
    ["A. We went out on a nice date", "B. I didn't show up to the picnic you had prepared for us", "C. We fucked a lot", "D. Nothing, you suck!"],
    ["A. We don't have any", "B. Real Housewives, Football", "C. I don't like watching anything with you", "D. Survivor, Baddies, Rugby, MasterChef, From, GOT"],
    ["A. Meeeh, it's okay", "B. No I don't TF!!", "C. I want money, give money", "D. Ncoooohhh babe, it's so cute."]

]


game()


import time


delay = 5
hearts = 100

love = "\nNgiyakthanda muntu wami, HAPPY ANNIVERSARY STHANDWA SAMI.\n"

print("....................................................................................")
print("\nWait, wait let me tell you something!!")
time.sleep(delay)

print(love)

print("\U00002764" * hearts)
print("\U00002764\U0001F499\U0001F49A" * 100)


while play_again():
    game()


print("\nThank you for playing, Bye!!")
