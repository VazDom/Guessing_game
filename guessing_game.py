import random
import os
os.system('cls')


def help(num_to_guess, num_try, score):
	if num_try != 0:
		if num_try < num_to_guess:
			print("you are lower. number of attempts {}".format(score))
		elif num_try > num_to_guess:
			print("you are higher. number of attempts {}".format(score))
	else:
		print("WELLCOME TO THE GAME")

def start_game():
	num_to_guess = random.randint(1, 10)
	num_try = 0
	score = 0
	print("HI")
	while num_to_guess != num_try:
		help(num_to_guess, num_try, score)
		score = score + 1
		num_try = input("tell me a number..")
		try:
			num_try = int(num_try)
			if num_try < 0 or num_try > 10:
				raise ValueError("{} is not valid. please choose a number between 1 and 10 .1 and 10 are included".format(num_try))
		except ValueError as err:
			os.system('cls')
			print("try again")
			print(err)
			start_game()

		os.system('cls')
	print("gg wp. your final score is {}".format(score))
	r = input("Would you like to play again? (y/n)")
	if r == "yes":
		os.system('cls')
		num_try = 0
		start_game()
	else:
		os.system('cls')
		print("ciao")


if __name__ == '__main__':
	start_game()