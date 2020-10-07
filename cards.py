'''
Här ska jag skapa själva kortleken som sedan kommer användas i 'data.py'
'''

class Playingcards():
    def __init__(self, suit, value):
        self.value = value
        self.suit = suit

    def show(self):
        print(f"{} av {}".format(self.value, self.suit))

class DeckOfCards():
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for c in ["Hjärter", "Spader", "Ruter", "Klöver"]: