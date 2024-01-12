import requests
import hashlib
import time

# Replace 'YOUR_PUBLIC_KEY' and 'YOUR_PRIVATE_KEY' with your actual Marvel API keys
MARVEL_PUBLIC_KEY = '26d1ee3961e9738009232fe4b1862cee'
MARVEL_PRIVATE_KEY = 'e90a403d54d72ec26a4e685235c180ee65aa8a26'

def get_marvel_character_info(character_name):
    timestamp = str(int(time.time()))
    hash_input = timestamp + MARVEL_PRIVATE_KEY + MARVEL_PUBLIC_KEY
    md5_hash = hashlib.md5(hash_input.encode()).hexdigest()

    api_url = f'https://gateway.marvel.com:443/v1/public/characters'
    params = {
        'name': character_name,
        'apikey': MARVEL_PUBLIC_KEY,
        'ts': timestamp,
        'hash': md5_hash
    }

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()['data']
        if data['results']:
            return data['results'][0]
        else:
            print("Character not found.")
            return None
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

def display_marvel_character_info(character_data):
    if character_data:
        print(f"Name: {character_data['name']}")
        print(f"Description: {character_data['description']}")
        print("Comics:")
        for comic in character_data['comics']['items']:
            print(f"  {comic['name']}")
        print("Series:")
        for series in character_data['series']['items']:
            print(f"  {series['name']}")
    else:
        print("Character not found.")

def main():
    character_name = input("Enter the name of the Marvel character: ")
    character_data = get_marvel_character_info(character_name)

    display_marvel_character_info(character_data)

if __name__ == "__main__":
    main()
