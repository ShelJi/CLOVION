import requests
from icecream import ic

# name = str(input("Enter pokemon name: "))
# url = f"https://pokeapi.co/api/v2/pokemon/{name}"
# response = requests.get(url)

# ic(response.json())

print(requests.get(f"https://pokeapi.co/api/v2/pokemon/{str(input("Enter Pokemon name: ").lower())}").json()[str(input("Enter what to know example 'name', 'rarity', 'moves' : ").strip())])
