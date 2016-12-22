'''
def display_message():
    print("I'm learning python function.")

display_message()


def favorite_book(title):
    print("One of my favorite book is " +title )

favorite_book('1948')



def make_shirt(print_title,size="large"):
    print(size + " size T-shirt with " + print_title + " on it.")


make_shirt('tokyo')
make_shirt(print_title='lA',size="medium")


def describe_city(city_name,country= 'USA'):

    print(city_name + " is in " + country)


describe_city('NYC')
describe_city('LA')
describe_city('tokyo','japan')





def city_country(city,country):

     string_format = city +"," +country

     return string_format.title()



print(city_country('tokyo','japan'))
print(city_country('nyc','Usa'))




def make_album(artist,title_name,tracks=' '):
    album = {'artist':artist,'title':title_name}

    if tracks:
        album['tracks'] = tracks
    return album


print(make_album('max','paint it black'))

print(make_album('tom',"I don't know",11))






def make_album(artist,title_name,tracks=' '):
    album = {'artist':artist,'title':title_name}

    if tracks:
        album['tracks'] = tracks
    return album

while True:
    a_artist = input("Artist name: ")
    if a_artist == 'q':
        break

    a_title_name = input("Album title name: ")
    if a_title_name =='q':
        break

    a_tracks = input("please enter track number ")
    if a_tracks =='q':
        break


    print(make_album(a_artist,a_title_name,a_tracks))









def show_magicians(magicians):

    for magician in magicians:
        print(magician.title())

def make_great(magicians_name,great_magician):

    for name in magicians_name:

        modified_name = "Great " + name
        great_magician.append(modified_name)

    show_magicians(great_magician)
    show_magicians(magicians_name)







magician_list = ['max','dan','mike','jack']
new_name = []
make_great(magician_list,new_name)







def make_sandwiches(*type_of_sandwich):

    print(type_of_sandwich)



make_sandwiches("cheese")
make_sandwiches("cheese","stake")
make_sandwiches("cheese","stake",'chiken')



def build_profile(first,last,**more_info):

    profile = {}
    profile['first_name']=first
    profile['last_name']= last

    for key,value in more_info.items():
        profile[key]=value
    return profile


user_profile = build_profile('kudrat','kuerban',
                             age = '23',
                             home= 'n/a')



print(user_profile)


'''
# import print_models
# import print_something from print_models
# import print_something from print_models as printing
# import print_models *
# import print_models as printing

from print_models import print_something as printing

def make_cars(make,model,**other_info):

    car = {}
    car['car_made']=make
    car['car_model']= model

    for key,value in other_info.items():
        car[key] = value
    return car



cars = make_cars('acura','TLX',
                 color = 'dark gray',
                 celender ='2.4' )


#printing.print_something(cars)
printing(cars)













