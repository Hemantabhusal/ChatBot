from API.pokemon_api import get_pokemon_info, initialize_pokemon_names, POKEMON_NAMES
import re

def recognize_pokemon_intent(user_input):
    user_input_lower = user_input.lower()

    # Quick pre-check: look for Pokémon-related trigger words or short inputs
    pokemon_triggers = {"pokemon", "pokedex", "stats", "abilities", "info"}
    words = re.findall(r"[\w-]+", user_input_lower)
    
    if not any(trigger in user_input_lower for trigger in pokemon_triggers) and len(words) > 5:
        return False

    pokemon_names = initialize_pokemon_names()
    for word in words:
        if word.capitalize() in pokemon_names:
            return True

    return any(trigger in user_input_lower for trigger in pokemon_triggers)

def extract_pokemon_name(user_input):
    pokemon_names = initialize_pokemon_names()
    user_input_lower = user_input.lower()
    words = re.findall(r"[\w-]+", user_input_lower)
    
    for word in words:
        if word.capitalize() in pokemon_names:
            return word.capitalize()
    
    return None

def handle_pokemon_intent(user_input, memory):
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
    if recognize_pokemon_intent(user_input):
        return handle_pokemon_intent(user_input, memory)
    return "I'm not sure what you mean. Try asking about a Pokémon, like 'Pikachu info'!"