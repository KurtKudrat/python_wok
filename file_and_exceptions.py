
'''
filename = 'python_text.txt'
# reading the entire file
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)


#reading the file line by line
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

#store the file in a list
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())


#working with a file's content
with open(filename) as file_object:
    lines = file_object.readlines()

read_line = ''
for line in lines:
    read_line += line.rstrip()

print(read_line)


user_name = input('please inter your name.')

with open('user_name.txt','w') as file_object:
    file_object.write(user_name)





while True :
    gust_name = input('please enter your name.')
    print(gust_name.title() + ' ,Welcome to the party.')

    with open('user_name.txt','a') as file_object:
        file_object.write(gust_name  + '\n')

    if gust_name == 'stop':
        break






while True :
    gust_name = input('Why do you like programing')

    with open('user_name.txt','a') as file_object:
        if gust_name == 'stop':
            break
        file_object.write(gust_name  + '\n')




# Addition ValueError

while True:
    num_1 = input("please enter the first number.")

    if num_1 == 'q':
        break

    num_2 = input('please enter the second number.')

    if num_2 == 'q':
        break

    try:

        answer = int(num_1) + int(num_2)

    except ValueError:
        print('please enter the valid number.')
    else:

        print(answer)






def read_txt(filename):
    try:

        with open(filename) as f_obj:
            content = f_obj.read()
            print(content)
    except FileNotFoundError:
        #print('File ' + filename + ' dose not exist')
        pass
read_txt('cat.txt')
read_txt('dog.txt')




#count the phrase


def count_the_phrase(filename):

    with open(filename) as f_obj:
        content = f_obj.read()

        count_num = content.lower().count('the')
        print(count_num)





count_the_phrase('Adventures of Huckleberry Finn.txt')






# store data as Json file
import json

file_name = 'favorite number.json'

favorite_number = input('what is your favorite number?')

with open(file_name,'w') as f_obj:
    json.dump(favorite_number,f_obj)


with open(file_name) as f_obj:
    favorite_number = json.load(f_obj)
    print("I know your favorite number is " + favorite_number )




# put tow code together

import json

file_name = 'favorite number.json'

try:
    with open(file_name) as f_obj:
        favorite_number = json.load(f_obj)

except FileNotFoundError:

    favorite_number = input('what is your favorite number?')
    with open(file_name, 'w') as f_obj:
        json.dump(favorite_number, f_obj)
        print("we will remember you when you come back, " + favorite_number + "!")

else:

    print("I know your favorite number is " + favorite_number)


'''


import json

def get_stored_username():

    file_name = 'username.json'

    try:
        with open(file_name) as f_obj:
            user_name = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return user_name

def get_new_username():

    user_name = input("what is your name?")
    file_name = 'username.json'
    with open(file_name,'w') as f_obj:
        json.dump(user_name,f_obj)
    return user_name

def greet_user():
    user_name = get_new_username()
    if user_name:
        correct_username = input("Is this your correct user name ? y/n")
        if correct_username == 'y':
            print("wellcome back " + user_name)

        else:
            user_name = get_new_username()
            print("we will remember you when you come back, " + user_name + "!")


greet_user()