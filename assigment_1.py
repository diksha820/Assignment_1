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
	90 and above → A 
	75 to 89 → B 
	50 to 74 → C 
	Below 50 → Fail 

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
num=int(input("enter a number : "))
if num>=1 and num<=100:
    print("number a witin range")
else:
    print("number is outside range")
"""




#Python for Loop 
#1.	Write a program to print numbers from 1 to 10 using a for loop. 
"""
for i in range(1,11):
    print(i)


#2.	Write a program to print numbers from 10 to 1 in reverse order. 
for i in range(10,0,-1):
    print(i)
    

#3.	Write a program to print all even numbers between 1 and 20. 
for i in range(2,21,2):
    print(i)


#4.	Write a program to print all odd numbers between 1 and 20. 
for i in range(1,20,2):
    print(i)
    

#5.	Write a program to find the sum of numbers from 1 to 100. 
total=0
for i in range(1,101):
    total += i
print("sum",total)


#6.	Write a program to print the multiplication table of a given number. 
num=int(input("enter a number : "))
for i in range(1,11):
    print(num,"x",i,"=",num*i)


#7.	Write a program using nested for loops to print pattern
for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()


#8.	Write a program to print each character of a string using a for loop. 
text=input("enter a string")
for ch in text:
    print(ch)


#9.	Write a program to find the factorial of a given number using a for loop. 
num=int(input("enter a number : "))
fact=1
for i in range(1,num+1):
    fact*=i
print("factorial",fact)


#10.	Write a program to print the following pattern:
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

    """


#Python while Loop:
#1. Write a program to print numbers from 1 to 10 using a while loop.
"""
i=1
while i<=10:
    print(i)
    i+=1


#2. Write a program to print numbers from 10 to 1 in reverse order using a while loop.
i=10
while i>=1:
    print(i)
    i-=1
    


#3. Write a program to print all even numbers between 1 and 20 using a while loop.
i=2
while i<=20:
    print(i)
    i += 2
    


#4. Write a program to print all odd numbers between 1 and 20 using a while loop.
i=1
while i<=20:
    print(i)
    i += 2
    


#5. Write a program to find the sum of numbers from 1 to 100 using a while loop.
i=1
total=0
while i<=100:
    total+=i
    i+=1
print(total)


#6. Write a program to print the multiplication table of a given number using a while loop .
num=int(input("enter a number : "))
i=1
while i<=10:
    print(num,"x",i,"=",num*i)
    i+=1


#7. Write a program to count the number of digits in a given number using a while loop.
num=int(input("enter a number : "))
count=0
while num>0:
    count+=1
    num//=10
print(count)



#8. Write a program to reverse a given number using a while loop.
num=int(input("enter a number : "))
reverse=0
while num>0:
    digit=num%10
    reverse = reverse * 10 + digit
print(reverse)
"""
#9. Write a program to find the factorial of a given number using a while loop.
num=int(input("enter a number : "))
fact=1
i=1
while i<=num:
    fact*=i
    i+=1
print(fact)
#10. Write a program to keep asking the user for a password until the correct password is entered.

password="diksha1234"
user=" "
while user !=password:
    user=input("enter a password : ")
print("asses granted")