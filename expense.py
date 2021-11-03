from PyInquirer import prompt
import csv
import os
import sys


def readUsers(infos):
    result = []
    with open('users.csv', 'r', newline='') as csvfile:
        spamreader = csv.DictReader(csvfile)
        for row in spamreader:
            result.append(row['User'])
    return result

def readUsersCheckbox(infos):
    result = []
    with open('users.csv', 'r', newline='') as csvfile:
        spamreader = csv.DictReader(csvfile)
        for row in spamreader:
            result.append({"name":row['User']})
    return result

    

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": readUsers,
    },
    {
        "type":"checkbox",
        "name":"InvolvedPeople",
        "message":"New Expense - Involved People: ",
        "choices": readUsersCheckbox,
    },

]


# method writing informations in CSV of the expense
def pushInCSV(infos):
    file_exists = os.path.isfile('expense_report.csv')
    with open('expense_report.csv', 'a', newline='') as csvfile:
        headers = ['Amount', 'Label', 'Spender', 'InvolvedPeople']
        spamwriter = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n',fieldnames=headers)
        if not file_exists:
            spamwriter.writeheader()  # file doesn't exist yet, write a header
        spamwriter.writerow({'Amount': infos.get('amount'), 'Label': str(infos.get('label')), 'Spender': str(infos.get('spender')), "InvolvedPeople": infos.get('InvolvedPeople')})
        
def repartition(infos):
    jsp = infos.get('InvolvedPeople')
    taille = len(jsp)
    montant = int(infos.get('amount')) / taille
    for elt in jsp:
        print(elt + " has to pay " + str(montant))



def new_expense(*args):
    infos = prompt(expense_questions)
    try:
        int(infos.get('amount'))
    except ValueError:
        print("Oops!  That was no valid number for the amount.  Try again...")
        sys.exit(1)

    if (infos.get('label').isdigit()):
        print("Oops!  That was no valid type for the label.  Try again with string")
        sys.exit(1)

    repartition(infos)

    pushInCSV(infos)

    print("Expense Added !")

    return True


