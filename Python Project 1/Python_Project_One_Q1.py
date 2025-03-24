import random

User = input("Please ask your question:")

def Standard_Magic(ebube):
    selected_items = random.sample(ebube, 3)
    for item in selected_items:
        print(item)

response_A = ["It is certain", "it is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes"]
response_NC = ["Reply Hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again"]
response_N = ["Dont count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

answers = [response_A, response_NC, response_N]
Standard_Magic(random.choice(answers))