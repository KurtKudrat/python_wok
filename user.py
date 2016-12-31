class User():

    def __init__(self,first,last,age,gender):

        self.first_name = first
        self.last_name = last
        self.age = age
        self.gender = gender
        self.login_attempts = 0


    def describe_user(self):
        print(self.first_name.title() + ' ' +self.last_name.title() + ' ' + self.gender + " is " + str(self.age) + " years old ")


    def greet_user(self):
        print(self.last_name.title() + ' ' + "Thanks for being in my code example!")


    def increment_login_attempts(self):
        self.login_attempts =self.login_attempts+1


    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):

    def __init__(self,first,last,age,gander):

        super().__init__(first,last,age,gander)
        self.privileges = Privileges()



class Privileges():

     def __init__(self):
         self.privileges = ['can add post', 'can delete post', 'can ban user']


     def show_privileges(self):
        print("Administrator's privileges: ")

        for privilege in self.privileges:
            print('\t' + privilege)
