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

# secret_number = random.randrange(0,10)
# number_of_chances = 5
# t = 0
# while t < number_of_chances:
#     guess = int(input("Enter number! "))
#     if guess == secret_number:
#         print(f"you win!, you guessed at {t} guesses & the secret number was {secret_number}")
#         break
#     elif guess > secret_number:
#         print("too high!")
#     elif guess < secret_number:
#         print("too low!")
#     t = t+1
#     if t == number_of_chances:
#         print(f"try again later!, the secret number was {secret_number}")

# import pandas as pd

# df = pd.DataFrame({"a":[1,2]})
# print(df)
# df["b"] = df["a"]+"sayantan"
# print(df)

# def break_continue_func():
#     # """print from 1-5 then ignore 6 and 7 then print 8,9,10"""
#     # for x in range(1,21):
#     #     if x>=6 and x<=10:
#     #         continue
#     #     print(x)
#     #     if x == 18:
#     #         break
#     for x in range(20):
#         if x % 2 == 0:
#             continue
#         print(x)
         

# break_continue_func()


# def read_file(file_path:str):
#     with open(file_path,"r") as f:
#         print(f.read().splitlines())

# read_file("poem.txt")

import json
import sys
# d = {"a":1}
# d.update({"a":1})
# print(d)
# print("sayantan {}".format({1}))
# sys.exit(0)

from typing import List
class Todo:
    def __init__(self) -> None:
        self.map1 = dict()

    def insert(self,*key:List[str]):
        for k in key:
            print(k)
            self.map1.update({k:True})
        # print(self.map1)
        return self.map1

    def save(self):
        content = ""
        for k in self.map1:
            print(k)
        #     record = "{}\t{}\n".format(k,v)
        #     content = content + record
        # with open("db_python.txt","w+",encoding="utf-8") as f:
        #     f.write(content)
    
if __name__ == "__main__":
    t = Todo()
    t.insert("eat rice","drink water")
    t.save()
