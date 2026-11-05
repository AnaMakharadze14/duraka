class GameState:
  def __init__(self, players, deck):
    self.players = players
    self.deck = deck
    self.trump_suit = None
    self.table = []

    self.attacker_index = 0
    self.defender_index = 1

    self.game_over = False
    self.winner = None


  def __str__(self):
    string = "===== GAME STATE =====\n"

    string += "Table:\n"
    for card in self.table:
        string += f"  {card}\n"

    string += "\nPlayers:\n"
    for player in self.players:
        string += f"  {player}\n"

    string += f"\nTrump suit: {self.trump_suit}\n"

    string += f"\nCards remaining: {len(self.deck.cards)}\n"

    string += "======================"


    return string