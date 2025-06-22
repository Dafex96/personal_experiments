import random
import time

phrases = [
    "The car is red",
    "The kid is playing",
    "The ball is square",
    "CR7 is the goat"
]

phr = random.choice(phrases)

s_time = time.time()

user_phr = input(f"Type this phrase: {phr}\n")

if user_phr == phr:
    print("¡You are correct!")
else:
    print("¡You misspelled something!")

e_time = time.time()

print(f"¡It took you {e_time - s_time:.2f}s!")