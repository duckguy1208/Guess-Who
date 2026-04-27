import random

def character_stats():
    #character attributes:
    #genesee ave
    anna = ("blonde hair", "blue eyes", "glasses", "no hat", "female", "human", "minnesota")
    tony = ("bald", "brown eyes", "no glasses", "hat", "male", "human", "minnesota")
    tieler = ("brown hair", "brown eyes", "no glasses", "hat", "male", "human", "minnesota")
    andie = ("blonde hair", "blue eyes", "glasses", "no hat", "female", "human", "minnesota")
    alex = ("blonde hair", "green eyes", "no glasses", "no hat", "female", "human", "minnesota")
    #gage ave
    steve = ("brown hair", "blue eyes", "no glasses", "no hat", "male", "human", "minnesota")
    karen = ("grey hair", "blue eyes", "no glasses", "no hat", "female", "human", "minnesota")
    kristina = ("brown hair", "brown eyes", "no glasses", "no hat", "female", "human", "minnesota")
    jake = ("brown hair", "blue eyes", "glasses", "hat", "male", "human", "minnesota")
    #utah
    jon = ("bald", "blue eyes", "no glasses", "hat", "male", "human", "utah")
    rochelle = ("brown hair", "brown eyes", "glasses", "no hat", "female", "human", "utah")
    grace = ("orange hair", "blue eyes", "no glasses", "no hat", "female", "human", "utah")
    charlie = ("brown hair", "green eyes", "no glasses", "no hat", "male", "human", "utah")
    #sauk
    gail = ("blonde hair", "brown eyes", "glasses", "no hat", "female", "human", "minnesota")
    roy = ("grey hair", "blue eyes", "no glasses", "hat", "male", "human", "minnesota")
    #chicago
    jade = ("grey hair", "green eyes", "glasses", "no hat", "female", "human", "chicago")  
    matt = ("brown hair", "brown eyes", "glasses", "no hat", "male", "human", "chicago")
    violet = ("blonde hair", "blue eyes", "no glasses", "no hat", "female", "human", "chicago")
    hazel = ("blonde hair", "green eyes", "glasses", "no hat", "female", "human", "chicago")
    #cats
    bobbie = ("orange hair", "yellow eyes", "no glasses", "no hat", "female", "cat", "minnesota")
    george = ("blonde hair", "yellow eyes", "no glasses", "no hat", "male", "cat", "minnesota")
    gg = ("grey hair", "yellow eyes", "no glasses", "no hat", "female", "cat", "minnesota")
    benny = ("grey hair", "yellow eyes", "no glasses", "no hat", "male", "cat", "minnesota")
    #ducks
    bob = ("grey hair", "brown eyes", "no glasses", "no hat", "female", "duck", "minnesota")
    notbob = ("grey hair", "brown eyes", "no glasses", "no hat", "male", "duck", "minnesota")
    micheal = ("brown hair", "brown eyes", "no glasses", "no hat", "male", "duck", "minnesota")
    mallards = ("brown hair", "brown eyes", "no glasses", "no hat", "female", "duck", "minnesota")


def opponent_choice():
    characters = ["Anna", "Tony", "Tieler", "Andie", "Alex", "Steve", "Karen", "Kristina", "Jake", "Jon", "Rochelle", "Grace", "Charlie", "Gail", "Roy", "Jade", "Matt", "Violet", "Hazel", "Bobbie", "George", "GG", "Benny", "Bob", "Not Bob", "Micheal", "The Mallards"] 
    return random.choice(characters)

characters_list = ["Anna", " Tony", " Tieler", " Andie", " Alex", " Steve", " Karen", " Kristina", " Jake", " Jon", " Rochelle", " Grace", " Charlie", " Gail", " Roy", " Jade", " Matt", " Violet", " Hazel", " Bobbie", " George", " GG", " Benny", " Bob", " Not Bob", " Micheal", " The Mallards"]