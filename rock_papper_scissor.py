import random
def rps(user_input, computer):
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
def main():
  items = ("rock", "paper", "scissor")
  computer = random.choice(items)
  print("Rock Paper Scissors")
  user_input = input("You: ").lower().strip()
  print(f"Computer: {computer.capitalize()}")      
  while True:
    exit_option = input("Do you want to continue to play?(y/n) ").lower().strip()
    if exit_option == "y":
      rps(user_input, computer)
    else:
      break

if __name__ == '__main__':
  main()