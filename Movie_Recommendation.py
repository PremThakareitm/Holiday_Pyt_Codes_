#GPT 
import requests

TMDB_API_KEY = 'YOUR_TMDB_API_KEY'

def get_movie_recommendations(movie_id):
    api_url = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations'
    params = {
        'api_key': TMDB_API_KEY,
        'language': 'en-US',
        'page': 1,
    }

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data['results']
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

def print_movie_info(movie):
    print(f"Title: {movie['title']}")
    print(f"Overview: {movie['overview']}")
    print(f"Release Date: {movie['release_date']}")
    print(f"Vote Average: {movie['vote_average']}")
    print("-----")

def main():
    movie_title = input("Enter the name of a movie: ")

    search_url = 'https://api.themoviedb.org/3/search/movie'
    search_params = {
        'api_key': TMDB_API_KEY,
        'query': movie_title,
        'language': 'en-US',
        'page': 1,
        'include_adult': False,
    }

    search_response = requests.get(search_url, params=search_params)

    if search_response.status_code == 200:
        search_results = search_response.json()['results']

        if not search_results:
            print("Movie not found.")
            return

        first_movie = search_results[0]
        print_movie_info(first_movie)

        recommendations = get_movie_recommendations(first_movie['id'])

        if recommendations:
            print("Recommendations:")
            for movie in recommendations:
                print_movie_info(movie)
        else:
            print("No recommendations found.")
    else:
        print(f"Error: {search_response.status_code}")
        print(search_response.text)

if __name__ == "__main__":
    main()
