from recognize_intent.weather_intent import recognize_weather_intent, handle_weather_intent
from recognize_intent.pokemon_intent import recognize_pokemon_intent, handle_pokemon_intent
from actions.action import execute_action
from config.config import INTENT_KEYWORDS

def get_intent(user_input):
    # Check for Pokémon intent
    if recognize_pokemon_intent(user_input):
        return "pokemon", handle_pokemon_intent

    # Check for weather intent
    if recognize_weather_intent(user_input):
        return "weather", handle_weather_intent

    # Check for system-level actions
    user_input_lower = user_input.lower()
    for intent, keywords in INTENT_KEYWORDS.items():
        if any(keyword in user_input_lower for keyword in keywords):
            return intent, None

    return None, None

def handle_intent(user_input, memory):
    intent, handler = get_intent(user_input)

    if intent:
        try:
            if handler:  # Pokémon or weather intent
                response = handler(user_input, memory)
            else:  # System-level action
                response = execute_action(intent, memory)

            memory.chat_memory.add_ai_message(response)
            print(f"Eva: {response}")
            return True
        except Exception as e:
            response = f"An error occurred: {e}"
            memory.chat_memory.add_ai_message(response)
            print(f"Eva: {response}")
            return False

    return False