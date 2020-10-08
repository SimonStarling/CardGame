'''
Här ska själva logiken ske. Ta emot userinput och ge output. Ska nyttjas av main.py och hämta 'kortleken' från cards.py
'''
from pathlib import Path
from cards import *


def ViewRules():
    p = Path('CardGame', 'gamerules.txt')
    rules = p.read_text(encoding='utf8')
    return rules


def Game():
    players = input("Skriv in era namn. Ange ett kommatecken mellan varje namn: ").split()
    if len(players) <= 0:
        print("Inga namn angavs... Gör om och gör rätt!")
    elif len(players) <= 1:
        print("Inte så kul att spela själv eller? Bjud in lite folk och försök igen!")
    else:
        print(f"Spelare {players} Antal spelare {len(players)}\nNu kör vi igång!")




if __name__ == '__main__':
    Game()