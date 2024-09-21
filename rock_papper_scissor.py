import random
items = ("rock", "paper", "scissor")
computer = random.choice(items)
print("Rock Paper Scissors")
user_input = input("You: ").lower().strip()
print(f"Computer: {computer.capitalize()}")

if user_input == "rock":
  if computer == "scissor":
    print("you win🥳")
  elif computer == user_input:
    print("Draw📍")  
  else:
    print("you lose😟")  
if user_input == "scissor":
  if computer == "paper":
    print("you win🥳")
  elif computer == user_input:
      print("Draw📍")  
  else:
    print("you lose😟")  

