#  Program to calculate discount base on given age
age = int(input("Enter your age: "))
ticket_price = eval(input("Enter ticket price: "))
if age < 18:
    if ticket_price >= 10:
        print("You are a minor and you get 20% discount")
        ticket_price = ticket_price - (ticket_price * 0.2)
    else:
        print("You are a minor but your ticket price is less than $10. No discount")
elif age >= 60:
    if ticket_price >= 20:
        print("You are a senior and you get 30% discount")
        ticket_price = ticket_price - (ticket_price * 0.3)
    else:
        print("You are a senior but your ticket price is less than $20. No discount")
else:
    print("You are an adult. No discount")

# ticket with 2 decimal places
print("Your ticket price is:", "{:.2f}".format(ticket_price))


# An other version witout using nested if
age = int(input("Enter your age: "))
ticket_price = eval(input("Enter ticket price: "))
if age < 18 and ticket_price >= 10:
    print("You are a minor and you get 20% discount")
    ticket_price = ticket_price - (ticket_price * 0.2)
elif age >= 60 and ticket_price >= 20:
    print("You are a senior and you get 30% discount")
    ticket_price = ticket_price - (ticket_price * 0.3)
else:
    print("You are an adult. No discount")

# ticket with 2 decimal places
print("Your ticket price is:", "{:.2f}".format(ticket_price))