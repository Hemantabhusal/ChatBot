from API.weather_api import get_weather
from config.config import INTENT_KEYWORDS
import re
# from utils.city_extraction import extract_city_from_input

def recognize_weather_intent(user_input):
    weather_keywords = INTENT_KEYWORDS.get("weather", [])  # Fetch weather keywords
    return any(keyword in user_input.lower() for keyword in weather_keywords)


def extract_city_from_input(user_input):
    """
    Extracts the city name from the user's input or defaults to Kathmandu.

    Args:
        user_input (str): The input from the user.

    Returns:
        str: Extracted city name or "Kathmandu" if no city is found.
    """
    city_pattern = re.compile(r"\b(?:in|at|on|of|for|about|near|to)\s+([\w\s]+)", re.IGNORECASE)
    match = city_pattern.search(user_input)
    if match:
        city = match.group(1).strip()
        return city.capitalize()
    return "Kathmandu"

def handle_weather_intent(user_input, memory):
    """
    Fetches weather information and logs it in memory.

    Args:
        user_input (str): The user's input.
        memory: The conversational memory object.

    Returns:
        str: The weather response.
    """
    # Extract city from input
    city = extract_city_from_input(user_input) or "Kathmandu"  # Default to Kathmandu
    response = get_weather(city)

    # Log the weather response in memory
    memory.chat_memory.add_ai_message(response)

    return response