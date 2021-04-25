import cards


deck = cards.CardDeck()

deck.shuffle()

print (deck)

print ("\n\n")

suit = cards.Suit.DIAMOND
mycard = cards.Card(suit, 10)

print ("--- mycard ---")
print (mycard)
