import random

# Card ranks and suits
suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "J", "Q", "K", "A")

# Card class
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"


# Create a deck and shuffle the cards
deck = [Card(rank, suit) for suit in suits for rank in ranks]
for card in deck:
    print(card)
random.shuffle(deck)

for card in deck:
    print(card)

# Split deck equally between 2 player after shuffling
player1_deck = deck[:26]
player2_deck = deck[26:]

def game():

    def handle_war(war_pile):
        print("⚔️ IT'S A WAR! ⚔️")

        # Check if each player has enough cards for at least one war! (4 cards)
        if len(player1_deck) < 4:
            print("Player 1 doesn't have enough cards for war! Player 2 wins!")
            player2_deck.extend(player1_deck + war_pile)
            player1_deck.clear()
            return
        elif len(player2_deck) < 4:
            print("Player 2 doesn't have enough cards for war! Player 1 wins!")
            player1_deck.extend(player2_deck + war_pile)
            player2_deck.clear()
            return

        # Draw three face-down cards + one battle card
        for _ in range(3):
            war_pile.extend([player1_deck.pop(0), player2_deck.pop(0)])

        # add the top 2 cards to the war_pile to keep track of them
        player1_card = player1_deck.pop(0)
        player2_card = player2_deck.pop(0)
        war_pile.extend([player1_card, player2_card])

        print(f"War battle: {player1_card} vs {player2_card}")

        if ranks.index(player1_card.rank) > ranks.index(player2_card.rank):
            print("Player 1 wins the war!")
            player1_deck.extend(war_pile)
        elif ranks.index(player1_card.rank) < ranks.index(player2_card.rank):
            print("Player 2 wins the war!")
            player2_deck.extend(war_pile)
        else:
            # call another war in case
            handle_war(war_pile)

    # Main game loop
    while player1_deck and player2_deck:
        player1_card = player1_deck.pop(0)
        player2_card = player2_deck.pop(0)

        print(f"{player1_card} vs {player2_card}")

        if ranks.index(player1_card.rank) > ranks.index(player2_card.rank):
            player1_deck.extend([player1_card, player2_card])
            print("Player 1 wins the round!")
        elif ranks.index(player1_card.rank) < ranks.index(player2_card.rank):
            player2_deck.extend([player1_card, player2_card])
            print("Player 2 wins the round!")
        else:
            # Call the nested function to handle the war
            handle_war([player1_card, player2_card])

    # Declare winner
    winner = "Player 1" if player1_deck else "Player 2"
    print(f"🏆 {winner} WINS THE GAME! 🏆")

# Start the game
game()
