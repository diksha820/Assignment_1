#Conditional Statements 
#1⦁	Write a program to check whether a number is positive or negative.
""" 
num=int(input("enter a number : "))
if num>=0:
    print("postive")
else:
    print("negative")


#2⦁	Write a program to check whether a number is even or odd. 
num=int(input("enter a number : "))
if num%2==0:
    print("even")
else:
    print("odd")


#3⦁	Write a program to find the greater number between two numbers. 
a=int(input("enter a number : "))
b=int(input("enter a number : "))
if a>b:
    print(" a grater number",a)
else:
    print("b is greater",b)



#4⦁	Write a program to check whether a person is eligible to vote (age ≥ 18). 
age=int(input("enter a number : "))
if age>=18:
    print("eligible for vote")
else:
    print("not eligible for vote ")


#5⦁	Write a program to check whether a number is divisible by 5. 
num=int(input("enter a number : "))
if num%5==0:
    print("divided by 5")
else:
    print("not divided ny 5")



#6⦁	Write a program to check whether a given year is a leap year or not. 
year=int(input("enter a number : "))
if year%4==0:
    print("this is a leaf year")
else:
    print("this is not leap year")
"""


#7⦁	Write a program to check whether a character is a vowel or a consonant. 
ch = input("enter a number : ")
if ch in "aeiouAEIOU":
    print("vowel")
else:
    print("consonant")


#8⦁	Write a program to find the largest among three numbers. 
a=int(input("enter a number : "))
b=int(input("enter a number : "))
c=int(input("enter a number : "))
if a>b and a>c:
    print("a largest")
elif b>c:
    print("b largest")
else:
    print("c is largest")
#9⦁	Write a program to assign grades based on marks: 
"""
	90 and above → A 
	75 to 89 → B 
	50 to 74 → C 
	Below 50 → Fail 
"""
marks=int(input("enter marks : "))
if marks >=90:
    print("grade A")
elif marks>=75:
    print("grade b")
elif marks>=50:
    print("grade c")
else:
    print("fail")
#10⦁	Write a program to check whether a number is within the range of 1 to 100.


