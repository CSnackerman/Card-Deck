import random
from os import system

#*********************************************************
# SPECIAL ENGLISH DEFINITIONS
#	
# class		     -  a blueprint for collection of data
#
#	instantiate  -  to ⚡zap⚡ into existence...
#					          (allocate 💻memory💻 for)
#
#	object	  	 -  a class which has been instantiated
#
#	instance  	 -  a single initialized object
#
#*********************************************************


# --- CONFIGURATION ---

# console print-color ansi escape sequences
GREEN	 = 	"\u001b[32m"
BLUE	 =	"\u001b[34m"
CYAN	 =	"\u001b[0;36m"
PURPLE 	 =	"\u001b[222;35m"
RED	 	 =	"\u001b[31m"
WHITE 	 =	"\u001b[0m"

# set the primary color
COLOR = RED

# deck display settings
SHOW_CARD_NUMBER = True
DECK_PRINT_COLUMNS = 7

# debugging switches
DEBUG = False

DEBUG_CARD = True and DEBUG
DEBUG_DECK = False and DEBUG

# ---------------------


# ♠︎ ♣︎ ♥︎ ♦︎
#=========
# SUITS  █
#=========

SPADE 	=  0
CLUB 	=  1
HEART 	=  2
DIAMOND =  3

TOTAL 	=  4


#=-=-=-=-=-=-=-=-=-=|
# Utility Functions |
#	(converters)	|
#=-=-=-=-=-=-=-=-=-=|

# convert a card value into a name string 
def valuetoname(val):
	if		val == 1  :	return "A"
	elif 	val == 2  :	return "2"
	elif 	val == 3  :	return "3"
	elif 	val == 4  :	return "4"
	elif 	val == 5  :	return "5"
	elif 	val == 6  :	return "6"
	elif 	val == 7  :	return "7"
	elif 	val == 8  :	return "8"
	elif 	val == 9  :	return "9"
	elif 	val == 10 :	return "10"
	elif 	val == 11 :	return "J"
	elif 	val == 12 :	return "Q"
	elif 	val == 13 :	return "K"
	elif 	val == 14 :	return "A"
	else:
		print("invalid card value")
		return "error"


# convert a number inclusive between 0 and 3 to a suit symbol
def numbertosuit(num):
	if   num == SPADE		:	return [0, "♠︎"]
	elif num == CLUB		:	return [1, "♣︎"]
	elif num == HEART		:	return [2, "♥︎"]
	elif num == DIAMOND : return [3, "♦︎"]
	else:
		print ("invalid suit number")
		return [-1, "error"]



#  [] [] []
#===========
# CLASS 2  █
#===========
class Card:
	
	#-------------
	# Function   │ ---> object initializer/startup/setup
	#-------------
	def __init__ (self, s, v):

		# declares
		self.suit  = None
		self.name  = None
		self.value = None

		# init suit
		self.suit = numbertosuit (s) 

		# init value
		self.value = v

		# init name
		self.name = valuetoname (self.value)

		# set the card value to zero if invalid number (prevent cheating!)
		if self.getname() == "error":
			self.value = 0

		return


	#-------------
	# Function   │ ---> get string representation of this Card instance (for print)
	#-------------
	def __str__(self):
	
		n = self.getname ()
		s = self.suit_sym ()

		# debug
		if DEBUG_CARD : print ("n =", n, "s =", s)

		outputstr = COLOR

		if n == "10":
			outputstr += "┏━━┓" + "\n┃" + "1" + s + "┃"+ "\n┃" + s + "0" + "┃" + "\n┗━━┛"
		else:
			outputstr += "┏━━┓" + "\n┃" + n + s + "┃"+ "\n┃" + s + n + "┃" + "\n┗━━┛"

		return outputstr + WHITE


	#-------------
	# Function   │ ---> get the SUIT VALUE of this Card instance
	#-------------	
	def suit_val (self):
		return self.suit[0]

	#-------------
	# Function   │ ---> get the SUIT SYMBOL of this Card instance
	#-------------
	def suit_sym (self):
		return self.suit[1]

	#-------------
	# Function   │ ---> get the NAME of a Card instance
	#-------------
	def getname (self):
		return self.name

	#-------------
	# Function   │ ---> get the VALUE of a Card instance
	#-------------
	def getvalue(self):
		return self.value

	#-------------
	# Function   │ ---> randomly changes the suit & val and name
	#-------------
	def randomize (self):
		self.value = random.randint (1, 14)

		s = random.randint (0, 3)

		self.suit = numbertosuit (s)
		
		self.name = valuetoname (self.value)

		return



#  [[[[[]
#===========
# CLASS 3  █
#===========	
class CardDeck:

	#-------------
	# Function 11 │ ---> initializer/startup/setup
	#-------------
	def __init__ (self, owner="dealer", numcards=52):

		# set the owner
		self.owner = owner
		
		# init num_cards
		self.numcards = numcards

		# init card array
		self.cards = []

		cards_per_suit = int(self.numcards / TOTAL)

		for suit_val in range(TOTAL):
			for card_val in range(cards_per_suit):
				temp_card = Card(suit_val, card_val + 1)
				self.cards.append(temp_card) 

		
		# set top/bottom indices
		self.top = 0
		self.bottom = numcards - 1

		return


	#-------------
	# Function   │ ---> convert the data of this CardDeck to a string (for print)
	#-------------
	def __str__ (self):
		
		# what will be returned
		output_string = ""

		# DEBUG
		if DEBUG_DECK:
			print ("numcards =", self.numcards)	
			print ("decksize =", len(self.cards)) 
		

		# loop through every card in order to 
		# print 4 rows of characters which
		# represent the columns of cards
		for card in range(0, self.numcards, DECK_PRINT_COLUMNS):

			if card == 0:
				output_string += "top\n"

			# --- number row (0th) ---
			if SHOW_CARD_NUMBER:
				
				# make number text color white
				output_string += WHITE

				for col in range(DECK_PRINT_COLUMNS):

					# guard out of range
					if card + col >= self.numcards:
						break
					
					# add a card number label
					if (card + col) >= 10:
						output_string += " " + str (card + col) + "  "
					else:
						output_string += " " + str (card + col) + "   "


			# go to next line
			output_string += COLOR + "\n"
			

			# --- 1st row ---
			for col in range(DECK_PRINT_COLUMNS):

				# guard - out of range
				if card + col >= self.numcards:
					break

				# append to the output 
				output_string += "┏━━┓ "


			# go to next line
			output_string += "\n"


			# --- 2nd row (name row) ---
			for col in range(DECK_PRINT_COLUMNS):

				# guard - out of range
				if card + col >= self.numcards:
					break

				# get name & suit of current
				c = self.cards [card + col]
				name = c.getname()
				suit = c.suit_sym()

				# append to the output
				if name == "10":
					output_string += "┃1" + suit + "┃ "
				else:
					output_string += "┃" + name + suit + "┃ "


			# go to next line
			output_string += "\n"


			# --- 3rd row (suit row) ---
			for col in range(DECK_PRINT_COLUMNS):

				# guard - out of range
				if card + col >= self.numcards:
					break

				# get name & suit of current
				c = self.cards [card + col]
				name = c.getname()
				suit = c.suit_sym()

				# append to output
				if name == "10":
					output_string += "┃" + suit +  "0┃ "
				else:
					output_string += "┃" + suit + name + "┃ "

			
			# go to next line
			output_string += "\n"


			# --- 4th row ---
			for col in range(DECK_PRINT_COLUMNS):

				# guard - out of range
				if card + col >= self.numcards:
					break

				# append to output
				output_string += "┗━━┛ "

			# go to next line
			output_string += "\n"


		# finished building the output
		return output_string + WHITE



	#-------------
	# Function   │ ---> shuffle the CardDeck cards list
	#-------------
	def shuffle (self):

		random.shuffle (self.cards)

		return


	#-------------
	# Function   │ ---> draw a card off the top of the deck
	#-------------
	def draw (self):
		
		# store the top card in variable drawn
		drawn = self.cards [self.top]

		# delete the top card from the deck
		self.cards.pop (self.top)

		# update bottom index
		self.bottom -= 1

		# reduce number of cards in deck
		self.numcards += -1

		return drawn

	
	#-------------
	# Function   │ ---> draw a card off the top of the deck
	#-------------
	def addtobottom (self, card):

		# increase bottom index
		self.bottom += 1
		self.numcards += 1

		# add the card
		self.cards.insert (self.bottom, card)

		return

	def getlist (self):
		copy = self.cards
		return copy

	# created by Lucas Martin
	def getcards (self, selection):

		x = selection.split()

		numberlist = []
		
		
		for num in x:
			numberlist.append(self.cards[int(num)])

		return numberlist

# TEST CODE

if __name__ == "__main__":

	print ("import the cards module to use")