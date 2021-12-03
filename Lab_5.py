# Programmers: Peter & Victoria
# Course: CS151, Dr. Rajeev
# Date: 10/21/21
# Lab Number: 5
# Program Inputs: floor type, square footage
# Program Outputs: cost per square foot for floor type, cost of single room, cost of whole house

# this function tells user the price per square foot of the type of floors they selected
def type_price(a):
    p = 0
    # price of floors if the user inputs hardwood
    if (a=="hardwood"):
        p += 1.39
        print("cost of hardwood is ", p, "per sq/ft")
        return p
    # price of floors if the user inputs carpet
    elif (a=="carpet"):
        p += 3.99
        print("cost of carpet is ", p, "per sq/ft")
        return p
    # price of floors if the user inputs tile
    elif (a=="tile"):
        p += 4.99
        print ("cost of tile is ", p, "per sq/ft")
        return p
    # for if the user inputs an invalid floor type
    else:
        print ("please input a valid floor type")
        return p
# calculates the area in square feet of the room
def room_area(l,w):
    a=l*w
    return a
# asks for the dimensions of the room
def dimensions():
    length = float(input("what is the length of this room? "))
    width = float(input("what is the width of this room? "))
    # calls the room area function with the inputted length and width
    dimension = room_area (length, width)
    return dimension

# main function
# initializing
room=1
total=0
# loops through 5 times for each of the different rooms
while (room<=5):
    # asks user for the floor type
    type = input("What floor type would you like room? ")
    # makes sure that input will work no matter of upper case or spaces
    type = type.lower().strip()
    price = type_price(type)
    # to make sure it will only ask for other inputs if the floor input is valid
    if (price !=0):
        area = dimensions()
        # calculates the price for that room
        room_price = price*area
        # calculates total price for all rooms
        total += room_price
        # prints price for that room
        print("price of room ", room, " is: ", room_price)

        room += 1
    # will restart if floor input is invalid
    else:
        type = input("What floor type would you like room? ")
        type = type.lower().strip()
# prints total price for all rooms
print("total price: ", total)

