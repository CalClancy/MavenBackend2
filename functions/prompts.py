import random

# Set the system message
def generate_learn_instruction():
    content = "You are a Spanish teacher and your name is Marcus."
    content += "Your response will have some light humour. "
    content += "Your demanour is supportive and patient. "
    
    return {"role": "system", "content": content}

def generate_user_message_prompt(decoded_message):
    user_message = {
        "role": "user", 
        "content": decoded_message + " Only say two or 6 words in Spanish if speaking in Spanish. The remaining words should be in English"
    }
    return user_message
