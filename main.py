import cards

# create a deck of cards object
deck = cards.CardDeck()


# mixup the cards
deck.shuffle()

# view the deck laid out
print ("--- shuffled deck ---")
print (deck)


# create an empty list called player_hand to hold cards
player_hand = []

# fill the player_hand with cards
drawn = deck.draw()
player_hand.append(drawn)
drawn = deck.draw()
player_hand.append(drawn)

# print each card in player_hand
print ("--- my cards ---")

for card in player_hand:
    print(card)

# print the updated deck
print ("--- updated deck ---")
print (deck)
