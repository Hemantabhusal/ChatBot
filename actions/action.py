from config.config import ACTION_KEYWORDS
import subprocess

def execute_action(intent, memory):
    """
    Executes a system command based on the recognized intent and logs the action into memory.

    Args:
        intent (str): The recognized intent.
        memory: The conversational memory object.

    Returns:
        str: A message indicating the result of the action.
    """
    if intent in ACTION_KEYWORDS:
        command, message = ACTION_KEYWORDS[intent]
        try:
            # Execute the system command
            subprocess.run(command, shell=True, check=True)

            # Log the action into memory
            memory.chat_memory.add_ai_message(message)

            return message
        except subprocess.CalledProcessError as e:
            error_message = f"Failed to execute action for {intent}. Error: {e}"
            memory.chat_memory.add_ai_message(error_message)  # Log failure into memory
            return error_message

    # Handle undefined intents
    undefined_message = f"No action defined for intent: {intent}"
    memory.chat_memory.add_ai_message(undefined_message)
    return undefined_message
