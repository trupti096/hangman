import random
def hangman( ):
	list_of_words=["india","hangman","education"]
	word=random.choice(list_of_words)
	turns=10
	guessmade=" "
	a=set("abcdefghijklmnopqrstuvwxyz")
	while True:
		main_word=0
		missed=0
		for letter in word:
			if letter in guessmade:
				main_word=main_word+letter
			# else:p\
				# main_word=main_word+"_"
		if main_word==word:
			print(main_word)
			print("you win!!!!")
			break
			print("guess the words",main_word)
		guess=input()
		if guess in a:
			guess=guessmade+guess
		else:
			print("enter valid character")
			guess=input()
		if guess not in word:
			turns=turns-1
			if turns==9:
				print("9 turns left!!!")
				print("__")
			if turns==8:
				print("8 turns left!!!")
				print("__")
				print("    o    ")
			if turns==7:
				print("7 turns left!!!")
				print("__")
				print("    o    ")
				print("    |    ")
			if turns==6:
				print("6 turns left!!!")
				print("__")
				print("    o    ")
				print("    |    ")
				print("   /      ")
			if turns==5:
				print("5 turns left!!!")
				print("__")
				print("    o    ")
				print("    |    ")
				print("   / \    ")
			if turns==4:
				print("4 turns left!!!")
				print("__")
				print("   \o    ")
				print("    |    ")
				print("   / \    ")
			if turns==3:
				print("3 turns left!!!")
				print("__")
				print("   \o/    ")
				print("    |    ")
				print("   / \    ")
			if turns==2:
				print("2 turns left!!!")
				print("__")
				print("   \o/ | ")
				print("    |    ")
				print("   / \   ")
			if turns==1:
				print("only 1 turns left!!! hangman on his last breath")
				print("__")
				print("   \o/_| ")
				print("    |    ")
				print("   / \   ")
			if turns==0:
				print("you loose")
				print("you let a gud man die")
name=input("enter your name:")
print("welcome",name,"!")
print("****")
print("try to guess the word in less than 10 attempts")
hangman()