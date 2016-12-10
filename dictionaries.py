'''
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



rivers = {
    'nil': 'egypt',
    'changjiang': 'china',
    'mississippi river':'USA',
}

for river,country in rivers.items():
    print('The ' + river.title() + ' run through '+ country.title())

for rivername in rivers.keys():
    print(rivername.title())
for countryname in rivers.values():
    print(countryname.title())



#==============================================================

my_friends1_info = {
    'first_name': 'Guldana',
    'last_name' : 'Arken',
    'age': 25,
    'address':'101 main st , Provence, RI'
}

my_friends2_info = {
    'first_name': 'Nadira',
    'last_name' : 'Tugl',
    'age': 26,
    'address':'101 main st , Denton, TX'
}

my_friends3_info = {
    'first_name': 'Kamiron',
    'last_name' : 'Adil',
    'age': 25,
    'address':'101 main st , Arlington, VA'
}

friends = [my_friends1_info,my_friends2_info,my_friends1_info]

for friend in friends:
    print(friend)


#=================================================


Max = {'type':'Dog','owner':'Jenney'}
Alessia = {'type':'Cat','owner':'Waverly'}
cacot = {'type':'bird','owner':'mark'}

pets = [Max,Alessia,cacot]


for pet in pets:

    print(pet)


#====================================================


favorite_places = {
    'mark':['Arlington','Fairfax'],
    'Jun':['Miami','London'],
    'Dan':['Tokyo','shanghai']
}

for name, places in favorite_places.items():
    print ("\n" + name.title() + " 's favorite place are :")
    for place in places:
        print("\t" + place.title())

#=====================================================


friends_favorite_num = {
    'max':  ['5','7'],
    'lynda': ['8','9'],
    'mark' : ['3','6'],
    'june': ['75','88'],
    'dan': ['45','99']
}

for name, nums in friends_favorite_num.items():
    print("\n" + name.title() + " 's favorite numbers are: ")
    for num in nums:
        print("\t" + num)

#======================================================
'''



cities = {
    'Tokyo':{'country':'Japan','population':'14million'},
    'Los Angeles':{'country':'USA','population':'4million'},
    'Washington DC':{'country':'USA','population':'66k'}
}


for citi ,cities_info in cities.items():
    print("\n" + citi.title())

    country = cities_info['country']
    population = cities_info['population']

    print("\t" + "country: " + country)
    print("\t" + "population: " + population)







