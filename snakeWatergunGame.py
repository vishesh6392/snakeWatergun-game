import random
playername=input("Enter your name:")
playerstr=input("Enter your choice: ")
if(playerstr=='snake' or playerstr=='water' or playerstr =='gun'):
    dic={'snake':1,'water':0,'gun':-1}
    revdic={1:'snake',0:'water',-1:'gun'}


    computerchoice=random.choice([1,0,-1])
    playerchoice=dic[playerstr]
    print(f"{playername} choose : {revdic[playerchoice]}\n computer choose: {revdic[computerchoice]}")
    if(computerchoice==playerchoice):
     print("Draw!, playagain")
    else:
    # if(computerchoice==1 and playerchoice==0):
    #     print(f"{playername } lose!")  
    # elif(computerchoice==1 and playerchoice==-1):#c-p=2--->analysis
    #     print(f"{playername } win!")  
    # elif(computerchoice==0 and playerchoice==-1):
    #     print(f"{playername } lose!")  
    # elif(computerchoice==0 and playerchoice==1):#c-p=-1--->analysis
    #     print(f"{playername } win!")  
    # elif(computerchoice==-1 and playerchoice==1):
    #     print(f"{playername } lose!")  
    # elif(computerchoice==-1 and playerchoice==0):#c-p=-1--->analysis
    #     print(f"{playername } win!")
     if(computerchoice-playerchoice==2 or computerchoice-playerchoice==-1):
        print(f"Wow,{playername} ,you win!\n Game over,thankyou!")
     else:
        print("you lose!\nyou win!\n Game over,thankyou!")  
else:
  print("You choose wrong \n choose among [snake, water, gun]:")    


          
  



