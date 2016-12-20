'''
car = input("What kind of car do you need? ")
print("Let me see if i can find a " + car )

gust = input("How many prople are there for dinner?  ")
gust = int(gust)

if gust >= 8:
    print("you need to wait.")
else:
    print("there is table available ")





number = input("Enter a number, we will see if it is a multiple of 10.")
number = int(number)

if number % 10 == 0 :
    print("Number " + str(number) +" is a multiple of 10. ")
else:
    print("Number " + str(number) + " is not a multiple of 10. ")



while True :

    topping = input("What topping would you like on your pizza.")

    if topping == 'quit':
        break
    else:
        print ("topping " +topping + " added to your order.")



while True:
    age = input("How old are you?")
    age = int(age)

    if age <= 3 :
        print("your ticket is free.")
    elif age <= 12:
        print("your ticket price is $10.")
    elif age > 12:
        print("your ticket price is $15.")
    elif age == 'quit':
        break



sandwich_orders = ['pastrami','stake cheese','grilled cheese','pastrami','chicken parmesan','pastrami','meat ball']
finished_sandwich = []

print("Deli has run out off pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')


while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made you " + sandwich.title() + "." )

    finished_sandwich.append(sandwich)

print("\nThe following sandwich have been made.")
for f_sandwich in finished_sandwich:
    print(f_sandwich)



'''
responses = {}

polling_active = True

while polling_active :
    name = input('what is your name? ')
    response= input("what is your dream vacation ?")

    responses[name]= response

    repeat = input("would you like to keep going? (yes / no)")
    if repeat == 'no':
        polling_active = False

for name, response in responses.items():
    print(name.title() + " want to go to " + response)













