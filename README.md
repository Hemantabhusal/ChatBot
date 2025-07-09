# 🤖 ChatBot Project

A conversational AI chatbot built with **Python**, powered by the **Groq LLaMA 3.3-70B-versatile model**, and designed for interactive natural language communication. This bot handles external API queries (like weather or Pokémon data), maintains conversation memory, and performs local system commands such as launching applications, shutting down the computer and many mores!!

---

## 🚀 Features

- 🧠 **NLP Intelligence:** Generates intelligent, natural responses using **Groq API** (LLaMA-70B model)
- 🌦️ **Weather Queries:** Uses the **OpenWeather API** to provide real-time weather information
- 🐾 **Pokémon Info:** Fetches Pokémon data from a custom Pokémon API
- 💻 **System Automation:** Supports commands to open apps (`Chrome`, `VSCode`, `Calculator`) and control system power (`shutdown`, `restart`, `lock`)
- 🧠 **Memory Retention:** Maintains context using **LangChain's `ConversationBufferWindowMemory`** (5-message history)
- 🔐 **Secure Configs:** Uses `.env` for secure environment variable management
- 🔧 **Customizable:** Fully modular and configurable via `config.py`

---

## 🧰 Tech Stack

- **Python 3.x** – Core language
- **LangChain** – For context-aware conversation and memory management
- **Groq API** – Access to the LLaMA-3.3-70B-versatile language model
- **OpenWeather API** – Weather data via RESTful API
- **Custom Pokémon API** – Bespoke endpoint for Pokémon-related queries
- **dotenv** – Loads environment variables from `.env`
- **os / subprocess** – Executes local system commands

---

## 📚 What I Learned

- 🔌 API Integration: How to connect, authenticate, and parse data from real-world APIs
- 🧠 NLP Engineering: Leveraging large language models for dialog applications
- 🧮 Memory & Context: Implementing LangChain memory tools for short-term retention
- ⚙️ System Programming: Interacting with the OS to launch apps and manage system power
- 🗂️ Modular Architecture: Structuring scalable projects using packages and utilities
- 🛡️ Error Handling: Debugging third-party libraries, APIs, and system commands

---

## 📦 Prerequisites

- Python 3.6 or higher
- Required dependencies listed in `requirements.txt`

---

## 🧾 requirements.txt

Below is the full list of dependencies used in this project:

```text
annotated-types==0.7.0
anyio==4.9.0
certifi==2025.1.31
charset-normalizer==3.4.1
click==8.1.8
colorama==0.4.6
comtypes==1.4.10
distro==1.9.0
greenlet==3.1.1
groq==0.20.0
gTTS==2.5.4
h11==0.14.0
httpcore==1.0.7
httpx==0.28.1
idna==3.10
jsonpatch==1.33
jsonpointer==3.0.0
langchain==0.3.21
langchain-core==0.3.49
langchain-groq==0.3.1
langchain-text-splitters==0.3.7
langsmith==0.3.19
orjson==3.10.16
packaging==24.2
PyAudio==0.2.14
pydantic==2.10.6
pydantic_core==2.27.2
pydub==0.25.1
pypiwin32==223
pyttsx3==2.98
pywin32==310
PyYAML==6.0.2
requests==2.32.3
requests-toolbelt==1.0.0
sniffio==1.3.1
SpeechRecognition==3.14.2
SQLAlchemy==2.0.39
tenacity==9.0.0
typing_extensions==4.13.0
urllib3==2.3.0
zstandard==0.23.0
```

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/Hemantabhusal/ChatBot.git
```

Navigate into the project folder:

```bash
cd chatbot
```

Create a `.env` file and set your keys:

```bash
GROQ_API_KEY=your_groq_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
```

---

## 🧠 Usage

Run the chatbot:

```bash
python main.py
```

Type commands or queries like:

```text
What's the weather in Kathmandu?
Tell me about Pikachu
Open Chrome
Shutdown
```

To exit the session:

```text
exit
```

or

```text
quit
```

---

## ⚙️ Configuration

Edit `config.py` to tweak:

- `GROQ_TEMPERATURE` – Controls response creativity
- `GROQ_MAX_TOKENS` – Max token limit per reply
- Intent/action keywords for your custom use-cases

The chatbot is also configured for a **concise, slightly sarcastic tone** by default via the system prompt.

---

## 📁 Project Structure

```text
ChatBot/
├── actions/
│   ├── __init__.py               # Initializes the actions module
│   └── action.py                 # Executes system-level actions (e.g., open apps, shutdown)

├── API/
│   ├── __init__.py               # Initializes the API module
│   ├── pokemon_api.py            # Fetches Pokémon data from custom API
│   └── weather_api.py            # Fetches weather data from OpenWeather API

├── config/
│   ├── __init__.py               # Initializes the config module
│   └── config.py                 # Stores API keys and model configuration

├── recognize_intent/
│   ├── __init__.py               # Initializes the intent recognition module
│   ├── pokemon_intent.py         # Parses and handles Pokémon-related user queries
│   ├── recognize_intent.py       # Central intent handler and router
│   └── weather_intent.py         # Parses and handles weather-related user queries

├── .env                          # Stores environment variables (DO NOT COMMIT)
├── .gitignore                    # Git ignore file (e.g., ignores .env, __pycache__)
├── main.py                       # Main script to run the chatbot
├── README.md                     # Project documentation
└── requirements.txt              # Python package dependencies
```

## 🧑‍💻 Contributing

Contributions are welcome! To contribute:

```bash
# Fork this repo
# Create a new branch for your feature or bugfix
# Submit a pull request with clear description
```

---

## 🪪 License

Free to use, modify, and distribute. Commercial and personal use allowed.

---

## 📌 Notes

- Ensure `.env` is correctly configured before launching the bot
- The system commands are **Windows-specific**; support for macOS/Linux can be added by extending `system_actions.py`
- Make sure the APIs (Groq, OpenWeather, Pokemon) have sufficient quota and access rights


Happy Chatting! 🤖💬
