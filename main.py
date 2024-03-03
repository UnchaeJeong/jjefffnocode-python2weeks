'''
> github commit > push 하는 방법

pwd
git remote add origin https://github.com/UnchaeJeong/jjefffnocode-python2weeks.git
git add main.py
git commit -m 'commit success'
git push -u origin main
'''

# print("Hello world!")

# a = 2
# b = 3
# c = a + b
# print(c)

# 2.3 Recap - 1일차

# my_name = "nico"
# age = 12
# dead = False

# print("Hello my name is", my_name)
# print("and I'm", age, "years old")

# 2.4 Define Function  - 2일차

# print(True)
# print("Hello")
# print(12)

# print(True, "Hello", 12)

# def say_hello() :
#   print("hello how r u?")

# say_hello()
# print("hello wolrd")

# 2.5 Indentation - 2일차

# def say_hello() :
#   print("hello how r u?")

# def say_bye() :
#   print("bye bye")
#   say_hello()

# 2.6 Parameters and Arguments - 2일차

# def say_hello(name): # parameters
#   print("hello how r u?", name) # print에서 ","를 사용할 수 있음

# say_hello("nico")
# say_hello('lynn')
# say_hello('lewis')
# say_hello('ralph') #argument

# 2.7 Multiple Parameters - 2일차
# def say_hello(user_name, user_age) :
#   print("hello", user_name)
#   print("you are", user_age, "years old")

# say_hello("nico", 12)

# 2.8 Recap - 2일차

# def tax_calculator(money) :
#   print(money * 0.35)

# tax_calculator(150000000)

# # 2.9 Default Parameters - 2일차

# def say_hello(user_name="annonymous") :
#   print("hello", user_name)
# say_hello("nico")
# say_hello()

# def plus(a=0, b=0) :
#   print(a + b)

# plus(1,2)
# plus()

# # 2.10 Return Values - 3일차

# def tax_calc(money) :
#   return money * 0.35

# def pay_tax(tax) :
#   print("thank you for paying", tax)

# to_pay = tax_calc(15000000)
# pay_tax(to_pay)

# # 2.11 Return Recap - 3일차

# my_name = 'nico'
# my_age = 12
# my_color_eyes = "brown"

# print(
#     f"Hello I'm {my_name}, I have {my_age} years in the earth, {my_color_eyes} is my eye color"
# )

# def make_juice(fruit):
#   return f"{fruit}+🥤"

# def add_ice(juice):
#   return f"{juice}+🧊"

# def add_sugar(iced_juice):
#   return f"{iced_juice}+🍬"

# juice = make_juice("🍎")
# cold_juice = add_ice(juice)
# perfect_juice = add_sugar(cold_juice)

# print(perfect_juice)

# # 3.0 IF - 4일차

# # if condition:
# #   "write the code to run"

# if 10 > 5:
#   print("correct!")

# if 10 < 5:
#   print("correct!")

# a = 10
# if a == 10:
#   print("correct!")

# 3.1 IF and ELSE - 4일차

password_correct = False
if password_correct:
  print("Here is your money")
else:
  print("Wrong password")

winner = 10

if winner > 10:
  print("Winner is greater than 10")
elif winner < 10:
  print("Winner is less than 10")
else:
  print("Winner is 10")
