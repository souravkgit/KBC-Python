from questions import QUESTIONS
def isAnswerCorrect(question, answer):
    return True if answer ==question["answer"]  else False 
def lifeline(ques):
    i=ques["answer"]
    print("as your lifeline deleted two of the options now you have to select from the given options:")
    if i==4 or i==3:
        print(f'\t\t\tOption 3: {ques["option3"]}')
        print(f'\t\t\tOption 4: {ques["option4"]}')
        reply = True
        while reply:
            ans = input('Your choice ( 3-4 ) : ')
            if ans=="lifeline":
                print("You Can't opt for lifeline anymore , please select from the remaining options : ")
            else:
                reply=False
    else:
        print(f'\t\t\tOption 1: {ques["option1"]}')
        print(f'\t\t\tOption 2: {ques["option2"]}')
        reply = True
        while reply:
            ans = input('Your choice ( 1-2 ) : ')
            if ans=="lifeline":
                print("You Can't opt for lifeline anymore , please select from the remaining options : ")
            else:
                reply=False
    return ans
def kbc(): 
    print("welcome to the Game of KBC .aao aur jeeto.to chaliye shuru krte h.")
    gameover=False
    i=0
    won=0
    minwon=0
    ll=1
    while not gameover:
        i+=1
        print(f'\tQuestion {i}: {QUESTIONS[i-1]["name"]}' )
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[i-1]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[i-1]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[i-1]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[i-1]["option4"]}')
        nhiliya=True
        while nhiliya:
            ans = input('Your choice ( 1-4 ) : ')
            if ans=="lifeline":
                if ll!=0 and i<15:
                    ans = lifeline(QUESTIONS[i-1])
                    ll-=1
                    nhiliya = False
                else:
                    print("You Can't opt for lifeline anymore , please select from the options : ")
            else:
                nhiliya=False
        if ans=="quit":
            print("Congrats , You Have Won "+str(won))
            break        
        if isAnswerCorrect(QUESTIONS[i-1], int(ans) ):
            won+=QUESTIONS[i-1]["money"]
            print('\nCorrect !')
            print("you have won : "+str(won)+" till now")
            if i==5:
                minwon=10000
                print("congo you have cleared first level now your minimum money you cane take to home is increased to 10,000")
            if i==11:
                minwon=320000
                print("congo you have cleared second level now your minimum money you cane take to home is increased to 3,20,000")
            if i==15:
                print("Congrats You Have Won This Game And Your Winning Amount Is "+str(won))
                break           
        else:
            print('\nIncorrect !')
            print("option"+str(QUESTIONS[i-1]["answer"]) +"is the correct answer")
            print("You Have Won"+str(minwon))
            gameover=True
kbc()
