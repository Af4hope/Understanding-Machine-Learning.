import nltk
from nltk.chat.util import Chat, reflections

reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you",
}
pairs = [
    [r"my name is (.*)", 
    ["Hello %1, how can I help you today?",]
],

[r"hi|hey|hello", 
 ["Hello!", "Hey there!",]],

[r"what is your name?", 
 ["I am a bot created by Codingal Edu.pvt. Lim.you can call me Jarvis!",]],

[r"how are you?", 
 ["I'm doing well, thank you! How about you?",]],

[r"sorry (.*)", 
 ["Its alright", "Its OK, never mind",]],

[r"i'm fine", 
 ["Great to hear that! How can I assist you today?",]],

[r"quit", 
 ["Bye! take care. See you soon :)", "It was nice talking to you. See you soon :)"]],]

def chat():
    print("Hi! I'm a chatbot created by Codingal Edu.pvt. Lim. for your service.")
    chat = Chat(pairs, reflections)
    chat.converse()
if __name__ == "__main__":    
    chat()