import random
message=[]
token=[]
jokes = ["Alright! I took the quiz and it turns out I do put career over men.",
         "Yes, on a scale of one to 10, 10 being the dumbest a person can look, you are definitely 19",
         "I'm not great at advice. Can I interest you with a sarcastic comment?",
         "Ok, you have to stop the Q-tip when there's resistance!",
         "What do you know? You're a door. You only like knock knock jokes.",
         "Until I was 25, I thought that the only response to 'I love you' was 'Oh, crap!'"]

def getReply ( message ):
    if "who" in message or "hi" in message:
        reply = "Hello, I'm Alpha the chatbot ^_^ "
    elif "joke" in message or "yes" in message:
        reply = random.choice(jokes)
    elif "how" in message and "you" in message:
        reply = "I am fine and how are you?"
    elif "what" in message and "do" in message:
        reply = "I am a chatbot and i will try to answer your questions *-*"
    elif " not fine" in message or " not good" in message or "bad" in message:
        reply = "Oh ... sorry to hear that can i tell you a joke for you?"
    elif "fine" in message or "good" in message:
        reply = "Nice... sounds good"
    else: 
        reply="sorry, I didn't understand you "
    print('Bot: ' + reply)


while ('bye' not in message):
    message = input('Human: ')
    message=message.lower()
    if "bye" in message:
        break
    getReply(message)

print("Bot: Bye have a nice day ^_^")
