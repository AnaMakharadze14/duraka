from .deck import Deck
from .player import Player
from .game_state import GameState


class GameController:

    def __init__(self, player_names):
        self.deck = Deck()
        self.players = []

        for name in player_names:
            self.players.append(Player(name))

        self.state = GameState(self.players, self.deck)

    def start_game(self):
        self.deck.shuffle()

        # Deal 6 cards to each player
        for player in self.players:
            cards = self.deck.draw(6)
            player.hand = cards

        # Set the trump suit
        if self.deck.cards:
            self.state.trump_suit = self.deck.cards[0].suit


        print("Game started!")
        print(self.state)
        self.game_engine()

        # self.deck.show_deck()
        

    def play_a_card(self, player):
      card = player.hand[0]

      player.remove_card(card)

      self.state.table.append(card)

      print(player.name, "played:", card)
      print(self.state)

    def game_engine(self):

      attacker = self.players[self.state.attacker_index]

      self.play_a_card(attacker)






