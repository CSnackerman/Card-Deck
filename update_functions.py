# open the cards.py file
cards_file = open("cards.py", "r")

# read the file into a string
cards_string = cards_file.read ()

# close the file after reading
cards_file.close()

#convert the string to a list
cards_string_list = list (cards_string)

sentinel = 0
counter = 0
while sentinel != -1:
	
	# update the counter
	counter += 1

	# move the sentinel 
	sentinel = cards_string.find("# Function ", sentinel)
	
	# delete the occurence
	cards_string = cards_string.replace("# Function ", "$r$e$p$l$a$c$e$d$", 1)

	# create replacement string
	replacement = "# Function " + str(counter) + " "

	# insert the replacement string
	for i in range ( len (replacement) ):
		cards_string_list [sentinel + i] = replacement [i]

# convert list back to string
new_file_string = ""
for c in cards_string_list:
	new_file_string += c

# overwrite the file
