import cards

# create a deck of cards object
deck = cards.CardDeck()


# player_hand = [cards.Card()


# mixup the cards

deck.shuffle()

# view the deck laid out

print ("--- shuffled deck_2 ---")
print (deck)




# create an empty list called player_hand
player_hand = []

# fill the player_hand with cards using a for-loop



drawn = deck.draw()

player_hand.append(drawn)

drawn = deck.draw()


player_hand.append(drawn)

# use a for each loop to print the player_hand


print ("--- my cards ---")
for card in player_hand:
	
    print(card)

print ("--- new deck ---")
print (deck)
