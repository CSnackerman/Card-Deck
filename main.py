from cards import Card, CardDeck
from cards import CLUB, SPADE, DIAMOND, HEART
from os import system

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
			second = cardset [ij]
			second = second.getvalue()
			
			if valoffirst != second:
				matchfound = False  

  return matchfound


def checkrun(cardset):
	matchfound = True
	
	if checksuit(cardset):
		print ("the suits matched, so we move forward to check the values")
	else:
		return False

	for i in range( 1, len(cardset) ):

		first = cardset[i - 1]
		first = first.getvalue()
		
		second = cardset [i]
		second = second.getvalue()
		if second != first + 1:
			matchfound = False
		if second == first - 1:
			matchfound = True
	
	
	return matchfound

# function for printing a player hand
def printhand(cardhand):

	print("--- ", cardhand.owner, "\'s hand ---", sep="")

	if cardhand.numcards == 0:
			print("* empty *")
	else:
			print(cardhand)

	return


def printcards(cardlist):
	
	if  (cardlist) == False:
		print ("cannot print empty list\n")
		return 
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

# create the table deck
table = CardDeck ("table", 0)

# # fill each player's hand:
# max_cards_in_hand = 7
# for i in range (max_cards_in_hand):
  
# 	# player 1
# 	drawn = dealdeck.draw()
# 	player1.addtobottom ( drawn )


# 	# player 2
# 	drawn = dealdeck.draw()
# 	player2.addtobottom ( drawn )

player1.addtobottom (Card (SPADE, 2))
player1.addtobottom (Card (SPADE, 3))
player1.addtobottom (Card (SPADE, 4))
player1.addtobottom (Card (SPADE, 5))


# primary loop
while True:
	printhand (table)
	# display hands
	printhand (player1)
	printhand (player2)

	# ask player1 to select some cards from hand
	mycardstocheck = input ("which cards?")

	system ("clear")

	selectedcards = player1.getcards (mycardstocheck)

	print ("--- player1 selected cards ---")
	printcards (selectedcards)

		
	if checkrun (selectedcards):
		print ("run match")
		# remove the cards from the player hand
		player1.removecards (selectedcards)

		# place the cards on the table
		table.addcards(selectedcards)
	else:
		print ("run missmiatch")	

	# if checkvalue (selectedcards):
	# 	print ("val match")
	# else:
	# 	print ("val missmatch") 














