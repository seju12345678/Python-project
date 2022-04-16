print("                 Hello!!🙏                    ")
print("    WELCOME TO KBC-Kaun Banega Crorepati🎯    ")

def questions():
    list1=["How many continents are there?", 
    "What is the capital of India?",
    "NG mei kaun se course padhaya jata hai?"]
    return list1
questions_new=questions()

def options():
    option=[["four","nine","seven","eight"],
    ["chandigarh","Bhopal","chennai","Delhi"],
    ["Software engineering","Counseling","tourism","Agriculture"]]
    return option
options_new=options()

def solutions():
    solution=[3,4,1]
    return solution
solutions_new=solutions() 
i=0
c=0
j=0
sum_prize=0
while i<(len(questions_new)) and j<len(options_new):
    print("Your question is 👇")
    print(questions_new[i])
    z=0
    while z<len(options_new[j]):
        print(z+1,options_new[j][z])
        z=z+1
        
    if c==0:
        k=0
        Prize=10000
        
        lifeline=input("Do you want to use 50-50 lifeline✨??, Enter y or n= ")
        if lifeline=="y":
            c=c+1
            ans1=int(input("Please enter your answer option⟹ "))
            ans2=int(input("Please enter your second answer option⟹ "))
            if ans1==solutions_new[i] or ans2==solutions_new[i]:
                print("             Congratulations👏🏼🥳               ")
                print("Correct answer👏🏼✔️✔️, 🥳You win Rs= ", Prize, "💰")
                sum_prize=sum_prize+Prize
            else:
                print("Sorry😢, Wrong answer, you are out of the game now, Thank for being part of the game🙏")
                break
        elif lifeline=="n":   
            ans1=int(input("Please enter your answer option⟹ "))
            print(solutions_new[i])
            if ans1==solutions_new[i]:
                print("             Congratulations👏🏼🥳               ")
                print("Correct answer👏🏼✔️✔️, 🥳You win Rs= ", Prize, "💰")
                sum_prize=sum_prize+Prize
            else:
                print("Sorry😢, Wrong answer, you are out of the game now, Thank for being part of the game🙏")
                break
    else:
        print("You don't have lifeline now")
        ans1=int(input("Please enter your answer option⟹ "))
        
        print(solutions_new[i])
        if ans1==solutions_new[i]:
            print("             Congratulations👏🏼🥳               ")
            print("Correct answer👏🏼✔️✔️, 🥳You win Rs= ", Prize, "💰")
            sum_prize=sum_prize+Prize
        else:
            print("Sorry😢, Wrong answer, you are out of the game now, Thanks for being part of the game🙏")
            break
    
    i=i+1
    j=j+1       
print("   Your total prize is : ",sum_prize)
print("          THANK YOU🙏KO")
        

     