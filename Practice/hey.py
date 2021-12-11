import os 
os.system("cls")
# for i in range(1,101):
#     if i%2==0 :
#         print(i)

#finding factors
# user = int(input("Enter number to find factors"))
# for i in range(1,user+1):
#     if user%i == 0 :
#         print(i)

#finding no of factor
# user = int(input("Enter number to find factors"))
# count = 0
# for i in range(1,user+1):
#     if user%i == 0 :
#         count = count + 1
# print(user," have ",count," factors")

#checking prime number
# user = int(input("Enter number :- "))
# count = 0
# for i in range(1,user+1):
#     if user%i == 0 :
#         count = count + 1
# if count == 2: 
#     print(user,"is a prime number")
# else :
#     print(user,"is not a prime number")

#checking perfect number
# user = int(input("Enter number : "))
# sum = 0
# for i in range(1,user):
#     if user%i == 0 :
#         sum = sum + i
# if sum == user :
#     print(user,"is a perfect number")
# else :
#     print(user,"is not a perfect number")

#3 , 6 , 12 , 24 , 48
# c=3
# for i in range (1,10):
#     print(c)
#     c = c * 2

#0 , 3 , 8 , 15 , 24
# s = 0
# for i in range(1,11):
#     s = i**2 -1
#     print(s)

#finding factorial
user = int(input("ENTER A NUMBER : "))
f = 1
for i in range(1,user + 1):
    f = f * i
print(f)





