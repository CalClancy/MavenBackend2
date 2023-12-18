import random

def generate_learn_instruction():
    content = "You are a Spanish teacher and your name is Rachel, the user is called Shaun. Keep responses under 20 words. "

    x = random.uniform(0, 1)
    if x < 0.2:
        content += "Your response will have some light humour. "
    elif x < 0.5:
        content += "Your response will include an interesting new fact about Spain. "
    else:
        content += "Your response will recommend another word to learn. "

    return {"role": "system", "content": content}

def generate_user_message_prompt(decoded_message):
    user_message = {
        "role": "user", 
        "content": decoded_message + " Only say two or 3 words in Spanish if speaking in Spanish. The remaining words should be in English"
    }
    return user_message
