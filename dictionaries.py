alian_0 = {'color' : 'green', 'points' : 5}


print(alian_0['color'])
print(alian_0['points'])

alian_0['x_position'] = 0
alian_0['y_position'] = 25

print(alian_0)


my_friends_info = {
    'first_name': 'Guldana',
    'last_name' : 'Arken',
    'age': 25,
    'address':'101 main st , Provence, RI'
}

print(my_friends_info['first_name']+' '+ my_friends_info['last_name']+' '+ str(my_friends_info['age'])+ ' '+ my_friends_info['address'])


friends_favorite_num = {
    'max':  5,
    'lynda': 8,
    'mark' : 10,
    'june': 75,
    'dan': 45,
}

print("Max's favorite number is "+ str(friends_favorite_num['max'])+"\n Lynda's favorite number is "+ str(friends_favorite_num['lynda']))


friends = ['max','dan']
for name in friends_favorite_num:
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() + " I see your favorite number is "+
              str(friends_favorite_num[name]).title())