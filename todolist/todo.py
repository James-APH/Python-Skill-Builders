# Author: James Huston
# Email:  jamzhuston@gmail.com
# Description:
# 
# 

# Tasks:
# write a todo list in a list of tuples
# create a file
# read a file (must make sure file exists)
# write a file ()
# remove items
# add items
# change priority
# add extension to todos
# add ui
# add stages (todo, doing, done)
     

from datetime import date
import copy
# create a todo list with a list and a tuple
# print the rules
# on quit ask the user if they would like to save their todolist

class ToDo:
    todaysDate = date.today()
    task = "no task"
    time = 0
    priority = 0










def saveToDoList(todoList):
    name = input("What would you like to name your ToDo list: ")
    f = open("%s.csv" %name, 'x')
    for x in todoList:
        f.write(f'{x.todaysDate},{x.task},{x.priority},{x.time}')





def menu():
    return input("""Would you like to: 
                \nRead Tasks --------------> [R]
                \nAdd Tasks ---------------> [A]
                \nDelete a Task -----------> [D]
                \nDelete the Task List ----> [DD]
                \nAlter a tasks priority --> [P]
                \nQuit --------------------> [Q]""")


def createTasks():
    answer = "y"
    todo = ToDo()
    todoList = []
    while answer != "n":
        todo.task = input("What is the task: ").lower()
        todo.todaysDate = date.today()
        todo.time = input("How long should this take you? ")
        todo.priority = input("""How Important is this task?\n
                            Nice To Have --> [1]\n
                            Important    --> [2]\n
                            Crucial      --> [3]""")
        todoList.append(copy.copy(todo))
        answer = input("Would you like to contiue adding add tasks [Y/N]").lower()
    return todoList

createLoadAnswer = input("Create or Load a ToDo list: [C/L]").lower()

if createLoadAnswer == "c":
    addTasksAnswer = input("Would you like to add tasks [Y/N]").lower()
    if addTasksAnswer == "y":
        createTasks()
else:
    print(0)
    
