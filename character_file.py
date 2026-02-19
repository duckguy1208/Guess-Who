import random

def character_stats():
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
    #ducks
    bob = ("grey hair", "brown eyes", "no glasses", "no hat", "female", "duck")
    notbob = ("grey hair", "brown eyes", "no glasses", "no hat", "male", "duck")
    micheal = ("brown hair", "brown eyes", "no glasses", "no hat ", "male", "duck")
    mallards = ("brown hair", "brown eyes", "no glasses", "no hat" , "female", "duck")


def opponent_choice():
    characters = ["Anna", "Tony", "Tieler", "Andie", "Alex", "Steve", "Karen", "Kristina", "Jake", "Jon", "Rochelle", "Grace", "Charlie", "Gail", "Roy", "Jade", "Matt", "Violet", "Hazel", "Bobbie", "George", "GG", "Benny", "Bob", "Not Bob", "Micheal", "Mallards"] 
    return random.choice(characters)

characters_list = ["Anna", "Tony", "Tieler", "Andie", "Alex", "Steve", "Karen", "Kristina", "Jake", "Jon", "Rochelle", "Grace", "Charlie", "Gail", "Roy", "Jade", "Matt", "Violet", "Hazel", "Bobbie", "George", "GG", "Benny", "Bob", "Not Bob", "Micheal", "Mallards"]