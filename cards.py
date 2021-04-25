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

#  ♠︎ ♣︎ ♥︎ ♦︎
#===========
# CLASS 1  █
#===========
class Suit:
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
	def __init__(self, suit, value):

		# declares
		self.__suit  = None
		self.__name  = None
		self.__value = None

		# init suit
		if   suit == Suit.SPADE	  :	self.__suit = [0, "♠︎"]
		elif suit == Suit.CLUB	  :	self.__suit = [1, "♣︎"]
		elif suit == Suit.HEART	  :	self.__suit = [2, "♥︎"]
		elif suit == Suit.DIAMOND :	self.__suit = [3, "♦︎"]
		else:
			self.__suit = [-1, "error"]
			print ("invalid suit")

		# init value
		self.__value = value

		# init name
		if		self.__value == 1  :	self.__name = "A"
		elif 	self.__value == 2  :	self.__name = "2"
		elif 	self.__value == 3  :	self.__name = "3"
		elif 	self.__value == 4  :	self.__name = "4"
		elif 	self.__value == 5  :	self.__name = "5"
		elif 	self.__value == 6  :	self.__name = "6"
		elif 	self.__value == 7  :	self.__name = "7"
		elif 	self.__value == 8  :	self.__name = "8"
		elif 	self.__value == 9  :	self.__name = "9"
		elif 	self.__value == 10 :	self.__name = "10"
		elif 	self.__value == 11 :	self.__name = "J"
		elif 	self.__value == 12 :	self.__name = "Q"
		elif 	self.__value == 13 :	self.__name = "K"
		elif 	self.__value == 14 :	self.__name = "A"
		else:
			self.__value = 0
			self.__name = "error"
			print("invalid value")


	#-------------
	# Function 2 │ ---> get string representation of this Card instance (for print)
	#-------------
	def __str__(self):
		n = self.name()
		s = self.suit_sym()

		if n == "10":
			outputstr = "┍━━┑" + "\n│" + "1" + s + "│"+ "\n│" + s + "0" + "│" + "\n┕━━┙"
		else:
			outputstr = "┍━━┑" + "\n│" + n + s + "│"+ "\n│" + s + n + "│" + "\n┕━━┙"

		return outputstr

	#-------------
	# Function 3 │ ---> get the SUIT VALUE of this Card instance
	#-------------	
	def suit_val(self):
		return self.__suit[0]

	#-------------
	# Function 4 │ ---> get the SUIT SYMBOL of this Card instance
	#-------------
	def suit_sym(self):
		return self.__suit[1]

	#-------------
	# Function 5 │ ---> get the NAME of a Card instance
	#-------------
	def name(self):
		return self.__name

	#-------------
	# Function 6 │ ---> get the VALUE of a Card instance
	#-------------
	def value(self):
		return self.__value


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
		self.__numcards = numcards

		# init card array
		self.__cards = []

		cards_per_suit = int(self.__numcards / Suit.TOTAL)

		for suit_val in range(Suit.TOTAL):
			for card_val in range(cards_per_suit):
				temp_card = Card(suit_val, card_val + 1)
				self.__cards.append(temp_card) 


	#-------------
	# Function 8 │ ---> convert the data of this CardDeck to a string (for print)
	#-------------
	def __str__(self):
		
		# declarations
		output_string = ""
		columns = 9
		

		# loop through every card in order to 
		# print 4 rows of characters which
		# represent the columns of cards
		for card in range(0, self.__numcards - 1, columns):
			

			# --- 1st row ---
			for col in range(columns):

				# guard - out of range
				if card + col >= self.__numcards:
					break

				# append to the output 
				output_string += "┍━━┑ "


			# go to next line
			output_string += "\n"


			# --- 2nd row (name row) ---
			for col in range(columns):

				# guard - out of range
				if card + col >= self.__numcards:
					break

				# get name & suit of current
				c = self.__cards [card + col]
				name = c.name()
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
				if card + col >= self.__numcards:
					break

				# get name & suit of current
				c = self.__cards [card + col]
				name = c.name()
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
				if card + col >= self.__numcards:
					break

				# append to output
				output_string += "┕━━┙ "

			# go to next line
			output_string += "\n"


		# finished building the output
		return output_string



	#-------------
	# Function 9 │ ---> shuffle the CardDeck __cards list
	#-------------
	def shuffle(self):

		random.shuffle(self.__cards)



# TEST CODE

if __name__ == "__main__":
	
	deck = CardDeck()

	deck.shuffle()

	system("clear")

	print ("--- shuffle ---")
	print (deck)

	print ("\n\n")

	mycard = Card(Suit.HEART, 14)

	print (mycard)