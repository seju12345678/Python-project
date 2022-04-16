import json
user_choice=input("Do you want to Login/Signup?")
dic={}
dic1={}
dic2={}
a=[]
b=open("Login/Signup/userdetails.json","r+")
c=b.read()  #strinf
if user_choice=="signup":
    username=input("enter the name :")
    password=input("enter the password and  password length should be 6 or greater than 6 : " )
    confirm_password=input("enter password again :")
    if password!=confirm_password: 
        print("Both password are not same")
    else :
        if len(password)>=6 :
            dic1["username"]=username
            dic1["password"]=password
            a.append(dic1)
            dic["user"]=a
            if username in c :
                print(" Username already exists")
            else:
                print("Congrats",username," You are Signed up successfully")
                Description=input("enter your description :")
                Birth_Date=input("enter your D.O,B :")
                Hobbies=input("enter your hobby :")
                Gender=input("Enter M/F :")
                dic2["description"]=Description
                dic2["dob"]=Birth_Date
                dic2["hobbies"]=Hobbies
                dic2["gender"]=Gender
                dic1["profile"]=dic2
                d=open("Login/Signup/userdetails.json","a")
                json.dump(dic,d,indent=4)
        else:
            print("Create some strong password please")  
else :
    username=input("enter the name :")
    password=input("enter the password :")
    if username and password in c :
        print(username,"You are logged in successfully")
    else :
        print("invalid username or  password")





























































