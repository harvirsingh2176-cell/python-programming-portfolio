# Importing random for randoming choosing move
import random

# TITLE
print("---ROCK PAPER SCISSORS---")

# ASking Name
name=input("Your name: ")

# Asking the rounds
try:
    rounds=int(input("Rounds you want to play: "))
    if(rounds<=0):
        print("Enter a number greater than 0")
        exit()
except ValueError:
    print("Enter a number greater than 0")
    exit()


# Defining lists for moves, score of user and bot
moves=["paper","scissors","rock"]
score_user=[]
score_bot=[]

# Score
grade=["Tie","Point:1","Bot Point:1"]

# User Win f(x)
def user_win():
    score_user.append(1)
    score_bot.append(0)
    print(name,grade[1])

# Bot Win f(x)
def bot_win():
    score_user.append(0)
    score_bot.append(1)
    print(grade[2])

# Tie f(x)
def tie_func():
    score_user.append(0)
    score_bot.append(0)
    print(grade[0])

# Game Function
def game_func():
    # Game Rounds
    for _ in range (rounds):

        # User Move
        while True:
            user_move=input("\nEnter Your Move: ").strip().lower()

            if (user_move in moves):
                break

        # Random moves by Bot 
        bot_move=random.choice(moves)

        # Printing Moves of Bot
        print(f"Bot Move: {bot_move.capitalize()}")

        # Rules
        # User Win
        if(user_move =="scissors" and bot_move == "paper"):
            user_win()
        elif(user_move == "rock" and bot_move == "scissors"):
            user_win()
        elif(user_move == "paper" and bot_move == "rock"):
            user_win()

        # Bot Win
        elif(user_move =="paper" and bot_move == "scissors"):
            bot_win()
        elif(user_move == "scissors" and bot_move == "rock"):
            bot_win()
        elif(user_move == "rock" and bot_move == "paper"):
            bot_win()

        # Tie
        else:
            tie_func()       

# f(x) call
game_func()

# Game Over
print("\nGame Over")

#  Score Board
print(f"---Score Board---\n{name} Score: {sum(score_user)}\nBot Score: {sum(score_bot)}")

# When Bot Wins
if(sum(score_bot)>sum(score_user)):
    print("\nBot Wins")

# When user wins
elif(sum(score_user)>sum(score_bot)):
    print(f"\n{name} Wins")

# Tie
else:
    print("\nTie")