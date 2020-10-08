'''
Här ska jag skapa själva kortleken som sedan kommer användas i 'data.py'
'''
import random


class Playingcards():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def show(self):
        print(f"{self.value} {self.suit}")


class DeckOfCards():
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for card in ["Hjärter", "Spader", "Ruter", "Klöver"]:
            for value in range(1,14):
                self.cards.append(Playingcards(card, value))
    def show(self):
        for c in self.cards:
            c.show()

    def DeckShuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    def DrawCard(self):
        return self.cards.pop()
