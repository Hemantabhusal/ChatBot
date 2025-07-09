from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env file

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER-API-KEY")
GROQ_API_KEY = os.getenv("GROQ-API-KEY")

# Groq LLM parameters
GROQ_MODEL_NAME = "llama-3.3-70b-versatile"
GROQ_MAX_TOKENS = 80
GROQ_TEMPERATURE = 0.68
SYSTEM_PROMPT = (
    "Keep your responses concise unless a detailed explanation is explicitly requested or necessary. "
    "Ask follow-up questions or provide suggestions to keep the conversation engaging and interactive. "
    "Avoid making unsolicited suggestions or asking random questions."
    "You are allowed to give me a little sarcastic text. I promise I won't get offended. "
)

# Intents and their keywords
INTENT_KEYWORDS= {
    "weather": ["weather", "forecast", "temperature", "what's the weather"],
    "open_calculator": ["calculator", "calc"],
    "open_camera": ["camera", "webcam"],
    "open_chrome": ["chrome", "browser"],
    "open_vscode": ["vscode"],
    "open_microsoft_store": ["microsoft store", "store"],
    "open_youtube": ["youtube", "videos"],
    "open_whatsapp": ["whatsapp", "messages"],
    "open_notepad": ["notepad", "editor", "text"],
    "open_word": ["word", "microsoft word", "document"],
    "open_terminal": ["terminal", "command prompt", "cmd"],
    "open_file_explorer": ["file explorer", "explorer", "my computer"],
    "open_settings": ["settings", "control panel"],
    "search_google": ["search google", "google search", "google for"],
    "open_twitter": ["twitter", "tweets", "social media"],
    "open_instagram": ["instagram", "photos", "insta"],
    "shutdown_computer": ["shutdown", "turn off computer"],
    "restart_computer": ["restart", "reboot"],
    "lock_computer": ["lock computer", "lock screen", "lock"]
}

# Actions and their associated commands
ACTION_KEYWORDS = {
    "open_calculator": ("calc.exe", "Opening calculator..."),
    "open_camera": ("start microsoft.windows.camera:", "Opening camera..."),
    "open_chrome": ("start chrome", "Opening Chrome browser..."),
    "open_vscode": ("start code", "Opening VSCode..."),
    "open_terminal": ("start cmd", "Opening terminal..."),
    "open_whatsapp": ( "start whatsapp:", "Opening Whatsapp"),
    "open_file_explorer": ("explorer", "Opening File Explorer..."),
    "open_settings": ("start ms-settings:", "Opening Settings..."),
    "open_youtube": ("start chrome https://www.youtube.com", "Opening youtube ..."),
    "search_google": ("start chrome https://www.google.com", "Opening Google for search..."),
    "open_twitter": ("start chrome https://www.twitter.com", "Opening Twitter..."),
    "open_instagram": ("start chrome https://www.instagram.com", "Opening Instagram..."),
    "shutdown_computer": ("shutdown /s /t 0", "Shutting down the computer"),
    "restart_computer": ("shutdown /r /t 0", "Restarting the computer"),
    "lock_computer": ("rundll32.exe user32.dll,LockWorkStation", "Locking the computer...")
}
