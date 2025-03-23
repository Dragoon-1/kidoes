import random,os
from time import sleep as s
clear = lambda: os.system('cls')

    
def sps():
    print("Welcome to Stone Paper Scissor Game^_^\n ")
    print("Rules:\n1.stone kills scissor\n2.scissor kills paper\n3.paper kills stone\n")
    print("Options:\n1.play with friend\n2.play with computer")
    how=int(input("Enter the option number:"))
    n=int(input("enter the number of rounds:"))
    clear()
    print("---------------------------------Stone Paper Scissor---------------------------------")
    print("options:\n1.stone\n2.paper\n3.scissor")
    wl={'p1':0,'p2':0}
    for i in range(n):
        if how == 1:
            p1=int(input("enter player 1 choice: "))
            p2=int(input("enter player 2 choice: "))
        elif how == 2:
            p1=int(input("enter player 1 choice: "))
            p2=random.randint(1,3)
        print('-------------------------------------------------------------------')
        if p1==p2:
            print("Draw, both players chose the same option\n")
        
        elif p1==1 and p2==3 or p1==2 and p2==1 or p1==3 and p2==2:
            print("Player 1 wins\n")
            wl['p1']+=1
        
        elif p2==1 and p1==3 or p2==2 and p1==1 or p2==3 and p1==2:
            print("Player 2 wins\n")
            wl['p2']+=1

        else:
            print("Invalid input\n")
            
    print('-------------------------------------------------------------------')
    s(3)
    clear()
    s(2)
    if wl['p1']>wl['p2']:
        print("Player 1 wins the game\n")
    elif wl['p1']<wl['p2']:
        print("Player 2 wins the game\n")
    else:
        print("Match Draw\n")
    print("-------------------------------------------------------------------------------------------------")
    s(2)
    clear()
    
def ng():
    print("---------------------------------Number Guessing Game---------------------------------")
    pnum=int(input("Enter the number between 1 to 10:"))
    num=random.randint(1,10)
    if pnum==num:
        print("You guessed it right\n")
    elif pnum+1==num or pnum-1==num:
        print("You were to close\n")
    elif pnum+2==num or pnum-2==num:
        print("You were close\n")
    else:
        print("You loose\n")
    s(3)
    clear()
    
    
def mq():
    print("◤------------------------------------------------------------------------◥")
    print("--------------------Welcome to Math Quiz Game^_^---------------------------\n")
    wl={'right':0,'wrong':0}
    for i in range(10):
        n1=random.randint(1,100)
        n2=random.randint(1,100)
        op=random.choice(['+','-','*','/'])
        if op=='+':
            ans = n1+n2
        elif op=='-':
            ans = n1-n2
        elif op=='*':
            ans = n1*n2
        elif op=='/':  
            ans = n1/n2
        pans=input(f"{i}.  {n1} {op} {n2} = ")
        if int(pans)==ans:
            print("Correct\n")
            wl['right']+=1
        elif op=='/' and int(pans)==round(ans,2):
            print("Correct\n")
            wl['right']+=1
        else:
            print("Wrong\n")
            wl['wrong']+=1
    clear()
    print(f"Right answers: {wl['right']}\nWrong answers: {wl['wrong']}\n")
    print(f"Your score is: {wl['right']}/{wl['right']+wl['wrong']}\n")
    print("-------------------------------------------------------------------------------------------------")
    s(3)
    clear()
            
if __name__ == "__main__":
    g=True
    while g==True:
        print("◤------------------------------------------------------------------------◥")
        print("-------------------------Welcome to Kidoes---------------------------")
        print("Options:")
        print("1. stone paper scissor")
        print("2. number guessing game")
        print("3. math quiz")   
        print("4. exit")
        wg=int(input("Enter the option number:"))
        clear()
        print("◤------------------------------------------------------------------------◥")
        if wg==1:
            sps()
        elif wg==2:
            ng()
        elif wg==3:
            mq()
        elif wg==4:
            print("Thank you for playing")
            g=False
        else:
            print("Invalid input or Something went wrong")
            s(3)
            clear()
        print("◣------------------------------------------------------------------------◢")