import cards

# create a deck of cards object
deck = cards.CardDeck()

# mixup the cards
deck.shuffle()


# view the deck laid out
print ("--- shuffled deck ---")
print (deck)

# print a spacer
print ("\n\n")

# create a single card instance
suit = cards.SPADE
mycard = cards.Card(suit, 10)
mycard.randomize()


# set the card on the console
print ("--- my card ---")
print (mycard)
