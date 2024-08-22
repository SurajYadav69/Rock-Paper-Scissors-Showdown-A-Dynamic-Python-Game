# Rock Paper Scissor Game

import random

computer = ["Rock👊","Paper✋","Scissor✌"]
x = random.choice(computer)

user = input("Enter your choice (Rock/Paper/Scissor):")
if(x=="Rock👊" and user=="Paper"): print("You Win")
elif(x=="Paper✋" and user=="Scissor"): print("You Win")
elif(x=="Scissor✌" and user=="Rock"): print("You Win")
elif(x=="Rock👊" and user=="Rock"): print("Match Draw")
elif(x=="Paper✋" and user=="Paper"): print("Match Draw")
elif(x=="Scissor✌" and user=="Scissor"): print("Match Draw")
else: print("You Lose The Match")

print("Computer Choice:-" , x)

