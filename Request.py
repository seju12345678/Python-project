from os import confstr
import requests
import json
from requests.api import request
url="http://saral.navgurukul.org/api/courses"
data=requests.get(url)
new_data=data.json()
with open("courses.json","w") as saral:
    json.dump(new_data,saral,indent=4)
i=0
while i<len( new_data["availableCourses"]):
    print(i+1,new_data["availableCourses"][i]["name"],new_data["availableCourses"][i]["id"])
    i=i+1
courses_name=int(input("enter the input1  :-"))
print(new_data["availableCourses"][courses_name-1]["name"])
course_id=new_data["availableCourses"][courses_name-1]["id"]
print(courses_name)

a=input("if you want to continue with this course say yes otherwise say no, yes/no:").lower()
if a=="no":
    i=0
    while i<len( new_data["availableCourses"]):
        print(i+1,new_data["availableCourses"][i]["name"],new_data["availableCourses"][i]["id"])
        i=i+1       
url1="http://saral.navgurukul.org/api/courses/"+str(new_data["availableCourses"][courses_name-1]["id"])+"/exercises"
data1=requests.get(url1)
new_data1=data1.json()
with open("child.json","w") as saral1:
    json.dump(new_data1,saral1,indent=4)
j=0    
for i in new_data1["data"]:
    print("",j+1,i["name"])
    if new_data1 ["data"][j]["childExercises"]== []:
        slug=(new_data1["data"][j]["slug"])
        print("    1.",slug)
    else:
        k=0
        while k<len(new_data1["data"][j]["childExercises"]):
            child=new_data1["data"][j]["childExercises"][k]["name"]
            print("   ",k+1,".",child)
            # print(j+1,new_data1["data1"][j]["name"])
            k=k+1
    j=j+1
print("")
topik_no=int(input("choose exercise which you want :-"))
serial_no=0
for i in new_data1["data"]:
    serial_no=+1
    if topik_no==serial_no:
        print("")
c=input("if you want to continue with this exercise then say yes otherwise no: ")
if c=="yes":             
    l=0
    list1=[]
    while l<len(new_data1["data"][topik_no-1]["childExercises"]):
        print("  ",l+1,new_data1["data"][topik_no-1]["childExercises"][l]["name"]) 
        slug=(new_data1 ["data"][topik_no-1]["childExercises"][l]["slug"])       
        url2=("http://saral.navgurukul.org/api/courses/"+str(course_id)+"/exercise/getBySlug?slug="+slug)
        url3=requests.get(url2)
        url4=url3.json()
        with open("selebarse.json","w")as a:
            json.dump(url4,a,indent=4)
            list1.append(url4["content"])
        l=l+1 
    user_choie_ques = int(input("enter a question number which you want: "))-1
    print(list1[user_choie_ques])
    while  user_choie_ques>=0:
        choose_previous_or_next = input("enter where you want to go previous or next: ").lower()
        if choose_previous_or_next == "p":
            user_choie_ques-=1
            print(list1[user_choie_ques])
        elif choose_previous_or_next == "n":
            if user_choie_ques == len(list1)-1:
                print("no more question exuercise ")
                break
            user_choie_ques+=1
            print(list1[user_choie_ques])
        else:
            print("input is not valid")
    else:
        print("page not found")