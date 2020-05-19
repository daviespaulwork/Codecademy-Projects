import random

money = 100

#Write your game of chance functions here

def validate_bet(bet):
    if bet <0:
        print("Invalid Bet, bet a positive amount")
        return False
    else:
        return True

def coin_flip(bet, call):
    print("")
    print("-------------------------------------------")
    print("You're playing Coin Flip!")

    #Check Bet is Valid
    check = validate_bet(bet)

    if check == False:
        return

    #Clean Input and assign to 'Guess'

    lower = call.lower()
    clean = lower.find("heads")

    if clean == 0:
        guess = 1

    else:
        clean = lower.find("tails")
        
        if clean == 0:
            guess = 2
        
        else:
            print("Invalid Call, call 'Heads' or 'Tails'")
            return

    #Report to user the Bet
    print("")
    print ("You bet " + str(bet))    
    print("You called " + call)
    print("")
    
    
    #Generate Coin Flip
    result = random.randint(1,2)

    if(result == 1):
        print("The coin shows Heads")
    else:
        print("The coin shows Tails")

    print("")

    #Compare Result to Call and Report Outcome
    if guess == result:
        print("You Win " + str(bet))
    else:
        print("You Lose " + str(bet))
        bet = bet*-1
    print("")

    global money 
    money += bet
    print("Money now equals " + str(money))
    return
    
def cho_han(bet, call):
    print("")
    print("-------------------------------------------")
    print("You're playing Cho Han!")

   #Check if Bet and Call are Valid
    check = validate_bet(bet)

    if check == False:
        return

    lower = call.lower()
    clean = lower.find("even")

    if clean == 0:
        guess = "even"

    else:
        clean = lower.find("odd")
        
        if clean == 0:
            guess = "odd"
        
        else:
            print("Invalid Call, call 'Odd' or 'Even'")
            return

    #Report to user the Bet and the Call
    print("")
    print ("You bet " + str(bet))    
    print("You called " + call)
    print("")
    
    #Simulate Rolling Two Dice and determine Odd or Even

    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    total = roll1 + roll2
    if total % 2 == 0:
        result = "even"
    else:
        result = "odd"

    print("The Roll is " + str(total) + " which is " + result)

    #Compare Result to Call and Report Outcome
    if guess == result:
        print("You Win " + str(bet))
    else:
        print("You Lose " + str(bet))
        bet = bet*-1
    print("")

    global money 
    money += bet
    print("Money now equals " + str(money))
    return

def card_draw(bet):
    print("")
    print("-------------------------------------------")
    print("You're playing Card Draw!")

    #Check if Bet is Valid
    check = validate_bet(bet)

    if check == False:
        return

    #Report to user the Bet and the Call
    print("")
    print ("You bet " + str(bet))
    card = random.randint(1,13)   
    print("")
    print("You picked card number " + str(card))
    
    
    #Simulate Computer Draw
    result = random.randint(1,13)
    print("Card Drawn is number " + str(result))
    print("")

    #Compare Result to Card and Report Outcome
    if card == result:
        print("Game Tied. " + str(bet) + " returned.")
        bet = 0
    elif card<result:
        print("You Lose " + str(bet))
        bet = bet*-1
    else:
        print("You Win " + str(bet))
    print("")

    global money 
    money += bet
    print("Money now equals " + str(money))
    return

def roulette(bet, guess):
    print("")
    print("-------------------------------------------")
    print("You're playing Roulette!")

    #Check if Bet is Valid
    check = validate_bet(bet)

    if check == False:
        return

    #Report to user the Bet and the Call
    print("")
    print ("You bet " + str(bet))    
    print("You picked " + str(guess))
    print("")
    
    #Simulate Spin and Report

    wheel = random.randint(-1,36)
    parity = None
    colour = None
    number = None

    if wheel % 2 == 0:
        parity = "Even"
    else:
        parity = "Odd"

    red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

    if wheel in red:
        colour = "Red"
    else:
        colour = "Black"

    if wheel in range(1,19):
        number = "Low"
    elif wheel in range(19, 37):
        number = "High"
    else:
        number = "0/00"

    if wheel == -1:
        print("The Spin is 00")
    elif wheel == 0:
        print("The Spin is 0")
    else:
        print("The Spin is " + str(wheel) + ", which is " + parity + ", " + colour + " and " + number)

    #Check Result and Report Winnings
        global money

        #Red or Black
    if guess == "Red" or guess == "Black":
        if guess == colour:
            print("You win " + str(bet))
            
        else:
            print("You lose " + str(bet))
            bet = bet *-1
        
        
        money += bet
        print("Money now equals " + str(money))
        return

        #Odd or Even
    if guess == "Odd" or guess == "Even":
        if guess == parity:
            print("You win " + str(bet))
            
        else:
            print("You lose " + str(bet))
            bet = bet *-1
        
        
        money += bet
        print("Money now equals " + str(money))
        return

        #High or Low
    if guess == "High" or guess == "Low":
        if guess == number:
            print("You win " + str(bet))
            
        else:
            print("You lose " +str(bet))
            bet = bet *-1
        
         
        money += bet
        print("Money now equals " + str(money))
        return

        #Number
    if guess == wheel:
        print("You win " + str(bet*36))
        bet = bet*36    
    else:
        print("You lose " +str(bet))
        bet = bet *-1

     
    money += bet
    print("Money now equals " + str(money))
    return


    





#Call your game of chance functions here
coin_flip(10, "Heads")
cho_han(50, "Odd")
card_draw(10)
roulette(10, "Odd")
roulette(10, "Red")
roulette(5, "High")
roulette(5, 5)
