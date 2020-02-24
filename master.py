from validate_email import validate_email
import re

profiles = {'Jane':'0.2 miles\nGoing to TacoBell at 10:00', 'Oski':'0.2 miles\n Going to Unit3 at 10:30',
        'Carol':'0.3 miles\nGoing to Frat Row at 12:00', 'DeNero':'0.4 miles\n Going to Wheeler at 10:15',
        'Marc':'0.4 miles\nGoing to Blackwell at 10:10'}



def other_locations():
    other_names = list(profiles.keys())
    print("\nHere are other students around you!\n", other_names)
    stalk_name = input("\nWhich student would you like to chat/match with? : ")
    while(stalk_name != 'match'):
        print('\n',stalk_name,profiles.get(stalk_name))
        stalk_name = input("\nEnter 'match' to match or enter other names to view profile!:\n")


def location():
    location = input("Location: ")

def profile():
    name = input("Name: ")
    password = input("Password: ")

def verify():
    valid = False
    email = input('\nEnter your berkeley.edu: ')

    while('berkeley.edu' not in email):
        print('Sorry, berkeley emails only!')
        email = input('Enter your berkeley.edu: ')

        if len(email) > 7 and validate_email(email):
            valid = True
        else:
            print("Invalid")
            email = input('Enter your berkeley.edu: ')                

    if(valid):
        print("\nWelcome to Paws & Go!")


verify()
profile()
location()
other_locations()
