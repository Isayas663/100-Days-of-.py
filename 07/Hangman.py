import random
import Pixel_Art
import Word_List
import os
#from Word_List import word_list this is another way to import, and thid creates a variable from the imported program

# this is a real game bro...my first game 

word_list = ["mice","parrot","tiger","spider","fish"]
display = []
endgame = False
word = Word_List.word_list[random.randint(0,(len(word_list))-1)]
lives=6
wrong_words = ""
#another way 
#word = random.choice(word_list)

print(word)
print(Pixel_Art.hangman)
for n in range(0,len(word)):
	display += "_"

print("\t\t-----", display,"-----")
while not endgame:
	letter = input("please introduce a letter bro --> ").lower()
	os.system('clear')
	counter = 0
	if letter in display:
		print("Bro, you repeatted this letter")
	for n in range(len(word)):
		if word[n] == letter:
			display[n]=letter	
	if not letter in word:
		if letter in wrong_words:
			print("Bro, you repeatted this letter")
		else:	
			print("*****Incorrect*****")
			wrong_words += "-"
			wrong_words += 	letter
			lives -= 1 
			print(f"your reminding lives are {lives}")
			if lives == 0:
				print(Pixel_Art.lose)
				endgame = True
	if not "_" in display:
		print(Pixel_Art.win)
		endgame = True
	print(f"Wrong Words {wrong_words}")
	print(Pixel_Art.stages[lives])
	print(' '.join(display))