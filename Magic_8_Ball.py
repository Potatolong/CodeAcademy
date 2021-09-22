import random

name = "Billy"
question = "Will I win the lottery?"
answer = ""

#This will produce a filler if a name is not provided.

#if len(name) == 0:
  #print("Question: " + question)
#else: 
  #print(name + " asks: " + question)  

#This will produce a filler if a question is not provided.

#if len(question) == 0:
  #print(name + question)
#lse: 
  #print(name + " asks: " + question)
  #print("Magic 8-Ball's answer: " + answer)  

random_number = random.randint(1, 12)
  #print(random_number)

if random_number == 1: 
  answer = "Yes - definitely."  
elif random_number == 2: 
  answer = "It is decidedly so."
elif random_number == 3: 
  answer = "Without a doubt."
elif random_number == 4: 
  answer = "Reply hazy, try again."  
elif random_number == 5: 
  answer = "Ask again later."  
elif random_number == 6: 
  answer = "Better not tell you now." 
elif random_number == 7: 
  answer = "My sources say no."   
elif random_number == 8: 
  answer = "Outlook not so good."  
elif random_number == 9: 
  answer = "Very doubtful."  
elif random_number == 10: 
  answer = "No dice yet.."
elif random_number == 11: 
  answer = "Let me check here in a bit."
elif random_number == 12: 
  answer = "Pack your bags, it is happening."       
else: 
  answer = "Error"

print(name + " asks: " + question)

print("Magic 8-ball's answer: " + answer)
