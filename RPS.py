#Rock paper scissors game
import random
player_score=0
pc_score=0
options=("Rock","Paper","Scissors")

print "ROCK PAPER SCISSORS!"
name=raw_input("What is your name?")
print "Welcome "+ name + " to the game"

print "The rules are simple:"
print "Rock crushes Scissors. Scissors cuts Paper. Paper beats " \
"Rock (no one knows why)"
n=int(raw_input("How many times do you want to play?"))

print "Which do you choose?:"
for x in range(0,n):
    player=raw_input("Rock, Paper or Scissors?").lower()
    options=["Rock","Paper","Scissors"]
    pc=random.choice(options)
    print "PC picked ",pc
    pc=pc.lower()
    if pc==player:
        print "Its a tie!"
    elif pc=="rock" and player=="scissors":
        print "PC wins!"
        pc_score+=1
    elif pc=="rock" and player=="paper":
        print name+" wins!"
        player_score+=1
    elif pc=="paper" and player=="scissors":
        print name+" wins!"
        player_score+=1
    elif pc=="paper" and player=="rock":
        print "PC wins!"
        pc_score+=1
    elif pc=="scissors" and player=="paper":
        print "PC wins!"
        pc_score+=1
    elif pc=="scissors" and player=="paper":
        print name+" wins!"
        player_score+=1
    else:
        print "That was not an option!"

print name, " won ", player_score
print"PC won ", pc_score
if player_score>pc_score:
    print name," wins the game!"
elif pc_score>player_score:
    print "Sorry, the PC won!"
else:
    print "It's a Draw!"
