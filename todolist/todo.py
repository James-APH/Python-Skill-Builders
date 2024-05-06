# Author: James Huston
# Email:  jamzhuston@gmail.com
# Description:
# This is a simple calculator project
# the calculator will add, multiply, divide, and subtract


from datetime import date

createLoadAnswer = input("Create or Load a ToDo list: [C/L]").lower()


def listOptions():
    input("Would you like to: ")


def addTaskToFile(file,date,time,priority,task):
    print(0)
    

def createTasks(file):
    answer = "y"
    while answer != "n":
        task = input("What is the task: ").lower()
        date = date.today()
        time = input("How long should this take you? ")
        priority = input("""How Important is this task?\n
                            Nice To Have --> [1]\n
                            Important    --> [2]\n
                            Crucial      --> [3]""")
        addTaskToFile(filemanip,date,time,priority,task)
        answer = input("Would you like to contiue adding add tasks [Y/N]").lower()


if createLoadAnswer == "c":
    name = input("What would you like to name your ToDo list: ")
    filemanip = open("%s.csv" %name, 'x')
    addTasksAnswer = input("Would you like to add tasks [Y/N]").lower()
    if addTasksAnswer == "y":
        createTasks(filemanip)
else:
    print(0)
    # Find out what the user wants to do?
    # read a file (must make sure file exists)
    # write a file ()
    # remove items
    # add items
    # change priority
    # add extension to todos
    # add ui
    
