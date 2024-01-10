import requests

def get_pokemon_info(pokemon_name):
    api_url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'
    response = requests.get(api_url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

def display_pokemon_info(pokemon_data):
    if pokemon_data:
        print(f"Name: {pokemon_data['name'].capitalize()}")
        print(f"ID: {pokemon_data['id']}")
        print("Types:", ", ".join([type['type']['name'] for type in pokemon_data['types']]))
        print("Abilities:", ", ".join([ability['ability']['name'] for ability in pokemon_data['abilities']]))
        print("Stats:")
        for stat in pokemon_data['stats']:
            print(f"  {stat['stat']['name'].capitalize()}: {stat['base_stat']}")
    else:
        print("Pokemon not found.")

def main():
    pokemon_name = input("Enter the name of the Pokemon: ")
    pokemon_data = get_pokemon_info(pokemon_name)

    display_pokemon_info(pokemon_data)

if __name__ == "__main__":
    main()
