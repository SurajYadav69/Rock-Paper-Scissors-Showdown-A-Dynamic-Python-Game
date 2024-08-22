Python Rock-Paper-Scissors Game


Overview:-
This is a simple Rock-Paper-Scissors game implemented in Python. The game allows the user to play against the computer, which randomly selects one of the three options. The outcome is determined based on standard Rock-Paper-Scissors rules.

How It Works:- 
Computer's Choice: The computer randomly selects one of the three options: Rock👊, Paper✋, or Scissor✌.
User Input: The user is prompted to enter their choice (Rock, Paper, or Scissor).
Result: The game determines the result based on the user's choice and the computer's choice:
Win: User's choice beats the computer's choice.
Draw: User's choice is the same as the computer's choice.
Lose: User's choice loses to the computer's choice.
Display: The game displays the result of the match and shows the computer's choice.
Usage
Run the Python script.
When prompted, enter your choice (Rock, Paper, or Scissor).
The game will display whether you won, lost, or drew, along with the computer's choice.


Code:- 
import random

computer = ["Rock👊", "Paper✋", "Scissor✌"]
x = random.choice(computer)

user = input("Enter your choice (Rock/Paper/Scissor): ")
if(x == "Rock👊" and user == "Paper"): 
    print("You Win")
elif(x == "Paper✋" and user == "Scissor"): 
    print("You Win")
elif(x == "Scissor✌" and user == "Rock"): 
    print("You Win")
elif(x == "Rock👊" and user == "Rock"): 
    print("Match Draw")
elif(x == "Paper✋" and user == "Paper"): 
    print("Match Draw")
elif(x == "Scissor✌" and user == "Scissor"): 
    print("Match Draw")
else: 
    print("You Lose The Match")

print("Computer Choice:-", x)
