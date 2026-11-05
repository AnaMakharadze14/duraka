import random

from game.card import Card


class Deck:
  def __init__(self):
    self.cards = []
    suits = [ "♥️", "♦️", "♣️", "♠️"]
    ranks = ["6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    for rank in ranks:
      for suit in suits:
        self.cards.append(Card(rank, suit))

  def show_deck(self):
    print("current deck:")
    for card in self.cards:
        print(card)


  def shuffle(self):
    random.shuffle(self.cards)


  def draw(self, amount):
    drawn_cards = []

    for i in range(amount):
      if len(self.cards) > 0:
        drawn_cards.append(self.cards.pop())
      else:
        break

    return drawn_cards



