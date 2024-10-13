import random
u=input("Enter rock or paper or scissors:")
c=("rock","paper","scissors")
a=random.choice(c)
print("computer's choice:",a)
if a==u:
    print("draw")
elif (u=="rock" and a=="scissors") or (u=="paper" and a=="rock") or (u=="scissors" and a=="paper"):
    print("you win")
else:
    print("you lose")
    
