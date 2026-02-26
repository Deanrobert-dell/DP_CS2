

def gam():
    import random

    random_move= random.randint(1,3)

    user_score = 0

    comp_score = 0

    rock = "    _____   \n   /     \\ \n  |       | \n   \\_____/ \n      "

    scissor = "Ʌ     Ʌ\n\\\\   //\n \\\\_//\n  (_)\n/\\   /\\ \n\\/   \\/ "

    paper = " ______\n/     /\n|     |\n\\_____\\"


    while comp_score < 5:
        random_move= random.randint(1,3)
        if random_move == 1:
            comp_move = (rock)
        elif random_move == 2:
            comp_move = (paper)
        elif random_move == 3:
            comp_move = (scissor)
        else:
            print("error")

        print ("computer chose, your turn \n")

        user_input = input("choose rock (1) paper (2) scissors (3) or quit (4): ")
        

        #WIERD problem where every other time it works, this fixes those times it doesnt
        try:
            user_input = int(user_input)
        except ValueError:
            print("error")
            continue

        #continues
        if user_input == 1:
            user_move = (rock)
        elif user_input == 2:
            user_move = (paper)
        elif user_input == 3:
            user_move = (scissor)
        elif user_input == 4:
            print ("quiting")
            break
        else:
            print("error")
        print (user_move)


        if user_move == rock and comp_move == paper:
            print ("comp chose paper, you lost")
            comp_score += 1
        elif user_move == rock and comp_move == scissor:
            print ("comp chose scissors, you won")
            user_score += 1
        elif user_move == rock and comp_move == rock:
            print ("comp chose rock, you tied")
            user_score += 0
        elif user_move == paper and comp_move == rock:
            print ("comp chose rock, you won")
            user_score += 1
        elif user_move == paper and comp_move == scissor:
            print ("comp chose scissors, you lost")
            comp_score += 1
        elif user_move == paper and comp_move == paper:
            print ("comp chose paper, you tied")
            user_score += 0
        elif user_move == scissor and comp_move == rock:
            print ("comp chose rock, you lost")
            comp_score += 1
        elif user_move == scissor and comp_move == paper:
            print ("comp chose paper, you won")
            user_score += 1
        elif user_move == scissor and comp_move == scissor:
            print ("comp chose scissor, you tied")
            user_score += 0
        else:
            print("wrong input")
            continue
        if comp_score >= 5:
            print ("computer won, you suck")
            print ("your highscore was", user_score)
            break
        print ("your score is", user_score, "computer score is", comp_score)
        


    print (user_move)
gam()


        
