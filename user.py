from PyInquirer import prompt
import os
import csv
import sys

user_questions = [
 {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
    },
]

# method writing informations in CSV of the expense
def pushInCSV(infos):
    file_exists = os.path.isfile('users.csv')
    with open('users.csv', 'a', newline='') as csvfile:
        headers = ['User']
        spamwriter = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n',fieldnames=headers)
        if not file_exists:
            spamwriter.writeheader()  # file doesn't exist yet, write a header
        spamwriter.writerow({'User': str(infos.get('name'))})

def add_user():
    infos = prompt(user_questions)

    if (infos.get('name').isdigit()):
        print("Oops!  That was no valid type for the user.  Try again with string")
        sys.exit(1)
    pushInCSV(infos)
    print("User Added !")
    
    return True