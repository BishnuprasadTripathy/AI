import nltk
from nltk.chat.util import Chat, reflections

# Define the chatbot's responses
pairs = [
    [
        r"(.*) your name ?",
        ["My name is ChatGPT.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm good, how about you?"]
    ],
    [
        r"sorry (.*)",
        ["It's okay!", "No worries!"]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"quit",
        ["Goodbye! It was nice talking to you.", "See you soon!"]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Could you please clarify?", "Can you rephrase that?"]
    ]
]

# Create and start the chatbot
def chatbot():
    print("Hi! I'm a simple chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
