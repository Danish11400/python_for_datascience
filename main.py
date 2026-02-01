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
"""

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
