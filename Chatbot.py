import random
import nltk
from nltk.chat.util import Chat, reflections

# Download NLTK data
nltk.download('punkt')

# Define pairs of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you today?", "Hi there! What can I do for you?"]
    ],
    [
        r"what is your name?",
        ["I'm a simple chatbot. You can call me Chatty!", "My name is Chatty. Nice to meet you!"]
    ],
    [
        r"how are you?",
        ["I'm just a program, so I'm always functioning well!", "I don't have feelings, but thanks for asking!"]
    ],
    [
        r"what can you do?",
        ["I can chat with you, answer simple questions, and tell jokes!", "My skills are limited, but I can have basic conversations."]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!", 
         "What do you call a fake noodle? An impasta!"]
    ],
    [
        r"quit|bye|exit",
        ["Goodbye! It was nice talking to you.", "See you later! Have a great day."]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Could you rephrase that?", 
         "Interesting! Tell me more about that."]
    ]
]

def chatbot():
    print("Chatty: Hello! I'm a simple chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
