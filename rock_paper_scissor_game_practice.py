from random import randint
# taking case insensitive choices
choice = ['rock','paper','scissors']
ch = 'y'
rounds = 0

# function to take player choice
def player_choice():
    plr_ch = input("\nPlease input complete word.\nEnter your choice Rock / Paper / Scissors: ")

    # player can input other char so check to ensure that cannot be broken
    if plr_ch.lower() and plr_ch.upper() in ('rock', 'paper', 'scissors'):
        return plr_ch.lower()
    else:
        print("\nWrong choice!! Retry!!")
        player_choice()

#function with parameter to get result on every choice
def get_result(plr_ch):
    comp_choice = choice[randint(0,2)]
    print("\nComputer choice,: ",comp_choice,"\n")

    #basic game rules
    if plr_ch == comp_choice:
        result = "tie"
        print(f"{plr_ch.upper()} is same as {comp_choice.upper()}! No score change")
    elif comp_choice == 'scissors' and plr_ch == 'rock':
        result = 'win'
        print('ROCK crushes SCISSORS! You win! Score +1')
    elif comp_choice == 'paper' and plr_ch == 'scissors': 
        result = 'win'
        print('SCISSORS cut PAPER! You win! Score +1')
    elif comp_choice == 'rock' and plr_ch == 'paper': 
        result = 'win'
        print('PAPER covers ROCK! You win! Score +1')

    #if it does not match any of the win criteria then add 1 to loss and 
    #display loss message 
    else:
        result = 'loss'
        print ('You loose! Score -1')
    return result

#now function to update the scores
def update_score(result):
    global wins, loss, tie
    if result == 'win':
        wins +=1
    elif result == 'loss':
        loss +=1
    else:
        tie += 1    

# Now function to run the game till user defined rounds
def game(rounds):
    total_score = 0
    global round_result
    for i in range(0, rounds):
        print("\nReady for round", i+1)
        pc = player_choice()
        res = get_result(pc)
        round_result.append(res)
        update_score(res)
        total_score = wins - loss #we can ignore tie as tie score is 0
        print("\nAfter round",(i+1),"your score is: ",total_score)

    #at the end of all rounds we return total score
    return total_score

#to take the number of rounds from user
def game_rounds(r=0):
    r = input("\nEnter how many rounds you want to play: ")

    #to ensure number is integer and code dosen't crash on other values 
    try:
        global rounds
        rounds = int(r)
    except:
        print("\nWrong input, Enter a number!")
        game_rounds()

# main function to run everything
def main():
    global ch, round_result
    print("\nWelcome to Rock, Paper, Scissors Game.\nRules are simple")
    print('''\nWinning Rules are as follows:
    Rock vs Paper -> Paper wins Rock Losses
    Rock vs Scissors -> Rock wins Scissors Losses
    Paper vs Scissors -> Scissors wins Paper Losses\n
    For each win you get 1 point 
    If you lose -1 point
    And if its a tie 0 point\n''')

    game_rounds()
    ts = game(rounds)

    #displaying results after all  rounds
    print(f"\nAfter {rounds} rounds, your final score is: {ts}")
    print(f"\nYou have {wins} wins, {tie} ties and {loss} losses!")
    print(f"\nRound wise result is {round_result}")
    ch = input("\nDo you want to continue? Enter y for yes any other char to exit: ")

while(ch == 'y' or ch == 'Y'):
    wins = 0
    loss = 0
    tie = 0

    round_result = []
    rounds
    main()
    print("\nSee you again")