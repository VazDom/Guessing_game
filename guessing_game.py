import random
import os
os.system('cls')


def help(num_to_guess, num_try):
	if num_try != 0:
		if num_try < num_to_guess:
			print("you are lower")
		elif num_try > num_to_guess:
			print("you are higher")
	else:
		print("WELLCOME TO THE GAME")

def start_game():
	num_to_guess = random.randint(1, 10)
	num_try = 0
	print("HI")
	while num_to_guess != num_try:
		help(num_to_guess, num_try)
		num_try = input("tell me a number..")
		num_try = int(num_try)
		os.system('cls')
	print("gg wp")
	r = input("Would you like to play again? (y/n)")
	if r == "yes":
		num_try = 0
		start_game()
	else:
		os.system('cls')
		print("ciao")


if __name__ == '__main__':
	start_game()