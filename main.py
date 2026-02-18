import random

from character_file import opponent_choice, characters_list

win = False
q = 0

opponent_choice = opponent_choice()

#rules
print("Welcome to Guess Who!")

#rules
print("\nTry To Guess The Opponent's Character By Asking Yes Or No Questions.")
print("\nYou Can Ask About Hair Color, Eye Color, Glasses, Hat, Gender, Or Species(Human Or Cat).")
print("\nWhen You Want To Guess The Opponent's Character, Type 'I want to guess'")
print("To Forfit The Game, Type 'end game'")

#print character list
print("Here are the characters you can choose from:")
print(", ".join(characters_list))

#game loop

while win == False:
    question = input("\nAsk a yes or no question about the opponent's character: ")
    q = q + 1
    #hair color questions
    #blonde hair
    if question.lower() == "do they have blonde hair?":
        if opponent_choice in ["Anna", "Andie", "Alex", "George", "Violet", "Hazel", "Jade", "Gail"]:
            print("Yes")
        else:
            print("No")
    #brown hair
    elif question.lower() == "do they have brown hair?":
        if opponent_choice in ["Tieler", "Steve", "Kristina", "Jake", "Rochelle", "Charlie", "Matt"]:
            print("Yes")
        else:
            print("No")
    #grey hair
    elif question.lower() == "do they have grey hair?":
        if opponent_choice in ["Karen", "Roy", "GG", "Benny"]:
            print("Yes")
        else:
            print("No")
    #orange hair
    elif question.lower() == "do they have orange hair?":
        if opponent_choice in ["Grace", "Bobbie"]:
            print("Yes")
        else:
            print("No")
    #no hair
    elif question.lower() == "are they bald?":
        if opponent_choice in ["Tony", "Jon"]:
            print("Yes")
        else:
            print("No")

    #eye color questions
    #blue eyes
    elif question.lower() == "do they have blue eyes?":
        if opponent_choice in ["Anna", "Andie", "Steve", "Karen", "Jon", "Grace", "Charlie", "Roy", "Gail", "Violet", "Jade"]:
            print("Yes")
        else:
            print("No")
    #brown eyes
    elif question.lower() == "do they have brown eyes?":
        if opponent_choice in ["Tony", "Tieler", "Kristina", "Rochelle", "Matt"]:
            print("Yes")
        else:
            print("No")
    #green eyes
    elif question.lower() == "do they have green eyes?":
        if opponent_choice in ["Alex", "Charlie", "Hazel", "Jade"]:
            print("Yes")
        else:
            print("No")
    #yellow eyes
    elif question.lower() == "do they have yellow eyes?":
        if opponent_choice in ["Bobbie", "George", "GG", "Benny"]:
            print("Yes")
        else:
            print("No")

    #glasses questions
    #yes glasses
    elif question.lower() == "do they wear glasses?":
        if opponent_choice in ["Anna", "Andie", "Jake", "Rochelle", "Gail", "Jade", "Matt", "Hazel"]:
            print("Yes")
        else:
            print("No")

    #hat questions
    #yes hat
    elif question.lower() == "do they wear a hat?":
        if opponent_choice in ["Tony", "Tieler", "Jake", "Jon", "Roy"]:
            print("Yes")
        else:
            print("No")

    #gender questions
    #male
    elif question.lower() == "are they male?":
        if opponent_choice in ["Tony", "Tieler", "Steve", "Jake", "Jon", "Charlie", "Roy", "Matt", "George", "Benny"]:
            print("Yes")
        else:
            print("No")
    #female
    elif question.lower() == "are they female?":
        if opponent_choice in ["Anna", "Andie", "Alex", "Karen", "Kristina", "Rochelle", "Grace", "Gail", "Jade", "Violet", "Hazel", "GG", "Bobbie"]:
            print("Yes")
        else:
            print("No")

    #species questions
    #human
    elif question.lower() == "are they human?":
        if opponent_choice in ["Anna", "Tony", "Tieler", "Andie", "Alex", "Steve", "Karen", "Kristina", "Jake", "Jon", "Rochelle", "Grace", "Charlie", "Gail", "Roy", "Jade", "Violet", "Matt", "Hazel"]:
            print("Yes")
        else:
            print("No")
    #cat
    elif question.lower() == "are they a cat?":
        if opponent_choice in ["Bobbie", "George", "Gg", "Benny"]:
            print("Yes")
        else:
            print("No")

    elif question.lower() == "i want to guess the opponent's character" or question.lower() == "i want to guess":
        guess = input("Enter your guess: ")
        if guess.title() == opponent_choice:
            print("Congratulations! You guessed the opponent's character correctly!")
            print(f"You guessed the character in {q} questions.")
            win = True
        else:
            print("Sorry, that's not correct. Keep trying!")
    elif question.lower() == "end game":
        print(f"The opponent's character was {opponent_choice}. Thanks for playing!")
        break