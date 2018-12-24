import random


greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!','hey']
random_greeting = random.choice(greetings)
name=input("What is your name?  ")
print("Hello " +name)

question = ['How are you?','What is your name?','What is the time?','What are you doing?']
responses = ['Okay',"Jarvis",'*3:30 PM*','"Just Chilling!!"']
random_response = random.choice(responses)


while True:
	userInput = input(">>>")
	if userInput in greetings:
		print(random_greeting)
	elif userInput in question:
		print(random_response)
	else:
		print("I did not get what you said")
