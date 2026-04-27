import random
import streamlit as st
from character_file import opponent_choice, characters_list

# Initialize session state
if 'opponent_character' not in st.session_state:
    st.session_state.opponent_character = None
if 'question_count' not in st.session_state:
    st.session_state.question_count = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'message' not in st.session_state:
    st.session_state.message = ""
if 'last_answer' not in st.session_state:
    st.session_state.last_answer = ""

st.title("Guess Who?")

# Rules
st.write("Welcome to Guess Who!")
st.write("Try to guess the opponent's character by asking yes or no questions.")
st.write("You can ask about hair color, eye color, glasses, hat, gender, or species (human, cat, or duck).")
st.write("When you want to guess the opponent's character, type 'I want to guess'")
st.write("To forfeit the game, type 'end game'")

# Display character list
st.write("Here are the characters you can choose from:")
st.write(", ".join(characters_list))

# New Game button
if st.button("Start New Game"):
    st.session_state.opponent_character = opponent_choice()
    st.session_state.question_count = 0
    st.session_state.game_over = False
    st.session_state.message = "New game started! Ask your first question."
    st.session_state.last_answer = ""

# Display current game state
if st.session_state.opponent_character and not st.session_state.game_over:
    st.divider()
    st.subheader(f"Question #{st.session_state.question_count}")
    
    # Question input
    question = st.text_input("Ask a yes or no question about the opponent's character:", key="question_input")
    
    col1, col2 = st.columns([1, 4])
    with col1:
        submit_btn = st.button("Submit Question")
    
    if submit_btn and question:
        question_lower = question.lower()
        opponent_choice_val = st.session_state.opponent_character
        
        st.session_state.question_count += 1
        answer = None
        
        # Hair color questions
        if "blonde hair" in question_lower:
            answer = "Yes" if opponent_choice_val in ["Anna", "Andie", "Alex", "George", "Violet", "Hazel", "Jade", "Gail"] else "No"
        elif "brown hair" in question_lower:
            answer = "Yes" if opponent_choice_val in ["Tieler", "Steve", "Kristina", "Jake", "Rochelle", "Charlie", "Matt", "Micheal", "Mallards"] else "No"
        elif "grey hair" in question_lower:
            answer = "Yes" if opponent_choice_val in ["Karen", "Roy", "GG", "Benny", "Bob", "Not Bob"] else "No"
        elif "orange hair" in question_lower:
            answer = "Yes" if opponent_choice_val in ["Grace", "Bobbie"] else "No"
        elif "bald" in question_lower:
            answer = "Yes" if opponent_choice_val in ["Tony", "Jon"] else "No"
        
        # Eye color questions
        elif "blue eyes" in question_lower:
            answer = "Yes" if opponent_choice_val in ["Anna", "Andie", "Steve", "Karen", "Jon", "Grace", "Charlie", "Roy", "Gail", "Violet", "Jade"] else "No"
        elif "brown eyes" in question_lower:
            answer = "Yes" if opponent_choice_val in ["Tony", "Tieler", "Kristina", "Rochelle", "Matt", "Bob", "Not Bob", "Micheal", "Mallards"] else "No"
        elif "green eyes" in question_lower:
            answer = "Yes" if opponent_choice_val in ["Alex", "Charlie", "Hazel", "Jade"] else "No"
        elif "yellow eyes" in question_lower:
            answer = "Yes" if opponent_choice_val in ["Bobbie", "George", "GG", "Benny"] else "No"
        
        # Glasses questions
        elif "glasses" in question_lower:
            answer = "Yes" if opponent_choice_val in ["Anna", "Andie", "Jake", "Rochelle", "Gail", "Jade", "Matt", "Hazel"] else "No"
        
        # Hat questions
        elif "hat" in question_lower:
            answer = "Yes" if opponent_choice_val in ["Tony", "Tieler", "Jake", "Jon", "Roy"] else "No"
        
        # Gender questions
        elif "male" in question_lower:
            answer = "Yes" if opponent_choice_val in ["Tony", "Tieler", "Steve", "Jake", "Jon", "Charlie", "Roy", "Matt", "George", "Benny", "Not Bob", "Micheal", "Mallards"] else "No"
        elif "female" in question_lower:
            answer = "Yes" if opponent_choice_val in ["Anna", "Andie", "Alex", "Karen", "Kristina", "Rochelle", "Grace", "Gail", "Violet", "GG", "Bobbie"] else "No"
        
        # Species questions
        elif "human" in question_lower:
            answer = "Yes" if opponent_choice_val in ["Anna", "Tony", "Tieler", "Andie", "Alex", "Steve", "Karen", "Kristina", "Jake", "Jon", "Rochelle", "Grace", "Charlie", "Gail", "Roy", "Jade", "Violet", "Matt", "Hazel"] else "No"
        elif "cat" in question_lower:
            answer = "Yes" if opponent_choice_val in ["Bobbie", "George", "GG", "Benny"] else "No"
        elif "duck" in question_lower:
            answer = "Yes" if opponent_choice_val in ["Bob", "Not Bob", "Micheal", "Mallards"] else "No"
        
        # Guess handling
        elif "guess" in question_lower:
            guess = st.text_input("Enter your guess:", key="guess_input")
            if st.button("Submit Guess"):
                if guess.title() == opponent_choice_val:
                    st.session_state.message = f"🎉 Congratulations! You guessed the opponent's character correctly!"
                    st.session_state.last_answer = f"The character was {opponent_choice_val}. You guessed it in {st.session_state.question_count} questions!"
                    st.session_state.game_over = True
                else:
                    st.session_state.message = f"❌ Sorry, that's not correct."
                    st.session_state.last_answer = f"The opponent's character was {opponent_choice_val}. Thanks for playing!"
                    st.session_state.game_over = True
            answer = "Make your guess above"
        
        # End game
        elif "end game" in question_lower:
            st.session_state.message = f"Game ended. The opponent's character was {opponent_choice_val}."
            st.session_state.last_answer = "Thanks for playing!"
            st.session_state.game_over = True
        
        else:
            answer = "I don't understand that question. Try asking about hair color, eye color, glasses, hat, gender, or species."
        
        if answer and answer != "Make your guess above":
            st.session_state.last_answer = answer
            st.session_state.message = f"You asked: {question}"

    # Display message
    if st.session_state.message:
        st.info(st.session_state.message)
    if st.session_state.last_answer:
        st.write(f"**Answer: {st.session_state.last_answer}**")

elif st.session_state.game_over:
    st.success(st.session_state.message if st.session_state.message else st.session_state.last_answer)
    st.write("Click 'Start New Game' to play again!")

else:
    st.write("Click 'Start New Game' to begin!")
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