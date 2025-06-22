import random

ppt = ["piedra","papel","tijera"]

maquina = random.choice(ppt)

while True:
    try:
        user = input("Elija Piedra, Papel o Tijera: ").lower()
        break
    except:
        print("Opcion ingresada no valida, intentre nuevamente.")

print(f"La maquina escogió {maquina}, tu elegiste {user}")

if maquina == user:
    print("!Empate¡")
elif maquina == "piedra" and user == "papel":
    print("!Has ganado¡")
elif maquina == "papel" and user == "piedra":
    print("!Has perdido¡")
elif maquina == "piedra" and user == "tijera":
    print("!Has perdido¡")
elif maquina == "tijera" and user == "piedra":
    print("!Has ganado¡")
elif maquina == "tijera" and user == "papel":
    print("!Has perdido¡")
elif maquina == "papel" and user == "tijera":
    print("!Has ganado¡")
else:
    print("Opcion ingresada no válida")