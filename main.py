"""
#variables
print("Start our data science journey")

# data types

# numbers


a = 12
b = 12.865
c = 12/3
d = 12j # only can use j here not any other like x and y etc etc

print(type(b))

name = "danish nisar" 
age = 18
print("Hello my name is",name,"and my age is",age)

# or 

print(f"my name is {name} and my age is {age}")

# Question time
 #name1=int(input("hello what is your age"))
#print(name1)

print(10**10)
print(32%5)
print(32//5)
print(32/5)

aa=4
bb=12/3
print(aa==bb,"hi1")

aaa=4
bbb=12//3
print(aaa==bbb,"hi2")

print(type(aa)==type(bb))
print(type(aaa)==type(bbb))


print(ord("A"))
print(chr(65))

print("A" > "B")

# Some Questions on Conditional 
#  Q1. Accept two numbers and print the greatest between them.

a= int(input("Enter Ist Number"))
b= int(input("Enter 2nd Number"))

if a>b:
    print(f"the greater number is {a}")
elif a<b:
    print(f"the greater number is {b}")
else:
    print("Numbers are same")
# Q2. Accept the gender from the user as char and print the 
#respective greeting message 
#Ex - Good Morning Sir (on the basis of gender)


gender = input("Enter your gender as (M or F)")

if gender == "M" or gender == "m":
    print("Good Morning Sir")
elif gender == "F"or gender == "f":
    print("Good Morning Mam")

else:
    print("Invalid input")


# Q3. Accept an integer and check whether it is an even number or odd.

num = int(input("Enter an integer: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Q4. Accept name and age from the user. Check if the user is a valid voter or not.

user_name = input("Enter Your Name")

user_age = int(input("Enter Your Age"))

if user_age >= 18 :
    print(f"Yes! :) {user_name} You Can Vote")
else:
    print(f"No {user_name} You Can't Vote")

# Q5. Accept a year and check if it a leap year or not (google to find out what is a leap year) leap year comes after every 4 years 

year = int(input("Enter year"))

if year % 100!= 0 and year % 4 == 0 or year % 100 == 0 and year % 400 == 0:
    print(f"Yes {year} is a leap year")
elif year % 4 != 0:
    print(f"No {year} is not a leap year")
else:
    print("Enter valid year")

# Range and for loop

a=range(1,20,1)
for i in a:
    print(i)
    # or

    for i in range(2,35,2):
        print(i)

# go from 17 to -3

for i in range(17,-4,-1):
    print(i)


    # lets print a table of 5 
for i in range(1,11,1):
    print(f"5 x {i} = {5*i}")

# Loops for strings 

a = "Danish Nisar Kumar"

print(len(a)) # to know the length of our string

for i in range(0,len(a),1):
    print(a[i])

# or 

for i in a:
    print(i)


# Question from the for loop
# Q1 Accept an integer and Print hello world n times

a = range(1,int(input("Enter the Number:-"))+1,1)

for i in a:
   print(f"{i}:Hello World")

# Q2 Print natural number up to n

n = int(input("Enter the number: "))

if n > 0:
    for i in range(1, n + 1):
        print(i)
else:
    print("Enter a valid natural number (greater than 0)")

# Q3 Reverse for loop. Print n to 1

n = int(input("Enter the number: "))

if n >0 :
    for i in range(n,0,-1):
        print(i)

    else: print("invalid no.")


# Q4 Sum up to n terms

n = int(input("Enter the number:- "))
sum=0
for i in range(1,n+1):
    sum +=i
print(sum)

# Q5 Factorial of a number

n = int(input("Enter the number:- "))
factorail=1
for i in range(n,1,-1):
     factorail*=i
print(factorail)

# Q6 Print the sum of all even & odd numbers in a range separately

n = int(input("Enter the number:- "))
sum_even=0
sum_odd=0

if n> 0:
    
    for i in range(1,n+1):
         if i % 2 == 0:
            sum_even += i
         else:
            sum_odd += i

    print(f"Sum of even numbers = {sum_even}")
    print(f"Sum of odd numbers  = {sum_odd}")

else:
    print("Enter a natural number (greater than 0).")
    


#Q7 Print all the factors of a number



n = int(input("Enter the number:- "))

for i in range(1,n+1,1):
    if n%i==0:
        print(i)


# Q8 Accept a number and check if it a perfect number or not. 
#A number whose sum of factors is equal to the number itself 
#Ex -  6 = 1, 2, 3 = 6
n = int(input("Enter the number:- "))

perfect_no=0

for i in range(1,n+1,1):
    if n%i==0:
        perfect_no+=i
if perfect_no==n*2:
         print("yes it is a perfect no.")
else:
         print("no it is not perfect no.")

# Q9 Check wether the number is prime or not

n = int(input("Enter Your No:- "))
prime_checker=True

if n >0:
    for i in range(2,n,1):
        if n%i==0:
            prime_checker=False
            break
    if prime_checker:
        print(f"Yes! {n} is prime number")
    else:
        print(f"No! {n} is not a prime number")
 

    
else:
    print("Enter a valid natural number")

# Method 2nd 

n = int(input("Enter Your No:- "))
count=0
if n >0:
    for i in range(1,n+1,1):
        if n%i==0:
            count=count+1 # eg. n=3 factors 1,3 when 1 came count becomes 0=0+1-->1 and then when 3 came count becomes 1=1+1 --> 2
    if count==2:
        print(f"Yes! {n} is prime number")
    else:
        print(f"No! {n} is not a prime number")
else:
    print("Enter a valid natural number")

# Q10 Reverse a string without using in build functions.dont use .reverse and a[::-1] use with for loop 

a = "Danish Nisar Kumar"
b=""

for i in range(len(a)-1,-1,-1):
    print(a[i])
    b+=a[i]
print(b)

# q11 Check string is Pallindrome or not


a= "madam"
b=""
for i in range(len(a)-1,-1,-1):
    print(a[i])
    b+=a[i]
if a==b:
    print("yes palindrome")
else:
    print("not a palindrome")

# lec at 3 hrs 35 min
# Count all letters, digits, and special symbols from a given string Given: str1 = "P@#yn26at^&i5ve" 
 #Expected Outcome: 
 #Total counts of chars, digits, and symbols 
 #Chars = 8 
 #Digits = 3 
 #Symbol = 4

a = "Chysr$^&#7285v#$72bdg)(2_)"

char=0
digit=0
symbol=0

for i in a:
    if i.isdigit():
        digit+=1
    elif i.isalpha():
        char+=1

    else:
        symbol+=1
print(f"symbols are {symbol}, alphabets are {char}, and digits are {digit} in this string")

# While loop

a=1 # its like the i=x in js ist one in loop 
while a<=30: # condition runs when condition is true stops when condition became false --> 2nd thing in js look a like
     print(a)
     a+=1 # its like i++ in js to make aur work 

# Separate each digit of a number and print it on the new line

a=int(input("Enter any number:-"))
while a>0:
    print(a % 10) #---> that means 12345 remender when divided by 10 qutotent = 1234 and remender is 5 
    a= a // 10 # ----> means 12345 divides float by 10 means q = 1234.5 anf float divide makes decimal free so q ----> 1234 and now new number is 1234 and it runs till new number is becomes zero according to our condition 


# accept a number and reverse it

a=int(input("Enter any number:-"))

reverse_number=0

while a>0:
    reverse_number=reverse_number * 10 + a % 10 # eg 653 is no and we have to make it 356 we can do like -------> 0=0*10 + 3= 3
                        # and then folat divide seperates 3 the again 3=3*10 + 5= 35
                        # and again float division extracts 5 then ----> 35=35*10 + 6 = 356
    a = a // 10
print(reverse_number)


# Accept a number and check if it is a pallindromic number (If number and its reverse are equal)

a=int(input("Enter any number:-"))


reverse_number=0
original_number=a # making copy of original number in himself

while a>0:
    reverse_number=reverse_number * 10 + a % 10 # e.g 653 is no and we have to make it 356 we can do like -------> 0=0*10 + 3= 3
                        # and then folat divide seperates 3 the again 3=3*10 + 5= 35
                        # and again float division extracts 5 then ----> 35=35*10 + 6 = 356
    a = a // 10

if reverse_number==original_number:
    print(f"Yes! {original_number} is pallindromic number")
else:
    print(f"No! {original_number} is not pallindromic number")

# Create a random number guessing game with python

import random
number = random.randint(0,10) # 1 to 10 include 10 randint ---> is function to mean random integer

print(number)

count = 3

while count > 0:
         user_guess_number= int(input("Enter your single digit number"))
         if user_guess_number <0 or user_guess_number >10:
                 print("Enter number between 0 to 10 only 🥰")
                 continue

         elif user_guess_number!= number:
                 count-=1
                 print(f"Wrong guess! only {count} life remaining") 
                 if count==0:
                         print("You lose the game 🥲  the number was", number)
                         break
                
         elif user_guess_number== number:
                 print("yes correct guess you won the game 🎆")
                 break
         if user_guess_number <0 or user_guess_number >10:
                 print("Enter number between 0 to 10 only 🥰")

 # Functions 

 # make a function just like inbuild print() function

def print2(write): # function name and write is one parameter
    print(write)

print2("hello brother") # calling a function


# Functions and parametrs

def sum(a,b):
    print(a+b)

sum(12,12)

def divide(a,b):
    print(a/b)

divide(b=2,a=10) # already passe arguments and i give opposite also b ist and then a 2nd those are called keyword arguments

def multiply(a=1,b=2): # if i didnt pass arguments in calling those default values can be executed
    print(a*b)
multiply()

# Return

def sub(a,b):
    return a-b # return do it return the value that function give us to that line or pace where we call it eg we call it at line 426 so if we print calling the answer will print or we can keep that value store in variables
print(sub(2,3))

# return another example

def greet():
    return "asalamuaalikum"
greeting_in_islam=greet() # here we store the value in variable in greeting_in_islam

print(greeting_in_islam,"walikumasalam")
"""
# 4 hr and 30 min lect
