import random
from character_file import opponent_choice, characters_list
import streamlit as st

st.title("Guess Who?")

win = False
q = 0

opponent_choice = opponent_choice()

#rules
st.write("Welcome to Guess Who!")

#rules
st.write("\nTry To Guess The Opponent's Character By Asking Yes Or No Questions.")
st.write("\nYou Can Ask About Hair Color, Eye Color, Glasses, Hat, Gender, Or Species(Human Or Cat).")
st.write("\nWhen You Want To Guess The Opponent's Character, Type 'I want to guess'")
st.write("To Forfit The Game, Type 'end game'")

#print character list
st.write("Here are the characters you can choose from:")
st.write(", ".join(characters_list))

#game loop

while win == False:
    question = st.text_input("\nAsk a yes or no question about the opponent's character: ")
    q = q + 1
    #hair color questions
    #blonde hair
    if question.lower() == "do they have blonde hair?":
        if opponent_choice in ["Anna", "Andie", "Alex", "George", "Violet", "Hazel", "Jade", "Gail"]:
            st.write("Yes")
        else:
            st.write("No")
    #brown hair
    elif question.lower() == "do they have brown hair?":
        if opponent_choice in ["Tieler", "Steve", "Kristina", "Jake", "Rochelle", "Charlie", "Matt", "Micheal", "Mallards"]:
            st.write("Yes")
        else:
            st.write("No")
    #grey hair
    elif question.lower() == "do they have grey hair?":
        if opponent_choice in ["Karen", "Roy", "GG", "Benny", "Bob", "Not Bob"]:
            st.write("Yes")
        else:
            st.write("No")
    #orange hair
    elif question.lower() == "do they have orange hair?":
        if opponent_choice in ["Grace", "Bobbie"]:
            st.write("Yes")
        else:
            st.write("No")
    #no hair
    elif question.lower() == "are they bald?":
        if opponent_choice in ["Tony", "Jon"]:
            st.write("Yes")
        else:
            st.write("No")

    #eye color questions
    #blue eyes
    elif question.lower() == "do they have blue eyes?":
        if opponent_choice in ["Anna", "Andie", "Steve", "Karen", "Jon", "Grace", "Charlie", "Roy", "Gail", "Violet", "Jade"]:
            st.write("Yes")
        else:
            st.write("No")
    #brown eyes
    elif question.lower() == "do they have brown eyes?":
        if opponent_choice in ["Tony", "Tieler", "Kristina", "Rochelle", "Matt", "Bob", "Not Bob", "Micheal", "Mallards"]:
            st.write("Yes")
        else:
            st.write("No")
    #green eyes
    elif question.lower() == "do they have green eyes?":
        if opponent_choice in ["Alex", "Charlie", "Hazel", "Jade"]:
            st.write("Yes")
        else:
            st.write("No")
    #yellow eyes
    elif question.lower() == "do they have yellow eyes?":
        if opponent_choice in ["Bobbie", "George", "GG", "Benny",]:
            st.write("Yes")
        else:
            st.write("No")

    #glasses questions
    #yes glasses
    elif question.lower() == "do they wear glasses?":
        if opponent_choice in ["Anna", "Andie", "Jake", "Rochelle", "Gail", "Jade", "Matt", "Hazel"]:
            st.write("Yes")
        else:
            st.write("No")

    #hat questions
    #yes hat
    elif question.lower() == "do they wear a hat?":
        if opponent_choice in ["Tony", "Tieler", "Jake", "Jon", "Roy"]:
            st.write("Yes")
        else:
            st.write("No")

    #gender questions
    #male
    elif question.lower() == "are they male?":
        if opponent_choice in ["Tony", "Tieler", "Steve", "Jake", "Jon", "Charlie", "Roy", "Matt", "George", "Benny", "Not Bob", "Micheal", "Mallards"]:
            st.write("Yes")
        else:
            st.write("No")
    #female
    elif question.lower() == "are they female?":
        if opponent_choice in ["Anna", "Andie", "Alex", "Karen", "Kristina", "Rochelle", "Grace", "Gail", "Violet", "GG", "Bobbie"]:
            st.write("Yes")
        else:
            st.write("No")

    #species questions
    #human
    elif question.lower() == "are they human?":
        if opponent_choice in ["Anna", "Tony", "Tieler", "Andie", "Alex", "Steve", "Karen", "Kristina", "Jake", "Jon", "Rochelle", "Grace", "Charlie", "Gail", "Roy", "Jade", "Violet", "Matt", "Hazel"]:
            st.write("Yes")
        else:
            st.write("No")
    #cat
    elif question.lower() == "are they a cat?":
        if opponent_choice in ["Bobbie", "George", "Gg", "Benny"]:
            st.write("Yes")
        else:
            st.write("No")
    #duck
    elif question.lower() == "are they a duck?":
        if opponent_choice in ["Bob", "Not bob", "Micheal", "Mallards"]:
            st.write("Yes")
        else:
            st.write("No")

    elif question.lower() == "i want to guess the opponent's character" or question.lower() == "i want to guess":
        guess = st.text_input("Enter your guess: ")
        if guess.title() == opponent_choice:
            st.write("Congratulations! You guessed the opponent's character correctly!")
            st.write(f"You guessed the character in {q} questions.")
            win = True
        else:
            st.write("Sorry, that's not correct. Keep trying!")
            st.write(f"The opponent's character was {opponent_choice}. Thanks for playing!")
            win = True
    elif question.lower() == "end game":
        st.write(f"The opponent's character was {opponent_choice}. Thanks for playing!")
        break