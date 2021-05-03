from cards import Card, CardDeck
from cards import CLUB, SPADE, DIAMOND, HEART

# # create a deck of cards object
# deck = cards.CardDeck()


# # mixup the cards
# deck.shuffle()

# # view the deck laid out
# #print ("--- shuffled deck ---")
# #print (deck)


# # create an empty list called player_hand to hold cards
# player_hand = []

# # fill the player_hand with cards
# drawn = deck.draw()
# player_hand.append(drawn)
# drawn = deck.draw()
# player_hand.append(drawn)
# drawn = deck.draw()
# player_hand.append(drawn)
# drawn = deck.draw()
# player_hand.append(drawn)
# drawn = deck.draw()
# player_hand.append(drawn)
# drawn = deck.draw()
# player_hand.append(drawn)
# drawn = deck.draw()
# player_hand.append(drawn)
# print ("--- my cards ---")

# for card in player_hand:
# # print each card in player_hand
#     print(card)

# # Then print the first card in deck

# use_card = []
# use_card.append(drawn)

# print (card)



# #if the suits match and if the card is one below or above 



# user_input=input(">")


# # to compare suits
# card1 = use_card [0]
# card2 = player_hand [user_input]
# if card1.suit_val() == card2.suit_val():
# 	print ("that works")







# print the updated deck
#print ("--- updated deck ---")
#print (deck)


# function for printing a player hand
def printhand (cardhand):

    

    print ("--- ", cardhand.owner, "\'s hand ---", sep="")

    if cardhand.numcards == 0:
        print ("* empty *")
    else:
        print (cardhand)

    return

# =====================================================================

# create the dealer with a standard deck
dealdeck = CardDeck()
dealdeck.shuffle()

# create two empty player hands as CardDeck objects
player1 = CardDeck ("player1", 0)
player2 = CardDeck ("player2", 0)

# print the freshly shuffled deck
print ("--- before ---")
print (dealdeck)

# fill each player's hand:
max_cards_in_hand = 7

for i in range (max_cards_in_hand):

    # player 1
    drawn = dealdeck.draw()
    player1.addtobottom ( drawn )

    # player 2
    drawn = dealdeck.draw()
    player2.addtobottom ( drawn )

# ---

# display hands
printhand (player1)
printhand (player2)

# print the dealer's deck after dealing
print ("--- after ---")
print (dealdeck)
