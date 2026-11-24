aura = 100
game_running = True
room = "starting"

print("===================================")
print("       THE BANGKOK AURA GAME")
print("===================================")
print("Your starting aura is:", aura)

while game_running:
    if room == 'starting':
        print("\nYou are in a uniform senior only school in bangkok.")
        print("what do you do?")
        print("1. Talk to them, Press 1")
        print("2. FEELL the vibe:), Press 2")
        print("3. Ignore, Press 3")

        answer = input("1-3: ")

        if answer == "1":
            aura += 20
            print("\nYou gained 20 aura")
            room = "communication"

        elif answer == "2":
            aura += 50
            print("\nYou gained 50 aura! papa is proud of you!")
            room = "vibes"

        elif answer == "3":
            aura -= 30
            print("\nYou deservingly lose 30 aura. scaredy cat")
            room = "isolation"

        else:
            print("Invalid choice")

        print("Current aura:", aura)
        
    elif room == "communication":

        print("\nYou creeply approach a senior citizen")

        if aura >= 100:
            print("You have got a senior's number")
            print("you have awkwardly become friends with an 80 year old grandpa")
            print("to be determined...")
        else: 
            print("You don't have enough aura.")
            print("please turn 360 degrees")
            print("you lose sucker")

        game_running = False
    
    elif room == "isolation":

        print("\nyou are walking solooooo.")
        print("sorry man up your social skills.")
        aura = 0
        print("YOU LOSE GET OUTTT.")

        game_running = False


        
    elif room == "vibes":

        print("\nYou made a GREAT choice.")
        print("To your left, there is Kim Jong Un.") 
        print("To your right, there is Xi Jingping")
        print("choose one to meet and determine the future of the world. choose wisely")
        print("1. skinny kim john un:)")
        print("2. captain america xi jingping")

        answer = input("1-2: ")

        if answer == "1":
            aura += 30
            print("\n you gained 30 aura.")
            room = "big kimmy"

        elif answer == "2":
            aura += 30
            print("\nyou gained 30 aura.")
            room = "xie xie noodle house."

        else:
            print("watchu doing here")
            continue
        
        game_running = False

    elif room == "xie xie noodle house":
            
        print("You will help me conquer Thailand, Hong kong, and india.")
        print("please choose an option")
        print("1. Tell him you are the Ceo of taiwan")
        print("2. Ask him for the wifi password.")
        print("3. Tell him your mommy said no") 

        answer = input ("1-3: ")
                
        if answer == "1":
            aura -= 50
            print("\nXi Jinping is fired up")
            print("chinese airstrike has been ordered to take you.")
            print("you lose whoop whoop")

        elif answer == "2":
                aura -= 30
                print("\nHe says: Did you FORGET??")
                print("there is no internet or ai in china")
                print("deepseak ai crushes you.")
                print("you lose")

        elif answer == "3":
            aura += 150
            print("\n")
            print("mama say no.")
            print("he is heartbroken.")
            print("YOU WIN!")

        else: 
            print("whatchu doing here")
            continue

        game_running = False



    elif room == "big kimmy":

            print("\nYou are trapped in my country forever")
            print("to escape, please choose an option:")
            print("1. Call ICE and donald trump")
            print("2. Inform him that he looks like snorlax")
            print("3. Tell him south korea has better kimchi")
            print("4. Steal all the skincare")


            answer = input ("1-3: ")

            if answer == "1":
                    aura -= 100
                    print("\nThat is impossible")
                    print("you lose whoop whopp")

            elif answer == "2":
                    aura += 50
                    print("\nbig kimmy looks in the reflection of your forehead.")
                    print("he realizes you are right.")
                    print("smoke comes out his nose")
                    print("you cannot breathe")
                    print("you lose")

            elif answer == "3":
                    if aura >=150:
                        aura +=50
                        print("\nbig kimmy stares at you")
                        print("you can see his triple chin")
                        print("south korean army comes to save you")
                        print("you win!")
                    else:
                        aura -=50
                        print("\nbig kimmy is NOT happy")
                        print("he tickles you")
                        print("you lose.")

            elif answer == "4":
                    aura += 200
                    print("\nhe tries to stop you but")
                    print("your guts are bigger than his")
                    print("after 67 days")
                    print("you get drafted to bts")
                    print("YOU WIN!")
                    
            else: 
                    print("what are you doing here")
                    continue

            game_running = False
            
     print("\n==============================")
     print("        GAME OVER")
     print("==============================")
     print("Final aura:", aura)

     if aura >= 175:
        print("FINAL RANK: 67 AURA LORD")
    elif aura >= 100:
        print("FINAL RANK: RIZZLER")
    elif aura >=50:
        print("FINAL RANK: AI")
    else:
        print("FINAL RANK: CHUD")

    print("============================")
    print("     like and subscribe")
    print("============================")

                    


    
        
        





