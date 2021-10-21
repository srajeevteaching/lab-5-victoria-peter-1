# Programmers: Peter & Victoria
# Course: CS151, Dr. Rajeev
# Date: 10/21/21
# Lab Number: 5
# Program Inputs: floor type, square footage
# Program Outputs: cost per square foot for floor type, cost of single room, cost of whole house

def type_price(a):
    p = 0
    if (a=="hardwood"):
        p += 1.39
        print("cost of hardwood is ", p)
        return p
    elif (a=="carpet"):
        p += 3.99
        print("cost of carpet is ", p)
        return p
    elif (a=="tile"):
        p += 4.99
        print ("cost of tile is ", p)
        return p
    else:
        print ("please input a valid floor tyoe")
        return p
def room_area(l,w):
    a=l*w
    return a
def dimensions():
    length = float(input("what is the length of this room? "))
    width = float(input("what is the width of this room? "))
    dimension = room_area (length, width)
    return dimension


room=1
total=0
type = input("What floor type would you like room? ")
type = type.lower().strip()
while (room<=5):
    price = type_price(type)
    if (price !=0):
        area = dimensions()
        room_price = price*area
        total += room_price
        print("price of room ", room, " is: ", room_price)
        type = input("What floor type would you like room? ")
        type = type.lower().strip()
        room += 1
    else:
        type = input("What floor type would you like room? ")
        type = type.lower().strip()






