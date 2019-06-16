# print("Hello World")
# print("*" * 10)

# format document on command pallet
# x = 1
# y = 2
# uni_price = 3

# print("Hello World")

# user input
# x = input("x: ")
# print(int(x))
# print(float(x))
# print(bool(x))

# x = 1
# if x + 1:
#     pass
# else:
#     pass

# name = " "
# if not name.strip():
#     print("name is empty")

# age = 22
# if 18 <= age < 65:
#     print("You are elegible")

# age = 22
# if age >= 18:
#     message = "Elegible"
# else:
#     message = "Not elegible"

# message = "Eligible" if age >= 18 else "Not elegible"
# print(message)

# for x in "Pyton":
#     print(x)

# for x in ['a', 'b', 'c']:
#     print(x)

# for x in range(0, 10, 2):
#     print(x)

# print(type(range(5000)))

# names = ["AJohn", "Mary"]
# found = False
# for name in names:
#     if name.startswith("J"):
#         print("Found")
#         found = True
#         break
# if not found:
#     print("Not found")

# names = ["AJohn", "Mary"]
# for name in names:
#     if name.startswith("J"):
#         print("Found")
#         break
# else:
#     print("Not found")

# guess = 0
# answer = 5
# while answer != guess:
#     guess = int(input("Guess: "))
# else:
#     pass

# def increment(number: int, by: int = 1) -> tuple:
#     return (number, number + by)


# print(increment(2))

# def multiply(*list):
#     total = 1
#     for number in list:
#         total *= number
#     return total


# print(multiply(2, 3, 4, 5))

# def save_user(**user):
#     print(user["id"], user["name"])


# save_user(id=1, name="admin")

# message = "a"


# def greet():
#     global message
#     message = "b"
#     print(message)


# greet()
# print(message)

# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print("start")
# print(multiply(1, 2, 3))
# print("finish")

def fizz_buzz(input):
    if(input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


print(fizz_buzz(7))
