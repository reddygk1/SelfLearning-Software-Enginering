
print('Hello world')
name = "Madhvi"
""" if statement"""
if name is "reddy":
    print("Hello buddy")
elif name is "Lewi":
    print("hey Lewi")
elif name is "Aidan":
    print ("You what M9")
else:
    print("Who are you? you are not part of my squad")

    """ For loop"""

games = ["cricket", "soccer", "rugby", "tennis", "pool"]

for g in games:
    print(g)
    print(len(g))

print(len(games))
print("*******************************************")
""" For loop in range"""
"""The first two numbers are indicators for begin and start, the next number is the interval"""
for x in range(10, 20, 3):
    print(x)
    """ For loop break and continue"""

myNum = 33
for x in range(50):
    if x is myNum:
        print(x, " this is your number")
    else:
        print(x)

myNums = [12, 15, 18, 20]
for x in range(21):
    if x in myNums:
        continue
    print(x)



'''Functions'''

def areaOfSquare(side):
    area = side * side
    print("Area of the square is ", area)
areaOfSquare(10)


def datingAge(age):
    allowedAge = age/2 + 7
    return allowedAge

print(datingAge(40))


def health_calculator(age, apples_ate, cig_smoked):
    health = (100-age) + (apples_ate * 3) - (cig_smoked * 3.5)
    print(health)

myData = [34, 4, 0]

health_calculator(*myData)

classmates = {"Lewi": " Awesome coder", "Aidan": " Linux Guru", "Dan": " The Socialiser", "Emerson": " The silent master"}

for k, v in classmates.items():
    print(k + v)