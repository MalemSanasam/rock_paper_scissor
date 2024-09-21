import random
items = ("rock", "paper", "scissor")
computer = random.choice(items)
print("Rock Paper Scissors")
user_input = input("You: ").lower().strip()
print(f"Computer: {computer.capitalize()}")
# user picking rock
if user_input == "rock":
  if computer == "scissor":
    print("you win🥳")
  elif computer == user_input:
    print("Draw📍")  
  else:
    print("you lose😟")  
# user picking scissor    
if user_input == "scissor":
  if computer == "paper":
    print("you win🥳")
  elif computer == user_input:
      print("Draw📍")  
  else:
    print("you lose😟") 
# user picking paper     
if user_input == "paper":
  if computer == "rock":
    print("you win🥳")
  elif computer == user_input:
      print("Draw📍")  
  else: 
    print("you lose😟")  
    
