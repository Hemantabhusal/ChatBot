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

---

## 📌 Notes

- Ensure `.env` is correctly configured before launching the bot
- The system commands are **Windows-specific**; support for macOS/Linux can be added by extending `system_actions.py`
- Make sure the APIs (Groq, OpenWeather, Pokemon) have sufficient quota and access rights


Happy Chatting! 🤖💬
