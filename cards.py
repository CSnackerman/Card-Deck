import random
from os import system

#*********************************************************
# SPECIAL ENGLISH DEFINITIONS
#	
# 	class		 -  a blueprint for collection of data
#
#	instantiate  -  to ⚡zap⚡ into existence...
#					 (allocate 💻memory💻 for)
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


#  [] [] []
#===========
# CLASS 2  █
#===========
class Card:
	
	#-------------
	# Function 1 │ ---> initializer/startup/setup
	#-------------
	def __init__(self, s, v):

		# declares
		self.suit  = None
		self.name  = None
		self.value = None

		# init suit
		if   s == SPADE	  :	self.suit = [0, "♠︎"]
		elif s == CLUB	  :	self.suit = [1, "♣︎"]
		elif s == HEART	  :	self.suit = [2, "♥︎"]
		elif s == DIAMOND : self.suit = [3, "♦︎"]
		else:
			self.suit = [-1, "error"]
			print ("invalid suit")

		# init value
		self.value = v

		# init name
		if		self.value == 1  :	self.name = "A"
		elif 	self.value == 2  :	self.name = "2"
		elif 	self.value == 3  :	self.name = "3"
		elif 	self.value == 4  :	self.name = "4"
		elif 	self.value == 5  :	self.name = "5"
		elif 	self.value == 6  :	self.name = "6"
		elif 	self.value == 7  :	self.name = "7"
		elif 	self.value == 8  :	self.name = "8"
		elif 	self.value == 9  :	self.name = "9"
		elif 	self.value == 10 :	self.name = "10"
		elif 	self.value == 11 :	self.name = "J"
		elif 	self.value == 12 :	self.name = "Q"
		elif 	self.value == 13 :	self.name = "K"
		elif 	self.value == 14 :	self.name = "A"
		else:
			print("invalid value")
			self.value = 0
			self.name = "error"


	#-------------
	# Function 2 │ ---> get string representation of this Card instance (for print)
	#-------------
	def __str__(self):
		n = self.getname()
		s = self.suit_sym()

		outputstr = COLOR

		if n == "10":
			outputstr += "┍━━┑" + "\n│" + "1" + s + "│"+ "\n│" + s + "0" + "│" + "\n┕━━┙"
		else:
			outputstr += "┍━━┑" + "\n│" + n + s + "│"+ "\n│" + s + n + "│" + "\n┕━━┙"

		return WHITE + outputstr


	#-------------
	# Function 10 │ ---> randomly changes the suit & val and name
	#-------------
	def randomize(self):
		self.value = random.randint(1, 14)

		s = random.randint(0, 3)

		if   s == SPADE	  :	self.suit = [0, "♠︎"]
		elif s == CLUB	  :	self.suit = [1, "♣︎"]
		elif s == HEART	  :	self.suit = [2, "♥︎"]
		elif s == DIAMOND : self.suit = [3, "♦︎"]

		
		if		self.value == 1  :	self.name = "A"
		elif 	self.value == 2  :	self.name = "2"
		elif 	self.value == 3  :	self.name = "3"
		elif 	self.value == 4  :	self.name = "4"
		elif 	self.value == 5  :	self.name = "5"
		elif 	self.value == 6  :	self.name = "6"
		elif 	self.value == 7  :	self.name = "7"
		elif 	self.value == 8  :	self.name = "8"
		elif 	self.value == 9  :	self.name = "9"
		elif 	self.value == 10 :	self.name = "10"
		elif 	self.value == 11 :	self.name = "J"
		elif 	self.value == 12 :	self.name = "Q"
		elif 	self.value == 13 :	self.name = "K"
		elif 	self.value == 14 :	self.name = "A"


	#-------------
	# Function 3 │ ---> get the SUIT VALUE of this Card instance
	#-------------	
	def suit_val(self):
		return self.suit[0]

	#-------------
	# Function 4 │ ---> get the SUIT SYMBOL of this Card instance
	#-------------
	def suit_sym(self):
		return self.suit[1]

	#-------------
	# Function 5 │ ---> get the NAME of a Card instance
	#-------------
	def getname(self):
		return self.name

	#-------------
	# Function 6 │ ---> get the VALUE of a Card instance
	#-------------
	def value(self):
		return self.value



#  [[[[[]
#===========
# CLASS 3  █
#===========	
class CardDeck:

	#-------------
	# FUNCTION 7 │ ---> initializer/startup/setup
	#-------------
	def __init__(self, numcards=52):
		
		# init num_cards
		self.numcards = numcards

		# init card array
		self.cards = []

		cards_per_suit = int(self.numcards / TOTAL)

		for suit_val in range(TOTAL):
			for card_val in range(cards_per_suit):
				temp_card = Card(suit_val, card_val + 1)
				self.cards.append(temp_card) 


	#-------------
	# Function 8 │ ---> convert the data of this CardDeck to a string (for print)
	#-------------
	def __str__(self):
		
		# declarations
		output_string = COLOR
		columns = 7
		

		# loop through every card in order to 
		# print 4 rows of characters which
		# represent the columns of cards
		for card in range(0, self.numcards - 1, columns):
			

			# --- 1st row ---
			for col in range(columns):

				# guard - out of range
				if card + col >= self.numcards:
					break

				# append to the output 
				output_string += "┍━━┑ "


			# go to next line
			output_string += "\n"


			# --- 2nd row (name row) ---
			for col in range(columns):

				# guard - out of range
				if card + col >= self.numcards:
					break

				# get name & suit of current
				c = self.cards [card + col]
				name = c.getname()
				suit = c.suit_sym()

				# append to the output
				if name == "10":
					output_string += "│1" + suit + "│ "
				else:
					output_string += "│" + name + suit + "│ "


			# go to next line
			output_string += "\n"


			# --- 3rd row (suit row) ---
			for col in range(columns):

				# guard - out of range
				if card + col >= self.numcards:
					break

				# get name & suit of current
				c = self.cards [card + col]
				name = c.getname()
				suit = c.suit_sym()

				# append to output
				if name == "10":
					output_string += "│" + suit +  "0│ "
				else:
					output_string += "│" + suit + name + "│ "

			
			# go to next line
			output_string += "\n"


			# --- 4th row ---
			for col in range(columns):

				# guard - out of range
				if card + col >= self.numcards:
					break

				# append to output
				output_string += "┕━━┙ "

			# go to next line
			output_string += "\n"


		# finished building the output
		return output_string + WHITE



	#-------------
	# Function 9 │ ---> shuffle the CardDeck __cards list
	#-------------
	def shuffle(self):

		random.shuffle(self.cards)
		

	def draw(self):
		drawn = self.cards.pop()

		self.numcards += -1


		return drawn



# TEST CODE

if __name__ == "__main__":
	
	deck = CardDeck()

	deck.shuffle()

	system("clear")

	print ("--- shuffle ---")
	print (deck)

	print ("\n\n")

	mycard = Card(HEART, 14)

	print (mycard)