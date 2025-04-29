import re

def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if re.search(r"hello|hi", user_input):
        return "Hello! How can I assist you today?"
    elif re.search(r"what is your name", user_input):
        return "I am a chatbot, your virtual assistant."
    elif re.search(r"thank you", user_input):
        return "You're welcome! Let me know if you need anything else."
    elif re.search(r"how are you", user_input):
        return "I'm just a bot, but I'm here to help you! How can I assist you?"
    elif re.search(r"bye|goodbye", user_input):
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you rephrase?"

# Test the chatbot
print("Chatbot: Hello, how can I assist you?")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "goodbye"]:
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
