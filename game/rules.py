class Rules:

    RANK_VALUES = {
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14
    }

    @staticmethod
    def can_beat(attack_card, defence_card, trump_suit):

      # Rule 1: Same suit
      if attack_card.suit == defence_card.suit:
          return (
              Rules.RANK_VALUES[defence_card.rank]
              > Rules.RANK_VALUES[attack_card.rank]
          )

      # Rule 2: Defence card is trump
      if defence_card.suit == trump_suit:
        return True

      # Rule 3: Cannot beat the attacking card
      return False

    @staticmethod
    def can_add_attack(attack_card, table):
      # Rule 4: Cannot add more than 6 cards to attack
      if len(table) >= 6:
        return False

      # Rule 5: attacker can only add cards of the same rank that are on the table
      table_ranks = [card.rank for card in table]
      if attack_card.rank in table_ranks:
        return True
      return False

    @staticmethod
    def can_pick_up(defender, table, trump_suit):
      for defend_card in defender.hand:
        for attack_card in table:
          if Rules.can_beat(attack_card, defend_card, trump_suit):
            return False
      return True

    @staticmethod
    def can_finish_game(players, deck):
      num_of_cards_remaining = [len(player.hand) for player in players]
      if deck.cards == [] and 0 in num_of_cards_remaining:
        return True


