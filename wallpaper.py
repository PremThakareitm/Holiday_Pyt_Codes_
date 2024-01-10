import requests
import random

UNSPLASH_ACCESS_KEY = 'YOUR_UNSPLASH_ACCESS_KEY'

def get_wallpapers(category):
    api_url = 'https://api.unsplash.com/photos'
    params = {
        'client_id': UNSPLASH_ACCESS_KEY,
        'query': category,
        'orientation': 'landscape',
        'per_page': 10,
    }

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

def download_wallpaper(url, filename):
    response = requests.get(url)

    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Wallpaper downloaded: {filename}")
    else:
        print(f"Error downloading wallpaper: {response.status_code}")
        print(response.text)

def main():
    category = input("Enter the type of wallpapers you want (e.g., nature, architecture, etc.): ")

    wallpapers = get_wallpapers(category)

    if wallpapers:
        for i, wallpaper in enumerate(wallpapers):
            print(f"{i + 1}. {wallpaper['alt_description']}")

        choice = int(input("Choose a wallpaper number (1-10): ")) - 1

        if 0 <= choice < len(wallpapers):
            selected_wallpaper = wallpapers[choice]
            download_wallpaper(selected_wallpaper['urls']['full'], f"{category}_wallpaper.jpg")
        else:
            print("Invalid choice.")
    else:
        print("No wallpapers found.")

if __name__ == "__main__":
    main()
