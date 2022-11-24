import random
Score = 0
ComScore = 0
Game=True
TossScore = 0
TossComScore = 0
Under = 0
while Game==True:
    print("HandCricket|V1.2 - Made By Tharul Karunaratne")
    print("1.Start")
    print("2.Exit")
    Choice1 = int(input("Enter Choice: "))
    if Choice1 == "":
        print("Error")
    while Choice1 == 2:
        print("You Chose To Exit")
        Game=False
        Choice1=4
    while Choice1 == 1:
        print("----------------------")
        print("1.Toss")
        print("2.Random Toss")
        Choice5 = int(input("Pick From Above: "))
        print("----------------------")
        while Choice5 == 1:
                print("1.Rock")
                print("2.Paper")
                print("3.Scissors")
                print("----------------------")
                userChoice = int(input("Pick One Of The Above: "))
                comChoice = random.randint(1,3)
                if comChoice==1:
                    print("Computer Choose Rock")
                elif comChoice==2:
                    print("Computer Choose Paper")    
                else:
                    print("Computer Choose Scissors")   
                if userChoice==comChoice:
                    print("Its A Draw")    
                elif userChoice==1 and comChoice==3:
                    print("You Won!")
                    TossScore = int(TossScore + 1)    
                elif userChoice==2 and comChoice==1:
                    print("You Won!") 
                    TossScore = int(TossScore + 1)  
                elif userChoice==3 and comChoice==2:
                    print("You Won!")
                    TossScore = int(TossScore + 1)  
                else:
                    print("Computer Wins!")
                    TossComScore = TossComScore + 1
                if userChoice > 3:
                    print("Error, Try Again") 
                    TossComScore = TossComScore - 1   
                if TossScore == 3:
                    print("----------------------")
                    print("You Won The Toss")
                    print("----------------------")
                    print("1.Batting")
                    print("2.Balling")
                    Choice8 = int(input("Pick One Of The Above: "))
                    if Choice8 == 1:
                        print("Batting")
                        print("Start")
                        Under = int(input("Under: "))
                        print("----------------------")
                        while Game==True:
                            UserC = int(input("Enter Number: "))
                            ComC = random.randint(1,(Under))
                            print("Computer Played:",ComC)
                            if UserC > (Under):
                                print("Error")
                                Score = Score - UserC
                            if UserC == "":
                                print("Error")
                            if UserC < 1:
                                print("Error")       
                            if UserC!=ComC:
                                Score = Score + UserC
                                print("Your Total Score:",Score)   
                            while ComC == UserC:
                                print("Your Out")
                                print("Your Score Is",Score)
                                while Game == True:
                                    print("Now You are Balling")
                                    print("----------------------")
                                    while Game == True:
                                        UserC2 = int(input("Enter Number: "))
                                        ComC2 = random.randint(1,(Under))
                                        print("Computer Played:",ComC2)
                                        if UserC2 > (Under):
                                            print("Error")
                                        if UserC2 == "":
                                            print("Error")
                                        if UserC2 < 1:
                                            print("Error")
                                            ComScore = ComScore + (Under)
                                            ComScore = ComScore - ComC2           
                                        if UserC2!= ComC2:
                                            ComScore = ComScore + ComC2
                                            print("Computer's Total:",ComScore)   
                                        if ComScore > Score:
                                            print("You Lost!")
                                            print("Your Score Is",Score)
                                            print("Computer's Score Is",ComScore)
                                            print("Thanks For Playing!")
                                            Game = False
                                            exit()
                                        if UserC2 == ComC2 and ComScore < Score:
                                            print("You Won!")
                                            print("Your Score Is",Score)
                                            print("Computer's Score Is",ComScore)
                                            print("Thanks For Playing!")
                                            Game = False
                                            exit()
                                        if Score == ComScore and UserC2 == ComC2:
                                            print("Tie")
                                            print("Your Score Is",Score)
                                            print("Computer's Score Is",ComScore)
                                            print("Thanks For Playing!")
                                            Game = False
                                            exit()
                    elif Choice8 == 2:
                        print("Balling")
                        print("Start")
                        Under = int(input("Under: "))
                        print("----------------------")
                        while Game==True:
                            UserC = int(input("Enter Number: "))
                            ComC = random.randint(1,(Under))
                            print("Computer Played:",ComC)
                            if UserC > (Under):
                                print("Error")
                            if UserC < 1:
                                print("Error")
                                ComScore = ComScore + (Under)
                                ComScore = ComScore - ComC    
                            if UserC == "":
                                print("Error")    
                            if UserC!= ComC:
                                ComScore = ComScore + ComC
                                print("Computer's Total:",ComScore)
                            while ComC == UserC:
                                print("Computer Out")
                                print("Computer's Score Is",ComScore)
                                while Game == True:
                                    print("Now You are Batting")
                                    print("----------------------")
                                    while Game == True:
                                        UserC2 = int(input("Enter Number: "))
                                        ComC2 = random.randint(1,(Under))
                                        print("Computer Played:",ComC2)
                                        if UserC2 == "":
                                            print("Error")
                                        if UserC2 < 1:
                                            print("Error")      
                                        if UserC2 > (Under):
                                            print("Error")
                                            Score = Score - UserC2
                                        if UserC2!= ComC2:
                                            Score = Score + UserC2
                                            print("Your Total:",Score)   
                                        if Score > ComScore:
                                            print("You Won!")
                                            print("Your Score Is",Score)
                                            print("Computer's Score Is",ComScore)
                                            print("Thanks For Playing!")
                                            Game = False
                                            exit()
                                        if UserC2 == ComC2 and Score < ComScore:
                                            print("You Lost!")
                                            print("Your Score Is",Score)
                                            print("Computer's Score Is",ComScore)
                                            print("Thanks For Playing!")
                                            Game = False
                                            exit()
                                        if Score == ComScore and UserC2 == ComC2:
                                            print("Tie")
                                            print("Your Score Is",Score)
                                            print("Computer's Score Is",ComScore)
                                            print("Thanks For Playing!")
                                            Game = False
                                            exit()                 

                if TossComScore == 3:
                    print("You Lost The Toss")
                    print("----------------------")
                    Toss = random.randint(0,2)
                    while Toss==2:
                        print("Balling")
                        print("Start")
                        print("----------------------")
                        while Game==True:
                            UserC = int(input("Enter Number: "))
                            ComC = random.randint(1,10)
                            print("Computer Played:",ComC)
                            if UserC > 10:
                                print("Error")
                            if UserC < 1:
                                print("Error")
                                ComScore = ComScore + 10
                                ComScore = ComScore - ComC    
                            if UserC == "":
                                print("Error")    
                            if UserC!= ComC:
                                ComScore = ComScore + ComC
                                print("Computer's Total:",ComScore)
                            while ComC == UserC:
                                print("Computer Out")
                                print("Computer's Score Is",ComScore)
                                while Game == True:
                                    print("Now You are Batting")
                                    print("----------------------")
                                    while Game == True:
                                        UserC2 = int(input("Enter Number: "))
                                        ComC2 = random.randint(1,10)
                                        print("Computer Played:",ComC2)
                                        if UserC2 == "":
                                            print("Error")
                                        if UserC2 < 1:
                                            print("Error")      
                                        if UserC2 > 10:
                                            print("Error")
                                            Score = Score - UserC2
                                        if UserC2!= ComC2:
                                            Score = Score + UserC2
                                            print("Your Total:",Score)   
                                        if Score > ComScore:
                                            print("You Won!")
                                            print("Your Score Is",Score)
                                            print("Computer's Score Is",ComScore)
                                            print("Thanks For Playing!")
                                            Game = False
                                            exit()
                                        if UserC2 == ComC2 and Score < ComScore:
                                            print("You Lost!")
                                            print("Your Score Is",Score)
                                            print("Computer's Score Is",ComScore)
                                            print("Thanks For Playing!")
                                            Game = False
                                            exit()
                                        if Score == ComScore and UserC2 == ComC2:
                                            print("Tie")
                                            print("Your Score Is",Score)
                                            print("Computer's Score Is",ComScore)
                                            print("Thanks For Playing!")
                                            Game = False
                                            exit()                 
                    while Toss==1:
                        print("Batting")
                        print("Start")
                        print("----------------------")
                        while Game==True:
                            UserC = int(input("Enter Number: "))
                            ComC = random.randint(1,10)
                            print("Computer Played:",ComC)
                            if UserC > 10:
                                print("Error")
                                Score = Score - UserC
                            if UserC == "":
                                print("Error")
                            if UserC < 1:
                                print("Error")       
                            if UserC!=ComC:
                                Score = Score + UserC
                                print("Your Total Score:",Score)   
                            while ComC == UserC:
                                print("Your Out")
                                print("Your Score Is",Score)
                                while Game == True:
                                    print("Now You are Balling")
                                    print("----------------------")
                                    while Game == True:
                                        UserC2 = int(input("Enter Number: "))
                                        ComC2 = random.randint(1,10)
                                        print("Computer Played:",ComC2)
                                        if UserC2 > 10:
                                            print("Error")
                                        if UserC2 == "":
                                            print("Error")
                                        if UserC2 < 1:
                                            print("Error")
                                            ComScore = ComScore + 10
                                            ComScore = ComScore - ComC2           
                                        if UserC2!= ComC2:
                                            ComScore = ComScore + ComC2
                                            print("Computer's Total:",ComScore)   
                                        if ComScore > Score:
                                            print("You Lost!")
                                            print("Your Score Is",Score)
                                            print("Computer's Score Is",ComScore)
                                            print("Thanks For Playing!")
                                            Game = False
                                            exit()
                                        if UserC2 == ComC2 and ComScore < Score:
                                            print("You Won!")
                                            print("Your Score Is",Score)
                                            print("Computer's Score Is",ComScore)
                                            print("Thanks For Playing!")
                                            Game = False
                                            exit()
                                        if Score == ComScore and UserC2 == ComC2:
                                            print("Tie")
                                            print("Your Score Is",Score)
                                            print("Computer's Score Is",ComScore)
                                            print("Thanks For Playing!")
                                            Game = False
                                            exit()
                                    
                if TossScore == TossComScore:
                    print("Tie of Scores")                   
        while Choice5 == 2:    
            Toss = random.randint(0,2)
            while Toss==2:
                print("Balling")
                print("Start")
                print("----------------------")
                while Game==True:
                    UserC = int(input("Enter Number: "))
                    ComC = random.randint(1,10)
                    print("Computer Played:",ComC)
                    if UserC > 10:
                        print("Error")
                    if UserC < 1:
                        print("Error")
                        ComScore = ComScore + 10
                        ComScore = ComScore - ComC    
                    if UserC == "":
                        print("Error")    
                    if UserC!= ComC:
                        ComScore = ComScore + ComC
                        print("Computer's Total:",ComScore)
                    while ComC == UserC:
                        print("Computer Out")
                        print("Computer's Score Is",ComScore)
                        while Game == True:
                            print("Now You are Batting")
                            print("----------------------")
                            while Game == True:
                                UserC2 = int(input("Enter Number: "))
                                ComC2 = random.randint(1,10)
                                print("Computer Played:",ComC2)
                                if UserC2 == "":
                                    print("Error")
                                if UserC2 < 1:
                                    print("Error")      
                                if UserC2 > 10:
                                    print("Error")
                                    Score = Score - UserC2
                                if UserC2!= ComC2:
                                    Score = Score + UserC2
                                    print("Your Total:",Score)   
                                if Score > ComScore:
                                    print("You Won!")
                                    print("Your Score Is",Score)
                                    print("Computer's Score Is",ComScore)
                                    print("Thanks For Playing!")
                                    Game = False
                                    exit()
                                if UserC2 == ComC2 and Score < ComScore:
                                    print("You Lost!")
                                    print("Your Score Is",Score)
                                    print("Computer's Score Is",ComScore)
                                    print("Thanks For Playing!")
                                    Game = False
                                    exit()
                                if Score == ComScore and UserC2 == ComC2:
                                    print("Tie")
                                    print("Your Score Is",Score)
                                    print("Computer's Score Is",ComScore)
                                    print("Thanks For Playing!")
                                    Game = False
                                    exit()                 
            while Toss==1:
                print("Batting")
                print("Start")
                print("----------------------")
                while Game==True:
                    UserC = int(input("Enter Number: "))
                    ComC = random.randint(1,10)
                    print("Computer Played:",ComC)
                    if UserC > 10:
                        print("Error")
                        Score = Score - UserC
                    if UserC == "":
                        print("Error")
                    if UserC < 1:
                        print("Error")       
                    if UserC!=ComC:
                        Score = Score + UserC
                        print("Your Total Score:",Score)   
                    while ComC == UserC:
                        print("Your Out")
                        print("Your Score Is",Score)
                        while Game == True:
                            print("Now You are Balling")
                            print("----------------------")
                            while Game == True:
                                UserC2 = int(input("Enter Number: "))
                                ComC2 = random.randint(1,10)
                                print("Computer Played:",ComC2)
                                if UserC2 > 10:
                                    print("Error")
                                if UserC2 == "":
                                    print("Error")
                                if UserC2 < 1:
                                    print("Error")
                                    ComScore = ComScore + 10
                                    ComScore = ComScore - ComC2           
                                if UserC2!= ComC2:
                                    ComScore = ComScore + ComC2
                                    print("Computer's Total:",ComScore)   
                                if ComScore > Score:
                                    print("You Lost!")
                                    print("Your Score Is",Score)
                                    print("Computer's Score Is",ComScore)
                                    print("Thanks For Playing!")
                                    Game = False
                                    exit()
                                if UserC2 == ComC2 and ComScore < Score:
                                    print("You Won!")
                                    print("Your Score Is",Score)
                                    print("Computer's Score Is",ComScore)
                                    print("Thanks For Playing!")
                                    Game = False
                                    exit()
                                if Score == ComScore and UserC2 == ComC2:
                                    print("Tie")
                                    print("Your Score Is",Score)
                                    print("Computer's Score Is",ComScore)
                                    print("Thanks For Playing!")
                                    Game = False
                                    exit()
                                    

                            


                    
                    
        
            

        

                            