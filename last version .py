from random import shuffle
#using functions to ask name and using .isalpha
def greet():              
    global name 
    while True:
        name = input("Please enter your name here : ")
        if name.replace(' ','').isalpha():
            break 
        print("The data type you have used is invalid data type. (Please enter your name in alphabets only.)\n")


#Asking user if they want to see rules.
def rule():
    rule = input("\nDo you want to read the rules or continue without the rules? \nPress Y to learn the rules or any other key to continue without knowing the rules : ").lower()
    rule = rule.replace(' ','')
    if rule == "y" or rule == "yes" or rule == "okay":
        print("\nThe quiz is easy \n1. Enter the answer in a,b,c,d.\n2. You are not allowed to use cheat.")
        print("You may continue.")

#Asking for STATUS, if they want to play.
def status():
    status = input("\nAre you ready to play? :  ").lower()
    status = status.replace(' ','')
    if status == "y" or status == "yo" or status == "yes":
        print("\nThank you!")
    else:
        print("\nThank you, please join again when you are ready!.")
        exit()

def rounds():
    global r , total
    while True:
        try:
            r = int(input("How many rounds do you want to play? : "))
            if 0<r<=7:#this only allows 0-10 
                break
            else:
                print("ERROR 1-7 only")
        except:
            print('Please enter rounds in numbers only (The max number of rounds is 7!)')
            

    
        
    total=r

    
#using dictionary for the question 
gkquiz =[
[
    "\nWhat cpu uses LGA",
    {'answer':'a','option':'a)intel\nb)AMD\nc)Exnoys\n'}
    ],
[
    "\nwhat is the 24pin from the powersupply used for?",
    {'answer':'a','option':'a)Motherboard Power\nb)CPU power\nc)Graphics card power\nd)USB power\n'}
     ],
[
    "\nWhat is a M.2 SSD for?",
    {'answer':'B','option':'a)Run games\nb)Fast Storage\nc)For display\nd)For Gaming\n'}
     ],
[
    "\nWhich CPU brand uses pins on their cpus?",
    {'answer':'c','option':'a)LMD\nb)APPLE?\nc)AMD\nd)INTEL\n'}
     ],
[
    "\nWhat does RAM mean?",
    {'answer':'a','option':'a)Random Access Memory\nb)Random Access memus'}
     ],
[
    "\nWhat is a CPU used for",
    {'answer':'a','option':'a)processes the basic instructions that drive a computer\nb)Gaming\nc)Powers the pc\nd)Stores software\n'}
     ],



]

q_number=[i for i in range(len(gkquiz))] #asking the user if they want to play the quiz again.
shuffle(q_number)

index = 0
score = 0
optnum = 0

   
        


#def functions
greet()
rounds()
rule()
status()



while True:
    while r>0:#using for range 
        data = gkquiz[q_number[0]]
        q = data[0]
        data = data[1]
        answer = data['answer']
        option = data['option']

        print(q)#printing questions
        print(option)#printing options
        while True:
            user_answer = input("Please enter your answer here : ").lower().replace(' ','')
            if user_answer == 'a' or user_answer == 'b' or user_answer == 'c' or user_answer == 'd':
                if user_answer == answer: 
                    print("NICE ONE!")
                    score +=1 #Showing score and it will increase as the user gains more.
                    print("Your score is",score)
                else:

                    print("Sorry the option you have chosen is not right. The answer is ",answer)
                    print("Your score is",score)
                    

                del q_number[0] #using del so question wont repleat ever
                r-=1
                break
            else:
                print("Please enter the alphabet for the chosen option") 
                
    print(name,"Your score is ",score,"out of",total) #Show the score and stats for the end of the quiz.
    print("The precentage of the score is",(round(score/total*100,2)),"%")#showing percentage of the score they got

