marks = int(input("Enter your total_Marks/600 : "))
totalmarks = 600
grade = marks/totalmarks*100
if marks <= 600:
    print(grade)
else :
    print("Try once, You Enterd Above 600")

if grade >= 80 and grade <= 100 :
    print("Congrats! You are Distinction")
elif grade >= 60 and grade <= 80:
    print("Congrats! You are first class")
elif grade >= 40 and grade <= 60:
    print("Congrats! You are second class")
elif grade >= 35 and grade <= 40:
    print("Jast pass")
else : 
    print("Fail. Study well and Better luck next time")