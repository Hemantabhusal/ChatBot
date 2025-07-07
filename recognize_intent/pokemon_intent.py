from API.pokemon_api import get_pokemon_info, initialize_pokemon_names, POKEMON_NAMES
import re

def recognize_pokemon_intent(user_input):
    """
    Detects if the user's input is related to Pokémon with minimal processing.

    Args:
        user_input (str): The input from the user.

    Returns:
        bool: True if the input is likely Pokémon-related, False otherwise.
    """
    user_input_lower = user_input.lower()

    # Quick pre-check: look for Pokémon-related trigger words or short inputs
    pokemon_triggers = {"pokemon", "pokedex", "stats", "abilities", "info"}
    words = re.findall(r"[\w-]+", user_input_lower)
    
    # Skip name checks for inputs unlikely to be Pokémon-related
    if not any(trigger in user_input_lower for trigger in pokemon_triggers) and len(words) > 5:
        return False

    # Initialize Pokémon names and check for matches
    pokemon_names = initialize_pokemon_names()
    for word in words:
        if word.capitalize() in pokemon_names:
            return True

    # Return True for generic Pokémon queries (e.g., "Pokémon info")
    return any(trigger in user_input_lower for trigger in pokemon_triggers)

def extract_pokemon_name(user_input):
    """
    Extracts the first Pokémon name from the user's input.

    Args:
        user_input (str): The input from the user.

    Returns:
        str or None: The extracted Pokémon name or None if no name is found.
    """
    pokemon_names = initialize_pokemon_names()
    user_input_lower = user_input.lower()
    words = re.findall(r"[\w-]+", user_input_lower)
    
    for word in words:
        if word.capitalize() in pokemon_names:
            return word.capitalize()
    
    return None

def handle_pokemon_intent(user_input, memory):
    """
    Handles Pokémon-related intents and logs results into memory.

    Args:
        user_input (str): The user's input.
        memory: The conversational memory object.

    Returns:
        str: The Pokémon response.
    """
    pokemon_name = extract_pokemon_name(user_input)
    if not pokemon_name:
        response = (
            "I couldn't find a Pokémon name in your query. "
            "Please specify a Pokémon, e.g., 'Tell me about Pikachu'."
        )
    else:
        response = get_pokemon_info(pokemon_name)

    memory.chat_memory.add_ai_message(response)
    return response

def process_user_input(user_input, memory):
    """
    Process user input and route to the appropriate intent handler.

    Args:
        user_input (str): The user's input.
        memory: The conversational memory object.

    Returns:
        str: The chatbot's response.
    """
    if recognize_pokemon_intent(user_input):
        return handle_pokemon_intent(user_input, memory)
    return "I'm not sure what you mean. Try asking about a Pokémon, like 'Pikachu info'!"