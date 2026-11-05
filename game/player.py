class Player:
  def __init__(self, name):
    self.name = name
    self.hand = []

  def add_card(self, card):
    self.hand.append(card)

  def remove_card(self, card):
    if card in self.hand:
        self.hand.remove(card)


  def __str__(self):
    return f"{self.name}: {self.hand}"
