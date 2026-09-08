import random

name = input("What's your name: ")
print("Let's play a game", name)
player_score = 0
computer_score = 0
options = ["ROCK",  "PAPER", "SCISSORS"]
while True:
    player_choice= input("""
    ROCK,
    PAPER,
    SCISSORS""").strip().upper()
    if player_choice not in options:
        print("Invalid choice, please choose rock, paper, or scissors")
        continue

   
    
    computer_choice = random.choice(options)
    print(computer_choice)
    print(player_choice)
    if computer_choice==player_choice:
        print("It's a tie")
    elif( (player_choice=="ROCK" and computer_choice=="SCISSORS") or
          (player_choice=="PAPER" and computer_choice=="ROCK") or
          (player_choice=="SCISSORS" and computer_choice=="PAPER")
          
         ): 
        print("YOU WON THE ROUND")
        player_score+=1
    else:
            print("YOU LOST,OPPONENT TOOK THE VICTORY")
            computer_score+=1
    print(f"Score — You: {player_score}, Computer: {computer_score}")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        print(f"Final score — You: {player_score}, Computer: {computer_score}")
        break


     
        

    
    


