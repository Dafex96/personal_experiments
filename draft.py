import random
import time

phrases = [
    "El auto es rojo",
    "El niño esta jugando",
    "La pelota es cuadrada"
]

phr = random.choice(phrases)

s_time = time.time()

user_phr = input(f"Escribe: {phr}\n")

e_time = time.time()

print(f"Has tardado {e_time - s_time:.2f}s")