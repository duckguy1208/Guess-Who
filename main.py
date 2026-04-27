import random
import streamlit as st
from character_file import opponent_choice, characters_list


# Helper functions - defined FIRST
def get_values_for_attribute(attribute):
    if attribute == "Hair Color":
        return ["", "Blonde hair", "Brown hair", "Grey hair", "Orange hair", "Bald"]
    elif attribute == "Eye Color":
        return ["", "Blue eyes", "Brown eyes", "Green eyes", "Yellow eyes"]
    elif attribute == "Accessories":
        return ["", "Glasses", "Hat"]
    elif attribute == "Gender":
        return ["", "Male", "Female"]
    elif attribute == "Species":
        return ["", "Human", "Cat", "Duck"]
    elif attribute == "Location":
        return ["", "Minnesota", "Utah", "Chicago"]
    return [""]


def get_answer(opponent, attribute, value):
    # Hair Color
    if attribute == "Hair Color":
        if value == "Blonde hair" and opponent in ["Anna", "Andie", "Alex", "George", "Violet", "Hazel", "Jade", "Gail"]:
            return "Yes"
        elif value == "Brown hair" and opponent in ["Tieler", "Steve", "Kristina", "Jake", "Rochelle", "Charlie", "Matt", "Micheal", "Mallards"]:
            return "Yes"
        elif value == "Grey hair" and opponent in ["Karen", "Roy", "GG", "Benny", "Bob", "Not Bob"]:
            return "Yes"
        elif value == "Orange hair" and opponent in ["Grace", "Bobbie"]:
            return "Yes"
        elif value == "Bald" and opponent in ["Tony", "Jon"]:
            return "Yes"
        return "No"
    
    # Eye Color
    elif attribute == "Eye Color":
        if value == "Blue eyes" and opponent in ["Anna", "Andie", "Steve", "Karen", "Jon", "Grace", "Charlie", "Roy", "Gail", "Violet", "Jade"]:
            return "Yes"
        elif value == "Brown eyes" and opponent in ["Tony", "Tieler", "Kristina", "Rochelle", "Matt", "Bob", "Not Bob", "Micheal", "Mallards"]:
            return "Yes"
        elif value == "Green eyes" and opponent in ["Alex", "Charlie", "Hazel", "Jade"]:
            return "Yes"
        elif value == "Yellow eyes" and opponent in ["Bobbie", "George", "GG", "Benny"]:
            return "Yes"
        return "No"
    
    # Accessories
    elif attribute == "Accessories":
        if value == "Glasses" and opponent in ["Anna", "Andie", "Jake", "Rochelle", "Gail", "Jade", "Matt", "Hazel"]:
            return "Yes"
        elif value == "Hat" and opponent in ["Tony", "Tieler", "Jake", "Jon", "Roy"]:
            return "Yes"
        return "No"
    
    # Gender
    elif attribute == "Gender":
        if value == "Male" and opponent in ["Tony", "Tieler", "Steve", "Jake", "Jon", "Charlie", "Roy", "Matt", "George", "Benny", "Not Bob", "Micheal", "Mallards"]:
            return "Yes"
        elif value == "Female" and opponent in ["Anna", "Andie", "Alex", "Karen", "Kristina", "Rochelle", "Grace", "Gail", "Violet", "GG", "Bobbie"]:
            return "Yes"
        return "No"
    
    # Species
    elif attribute == "Species":
        if value == "Human" and opponent in ["Anna", "Tony", "Tieler", "Andie", "Alex", "Steve", "Karen", "Kristina", "Jake", "Jon", "Rochelle", "Grace", "Charlie", "Gail", "Roy", "Jade", "Violet", "Matt", "Hazel"]:
            return "Yes"
        elif value == "Cat" and opponent in ["Bobbie", "George", "GG", "Benny"]:
            return "Yes"
        elif value == "Duck" and opponent in ["Bob", "Not Bob", "Micheal", "Mallards"]:
            return "Yes"
        return "No"
    
    # Location
    elif attribute == "Location":
        if value == "Minnesota" and opponent in ["Anna", "Tony", "Tieler", "Andie", "Alex", "Steve", "Karen", "Kristina", "Jake", "Gail", "Roy", "Bobbie", "George", "GG", "Benny", "Bob", "Not Bob", "Micheal", "Mallards"]:
            return "Yes"
        elif value == "Utah" and opponent in ["Jon", "Rochelle", "Grace", "Charlie"]:
            return "Yes"
        elif value == "Chicago" and opponent in ["Jade", "Matt", "Violet", "Hazel"]:
            return "Yes"
        return "No"

    return "Unknown"


# Initialize session state
if 'opponent_character' not in st.session_state:
    st.session_state.opponent_character = None
if 'question_count' not in st.session_state:
    st.session_state.question_count = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'last_answer' not in st.session_state:
    st.session_state.last_answer = ""
if 'question_history' not in st.session_state:
    st.session_state.question_history = []

st.title("Guess Who?")

# Rules
st.write("Welcome to Guess Who!")
st.write("Choose an attribute and value to ask a yes/no question.")
st.write("Make a guess when you think you know the answer.")

# Display character list
st.write("**Characters:** " + ", ".join(characters_list))

# New Game button
if st.button("Start New Game"):
    st.session_state.opponent_character = opponent_choice()
    st.session_state.question_count = 0
    st.session_state.game_over = False
    st.session_state.last_answer = ""
    st.session_state.question_history = []

# Display current game state
if st.session_state.opponent_character and not st.session_state.game_over:
    st.divider()
    st.subheader(f"Question #{st.session_state.question_count + 1}")
    
    opponent_choice_val = st.session_state.opponent_character
    
    # Simple dropdown-based question selection
    col1, col2 = st.columns(2)
    
    with col1:
        attribute = st.selectbox(
            "Select attribute:",
            ["", "Hair Color", "Eye Color", "Accessories", "Gender", "Species", "Location"]
        )
    
    with col2:
        value = st.selectbox(
            "Select value:",
            get_values_for_attribute(attribute)
        )
    
    # Ask Question button
    if st.button("Ask Question"):
        if not value:
            st.warning("Please select both an attribute and a value.")
        else:
            question = f"{value}?"
            answer = get_answer(opponent_choice_val, attribute, value)
            
            st.session_state.question_count += 1
            st.session_state.last_answer = answer
            st.session_state.question_history.append(f"Q{st.session_state.question_count}: {question} → {answer}")
            st.rerun()

    # Display current answer
    if st.session_state.last_answer:
        st.write(f"**Answer: {st.session_state.last_answer}**")
    
    # Display question history
    if st.session_state.question_history:
        with st.expander("Question History"):
            for q in st.session_state.question_history:
                st.write(q)

    # Guess section
    st.divider()
    st.subheader("Make a Guess")
    
    guess_col1, guess_col2 = st.columns([3, 1])
    with guess_col1:
        player_guess = st.selectbox("Select a character:", [""] + characters_list, key="guess_select")
    with guess_col2:
        st.write("")  # spacing
        st.write("")  # spacing
        submit_guess_btn = st.button("Submit Guess")
    
    if submit_guess_btn and player_guess:
        if player_guess == opponent_choice_val:
            st.session_state.last_answer = f"Correct! The character was {opponent_choice_val}. You guessed it in {st.session_state.question_count} questions!"
            st.session_state.game_over = True
        else:
            st.session_state.last_answer = f" Wrong! The character was {opponent_choice_val}. Thanks for playing!"
            st.session_state.game_over = True
        st.rerun()
    
    # End Game button
    if st.button("End Game"):
        st.session_state.last_answer = f"Game ended. The character was {opponent_choice_val}."
        st.session_state.game_over = True
        st.rerun()

elif st.session_state.game_over:
    st.success(st.session_state.last_answer)
    st.write("Click 'Start New Game' to play again!")

else:
    st.write("Click 'Start New Game' to begin!")