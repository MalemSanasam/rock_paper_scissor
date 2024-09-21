import random
print("Rock Paper Scissors")
user_input = input("Pick one: ").lower().strip()
if user_input == "rock" and user_input == "scissor":
  print("You win🥳")
  
items = ("rock", "paper", "scissor")

print(random.choice(items))

