import random

# Set the system message
def generate_learn_instruction():
    content = "You are a Latin teacher and your name is Marcus."
    content += "Your response will have some light humour. "
    content += "Your demanour is supportive and patient. "
    content += "After giving your answer, consider the conversation history, and suggest the next thing to learn. Ask if use would like to learn it."
    
    return {"role": "system", "content": content}

def generate_user_message_prompt(decoded_message):
    user_message = {
        "role": "user", 
        "content": decoded_message
    }
    return user_message
