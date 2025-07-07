import requests

BASE_URL = "https://pokeapi.co/api/v2"

# Global in-memory cache for Pokémon names
POKEMON_NAMES = None

def initialize_pokemon_names():
    """
    Fetch all Pokémon names from the API and store in memory.

    Returns:
        set: Set of Pokémon names, or empty set on failure.
    """
    global POKEMON_NAMES
    if POKEMON_NAMES is not None:
        return POKEMON_NAMES

    url = f"{BASE_URL}/pokemon?limit=2000"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        POKEMON_NAMES = {pokemon["name"].capitalize() for pokemon in data["results"]}
        return POKEMON_NAMES
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch Pokémon names: {e}")
        return set()

def get_pokemon_info(pokemon_name):
    """
    Fetch and return information about a Pokémon by name.

    Args:
        pokemon_name (str): Name of the Pokémon (e.g., 'pikachu').

    Returns:
        str: Pokémon details or an error message.
    """
    endpoint = f"/pokemon/{pokemon_name.lower()}"
    url = BASE_URL + endpoint

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        name = data["name"].capitalize()
        id_ = data["id"]
        height = data["height"]
        weight = data["weight"]
        abilities = [ability["ability"]["name"] for ability in data["abilities"]]

        details = (
            f"Pokémon Name: {name}\n"
            f"Pokédex ID: {id_}\n"
            f"Height: {height} decimetres\n"
            f"Weight: {weight} hectograms\n"
            f"Abilities: {', '.join(abilities)}"
        )
        return details

    except requests.exceptions.HTTPError:
        return f"Error: Pokémon '{pokemon_name}' not found."
    except Exception as e:
        return f"An error occurred: {e}"