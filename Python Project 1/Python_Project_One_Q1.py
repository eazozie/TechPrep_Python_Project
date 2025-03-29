#Magic 8 Ball Project 

#Importing the random module on the python library
import random

#Input vaue asking the user to type in a question
User = input("Please ask your question:")

#Writing a function that picks a random value from any section of the list
def Standard_Magic(ebube):
    selected_items = random.sample(ebube, 1)
    for item in selected_items:
        print(item)

#Assigning the responses in a list according to their respective categories 
#Response A for affirmative answers, NC for non-committal asnwers and N for negative answers 

response_A = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes"]
response_NC = ["Reply Hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again"]
response_N = ["Dont count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]


#Assigning the responses to 'answer' to capture all the response categories
answers = [response_A, response_NC, response_N]

#Running the function to select a random choice from the list in 'answers'
Standard_Magic(random.choice(answers))