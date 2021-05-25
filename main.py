from cards import Card, CardDeck
from cards import CLUB, SPADE, DIAMOND, HEART

#**********************************#
# * * * Function Definitions * * * #
#**********************************#

def checksuit(cardset):

	matchfound = True
	# check if all the suits are the same
	# if list_of_cards.suit_val() == random_card.suit_val():

	# guard statement
	if len(cardset) == 0:
			return False

	# get the suit of the first card in cardset
	suitoffirst = cardset[0]  # <-- suitoffirst holds a card
	suitoffirst = suitoffirst.suit_val()  # <-- suitoffirst holds a suit value
	
	# check if each card suit @ i matches the first card
	for i in range( 1, len(cardset) ):

			suitofi = cardset [i]
			suitofi = suitofi.suit_val()

			if suitoffirst != suitofi:
				matchfound = False
		
	return matchfound   
   
def checkvalue(cardset):
  matchfound = True		
  valoffirst = cardset[0]    
  valoffirst = valoffirst.getvalue()
  for ij in range( 1, len(cardset) ):
			number = cardset [ij]
			number = number.getvalue()
			
			if valoffirst != number:
				matchfound = False  

  return matchfound

# TODO
def checkrun(cardset):
	valofirst = cardset[0]
	valofirst = valofirst.getvalue()
	for i in range( 1, len(cardset) ):
		number = cardset [i]
		number = number.getvalue()
		if number == valofirst + 1:
			matchfound = True 

  if number == valoffirst + 1:
    return

# function for printing a player hand
def printhand(cardhand):

	print("--- ", cardhand.owner, "\'s hand ---", sep="")

	if cardhand.numcards == 0:
			print("* empty *")
	else:
			print(cardhand)

	return


def printcards(cardlist):
	for card in cardlist:
		print (card)


#*********************************#
# * * * * * Driver Code * * * * * #
#*********************************#


# create the dealer with a standard deck
dealdeck = CardDeck()
dealdeck.shuffle()

# create two empty player hands as CardDeck objects
player1 = CardDeck ("player1", 0)
player2 = CardDeck ("player2", 0)

# fill each player's hand:
max_cards_in_hand = 7
for i in range (max_cards_in_hand):
  
  # player 1
  drawn = dealdeck.draw()
  player1.addtobottom ( drawn )

  # player 2
  drawn = dealdeck.draw()
  player2.addtobottom ( drawn )

player1.addtobottom (dealdeck.draw())

# display hands
printhand (player1)
# printhand (player2)

# ask player1 to select some cards from hand
mycardstocheck = input ("which cards?")

selectedcards = player1.getcards (mycardstocheck)

print ("--- player1 selected cards ---")
printcards (selectedcards)

if checksuit (selectedcards):
  print ("match")
else:
	print ("missmatch")
# if checkvalue (selectedcards):
# 	print ("match")







