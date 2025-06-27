pokemons = {}
#Diccionario vacio

def menu():#definir menu
    print("MAIN MENU")
    print("1) Add Pokémon: ")
    print("2) Search Pokémon: ")
    print("3) Remove Pokémon: ")
    print("4) List Pokémon: ")
    print("5) Exit: ")

def add():#definir añadir pokemon
    pok_id = int(input("Insert Pokémon ID: "))
    pok_name = input("Insert Pokémon name: ").lower()
    pok_code = input("Insert the Pokémon code: ")
    pok_type = input("Insert Pokémon type: ")
    pokemons[pok_id] = {"name": pok_name, "type": pok_type, "code": pok_code}
    print("¡Pokemon Added!")

def search():
    pok_name = input("Insert the name of the pokemon do you want to search: ").lower()
    for pok in pokemons.values():###
        if pok["name"] == pok_name:
            print(f"Type: {pok['type']}, Code: {pok['code']}")
            return
    print("No data.")

def delete():
    pok_name = input("Insert the Pokémon you want to delete: ").lower()
    for pok_id, pok in list(pokemons.items()):
        if pok["name"] == pok_name:
            del pokemons[pok_id]
            print("Pokémon deleted")
            return
    print("No data.")

def list_all():
    print("Pokémon's: ")
    for pok_id, pok in pokemons.items():
        print(f"{pok_id}: {pok['name']}")