import random

# def number_guessing_game():
#     number = random.randint(1, 10)
#     number_of_guesses = 0
#     while number_of_guesses < 5:
#         guess = int(input("Enter you number here "))
#         if guess < number:
#             print('Your guess is too low.')
#         elif guess > number:
#             print('Your guess is too high.')
#         else:
#             break
#         number_of_guesses += 1

#     print(f"you have guessed the number {guess}")
#     if guess == number:
#         print('Congratulations, ' + 'You guessed the number in ' + str(number_of_guesses) + ' tries!')
#     else:
#         print('Sorry, ' + 'you did not guess the number. The number was ' + str(number))

# number_guessing_game()

secret_number = random.randrange(0,10)
number_of_chances = 5
t = 0
while t < number_of_chances:
    guess = int(input("Enter number! "))
    if guess == secret_number:
        print(f"you win!, you guessed at {t} guesses & the secret number was {secret_number}")
        break
    elif guess > secret_number:
        print("too high!")
    elif guess < secret_number:
        print("too low!")
    t = t+1
    if t == number_of_chances:
        print(f"try again later!, the secret number was {secret_number}")
