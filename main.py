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

# Data structures (DS)

# 1-----> List e.g like arrays

a=[1,2,4,755,33,6,43,54.42,True,"Hello",print(),"Good"] # we can change the values and other info in ------> i book in page 30!!!!!
print(a[0:6:1])

print(a[-1:-3:-1]) # from backside starts at -1 means at good and ends at -3 means hello but not include hello and steps -1



a=[1,43,5,7553,2,340,2.42]

for i in range(0,len(a),1): # acessing index
    print(a[i])

a=[1,43,5,7553,2,340,2.42]

for i in a:  # direct access
    print(i)

a = [1,3,4,5]

a.append(6) # at last add this
a.append(7)

a.insert(1,2) # at 1 indec add 2

a.extend([8,9])

a.insert(0,2)

a.remove(2) # where ist 2 came remove that

popped_item=a.pop(3) # at index 3 which value is their you can store that in any variable and that value is removed from the list also


count=a.count(5) # how many times 5 repeat in the list
print("hello",count)

a.reverse()
print(a)



# Questions on list

# Q1 Print positive and negative elements of an List

question_list = [3,-14,-7,-3,2,5,90,-54.37,5,8,]

for i in question_list:
    if i>0:
        print(f"{i} is positive")
    elif i<0:
        print(f"{i} is negative")



#Q2 Mean of List elements

question_list = [3,-14,-7,-3,2,5,90,-54.37,5,8]


mean=0
for i in question_list:
    mean+=i
print(f"mean of given list is {mean/len(question_list)}")



# Q3 Find the greatest element and print its index too

question_list = [300,3,-14,-7,-3,2,5,90,-54.37,5,8]

greter_number=question_list[0]
for i in range(len(question_list)):
    if question_list[i] > greter_number:
        greter_number = question_list[i]
print(f"the greater number is {greter_number} at index number {question_list.index(greter_number)}")



# Q4 Find the second greatest element


# Thats my way to do that question but its bulky what if i have to find 100th largest value i find largest and then remove it from the list then again find largest which ultimately becomes the second largest value 

question_list = [300,3,-14,-7,-3,2,5,90,-54.37,5,8]

greter_number=question_list[0]


for i in range(len(question_list)):
    if question_list[i] > greter_number:
        greter_number = question_list[i]
question_list.pop(question_list.index(greter_number))



second_largest_number = question_list[0]

for i in range(len(question_list)):
    if second_largest_number < question_list[i]:
        second_largest_number=question_list[i]
print(f"second largest number in the list is {second_largest_number}")



# Q4 Find the second greatest element

#  Now its sir's way of doing the question bt i will write code of my own just get the idea 
# and i think its best wy to get the answer -----> so thye approach is that take
#  two variables largest and second largest then value at index 0 = both variables then loop runs if loop
# find big value than largest then it becomes the largest and alrady
# largest becames the second largest value------->


question_list = [15,3,-14,-7,-3,2,38,5,90,-54.37,5,8]

largest_value=question_list[0]
second_largest_value=question_list[0]

for i in range(len(question_list)):
    if question_list[i] > largest_value:
        second_largest_value = largest_value
        largest_value = question_list[i]
    elif question_list[i] > second_largest_value: # to prevent if second largest was last index of the list then largest reach there but second largest cant ------>
        second_largest_value = question_list[i]

print(second_largest_value)



#Q5 Check if List is sorted or not.


question_list = [15,3,-14,-7,-3,2,38,5,90,-54.37,5,8]


for i in range(len(question_list)-1): # why -1?? -----> becoz i+1 if i=11 and then i+1 becomes 12 but we dont have index 12 so last element is no need to check becoz it gets already checked in i 
    if question_list[i] < question_list[i+1]:
        continue
    else:
        print("your list is not sorted")
        break
else:
    print("Your list is sorted ")  # why we write else outside becoz if not sorted runs then loop stops  and says list is not sorted yes !!!! and if not sorted not runs then loop continue to run and not sorted then automatically our ist is sorted then last else runs becoz we already know list is sorted becoz not sorted else dont run so we casually says ohhh not sorted doesnt runs ohh that means list is sorted so ok run list is sorted 🥲...
    


# Tuple eg. a = (1,2,3,4)

a = (1,2,3,4,5,"hello",6.6) # only change in tuple and list in list we change any value but in tuple we cant change any value its immutable

# and in tuple only two methods .index() -----> to find index and .count() ------> to find how many times something is in tuple

# we can unpack tuple eg.

a,b,c,d = (1,2,"hello",4)

# Now a =1 b=2 c=hello d=4

print(type(a))  # now type of a----> integer not tuple becoz now it unpacks and a=1 not tuple
print(type(c))  # Now typeof c ------> string becoz its now equal to "hello"



# Set e.g ----> a = {1,2,3,4,"hello",5.6}


a = {1,2,3,4,"hello",5.6,(10,20,30)} # no duplicates and not ordered----> like a[0], a[1] means not like index acessing  

# And we can store tuples also in set
print(a)



a = {1,2,3,4,5}
b = {4,5,6,7,8}

union_set = a.union(b) # all values of a and b but same shows only once
print(union_set)
            # or
union_set_shortcut = a | b
print(union_set_shortcut)



intersection_set = a.intersection(b) # same values
print(intersection_set)
            # or
intersection_set_shortcut = a & b
print(intersection_set_shortcut)



difference_set_of_a_wrt_b = a.difference(b)
print(difference_set_of_a_wrt_b)
            # or
difference_set_of_a_wrt_b_shortcut = a - b
print(difference_set_of_a_wrt_b_shortcut)


difference_set_of_b_wrt_a = b.difference(a)
print(difference_set_of_b_wrt_a)
            # or
difference_set_of_b_wrt_a_shortcut = b - a
print(difference_set_of_b_wrt_a_shortcut)



symmetric_diff = a.symmetric_difference(b) # shows both a and b differce values
print(symmetric_diff)
            # or
symmetric_diff_shortcut = a ^ b
print(symmetric_diff_shortcut)



# Dictonaries eg . a = {1:"hello","name":"danish", "age":18}
# so in dictionaries is like sets but have keys and values just like
# objects in js

a = {"greetings":"hello","name":"danish", "age":18,786:"bismillah"}

a["greetings"] = "Assalamuaalikum"  # change key_value not key
print(a)

a.update({"address":"Okai kulgam"}) # add some key and value in dictionary UPDATING
print(a)

a["fav_food"] = "beef_biryani" #-----> Look here python says hey there is no key fav_food and it creats that key and if we give value it also then it gives that value to that key also so it is called CREATING  
print(a)


del a[786] # it deletes key and value both key name is 786
print(a)

"""

a = {"greetings":"Assalamuaalikum","name":"danish", "age":18,786:"bismillah"}

for i in a:
    print(f"now i= key like----> {i} and key_value is a[i] like---->{a[i]}")
                #or
print("<-------------------------------------------------------->")

for i in a.values():
    print(i) # now we can acess direct values only not keys

    #or
a = {"greetings":"Assalamuaalikum","name":"danish", "age":18,786:"bismillah"}
  
for keys, values in a.items():  # here keys and values we can use differnt names like keylal etc , value_khor etc just like js

    print(f"keys{keys} and values {values}")




# or to find methods of dictonaries and deep copy and shallow copy i will ad ss on the notes page of these...OK!!!!
