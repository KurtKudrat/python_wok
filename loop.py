'''
user_names = ["a","b","c","admin","x"]
if user_names:

    for user in user_names:

        if user == "admin":
            print("hello admin, would you like to see a status report?")
        else:
            print("hello " + user +", thank you for logging in.")
else:
    print("We need find some user.")

'''



#=====================================================

current_users = ["aA","bB","cC","dD","eE"]
new_user = ["tT","ee","xx","cc"]

for user in new_user:
    if user.upper() in (user_name.upper() for user_name in current_users):
        print("The user name is exist.")
    else:
        print("This user name is unique.")



