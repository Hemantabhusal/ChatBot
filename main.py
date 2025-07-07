from recognize_intent.recognize_intent import handle_intent
from config.config import SYSTEM_PROMPT
from langchain.chains import LLMChain
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
from config.config import (
    GROQ_API_KEY,
    GROQ_MODEL_NAME,
    GROQ_MAX_TOKENS,
    GROQ_TEMPERATURE,
    SYSTEM_PROMPT,
)

# Initialize the Groq Chat client
groq_chat = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name=GROQ_MODEL_NAME,
    base_url="https://api.groq.com",
    max_tokens=GROQ_MAX_TOKENS,
    temperature=GROQ_TEMPERATURE,
)

# Initialize conversational memory
memory = ConversationBufferWindowMemory(
    window_size=5,  # Number of recent exchanges to remember
    memory_key="chat_history",
    return_messages=True,
)

# Define the prompt template with placeholders for memory
prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content=SYSTEM_PROMPT),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{human_input}"),
    ]
)


def process_query(user_input):
    """
    Processes user input with conversational memory.

    Args:
        user_input (str): The user's input.

    Returns:
        str: The chatbot's response.
    """
    # Create an LLMChain for generating responses
    conversation = LLMChain(
        llm=groq_chat,
        prompt=prompt,
        verbose=False,
        memory=memory,
    )

    # Use the LLM to predict a response based on user input
    return conversation.predict(human_input=user_input)


def main():
    """
    Main chatbot function with integrated memory for both conversation and actions.
    """
    print("Welcome! You can start chatting with me. Type 'exit' to end the conversation.")
    while True:
        user_input = input("User: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye! Have a great day!")
            break

        # Handle intent
        if handle_intent(user_input, memory):
            continue

        # Handle general conversation using process_query
        response = process_query(user_input)
        print(f"Eva: {response}")


if __name__ == "__main__":
    main()
