import random

#character attributes:
#genesee ave
anna = ("blonde hair", "blue eyes", "glasses", "no hat", "female", "human")
tony = ("bald", "brown eyes", "no glasses", "hat", "male", "human")
tieler = ("brown hair", "brown eyes", "no glasses", "hat", "male", "human")
andie = ("blonde hair", "blue eyes", "glasses", "no hat", "female", "human")
alex = ("blonde hair", "green eyes", "no glasses", "no hat", "female", "human")
#gage ave
steve = ("brown hair", "blue eyes", "no glasses", "no hat", "male", "human")
karen = ("grey hair", "blue eyes", "no glasses", "no hat", "female", "human")
kristina = ("brown hair", "brown eyes", "no glasses", "no hat", "female", "human")
jake = ("brown hair", "blue eyes", "glasses", "hat", "male", "human")
#utah
jon = ("bald", "blue eyes", "no glasses", "hat", "male", "human")
rochelle = ("brown hair", "brown eyes", "glasses", "no hat", "female", "human")
grace = ("orange hair", "blue eyes", "no glasses", "no hat", "female", "human")
charlie = ("brown hair", "green eyes", "no glasses", "no hat", "male", "human")
#sauk
gail = ("blonde hair", "brown eyes", "glasses", "no hat", "female", "human")
roy = ("grey hair", "blue eyes", "no glasses", "hat", "male", "human")
#chicago
jade = ("grey hair", "green eyes", "glasses", "no hat", "female", "human")
matt = ("brown hair", "brown eyes", "glasses", "no hat", "male", "human")
violet = ("blonde hair", "blue eyes", "no glasses", "no hat", "female", "human")
hazel = ("blonde hair", "green eyes", "glasses", "no hat", "female", "human")
#cats
bobbie = ("orange hair", "yellow eyes", "no glasses", "no hat", "female", "cat")
george = ("blonde hair", "yellow eyes", "no glasses", "no hat", "male", "cat")
gg = ("grey hair", "yellow eyes", "no glasses", "no hat", "female", "cat")
benny = ("grey hair", "yellow eyes", "no glasses", "no hat", "male", "cat")

#listing characters
characters = ["Anna", "Tony", "Tieler", "Andie", "Alex", "Steve", "Karen", "Kristina", "Jake", "Jon", "Rochelle", "Grace", "Charlie", "Gail", "Roy", "Bobbie", "George", "GG", "Benny"]    
opponent_choice = random.choice(characters)

win = False

#rules
print("Welcome to Guess Who!")
print("Here are the characters you can choose from:")
for character in characters:
    print(character, end=", ")
print("\nTry to guess the opponent's character by asking yes or no questions.")
print("\nYou can ask about hair color, eye color, glasses, hat, gender, or species(human or cat).")
print("When You Want To Guess The Opponent's Character, Type 'I want to guess'")

#game loop

while win == False:
    question = input("Ask a yes or no question about the opponent's character: ")

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
        if opponent_choice in ["Karen", "Gail", "Roy", "GG", "Benny"]:
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
        if opponent_choice in ["Anna", "Andie", "Alex", "Karen", "Kristina", "Rochelle", "Grace", "Gail", "Violet", "GG", "Bobbie"]:
            print("Yes")
        else:
            print("No")

    #species questions
    #human
    elif question.lower() == "are they human?":
        if opponent_choice in ["Anna", "Tony", "Tieler", "Andie", "Alex", "Steve", "Karen", "Kristina", "Jake", "Jon", "Rochelle", "Grace", "Charlie", "Gail", "Roy", "Violet", "Matt", "Hazel"]:
            print("Yes")
        else:
            print("No")
    #cat
    elif question.lower() == "are they a cat?":
        if opponent_choice in ["Bobbie", "George", "GG", "Benny"]:
            print("Yes")
        else:
            print("No")

    elif question.lower() == "i want to guess the opponent's character" or question.lower() == "i want to guess":
        guess = input("Enter your guess: ")
        if guess.title() == opponent_choice:
            print("Congratulations! You guessed the opponent's character correctly!")
            win = True     
        else:
            print("Sorry, that's not correct. Keep trying!")
        