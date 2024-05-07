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
    taskNumber = 0
    todaysDate = date.today()
    task = "no task"
    time = 0
    priority = 0



class ToDoList:
    def __init__(self, todos, saveFile) -> None:
        self.todos = []
        self.saveFile = ""

    def loadTasks():
        print("this function will load the tasks to a list from a file")

    def readTasks():
        print("This function will read the tasks from the task list")

    def saveTasks(self):
        if not self.todos:
            print("Nothing to save")
        else:
            f = open("%s.csv" %self.saveFile, 'x')
            for x in self.todos:
                f.write(f'{x.todaysDate},{x.task},{x.priority},{x.time}')

    def deleteTask():
        print("This function will delete a task from the list")

    def editTask():
        print("This function will edit a tasks attributes")

    def addTasksP():
        print("This function will add tasks to the list")















def menu():
    return input("Would you like to:" 
                "\nRead Tasks --------------> [R]"
                "\nAdd Tasks ---------------> [A]"
                "\nDelete a Task -----------> [D]"
                "\nDelete the Task List ----> [DD]"
                "\nAlter a tasks priority --> [P]"
                "\nSave Tasks --------------> [S]"
                "\nQuit --------------------> [Q]").lower()


def createTasks():
    answer = "y"
    todo = ToDo()
    todoList = ToDoList()
    i = int(1)
    while answer != "n":
        todo.taskNumber = i
        todo.task = input("What is the task: ").lower()
        todo.todaysDate = date.today()
        todo.time = input("How long should this take you? ")
        todo.priority = input("How Important is this task?"
                              "\nNice To Have --> [1]"
                              "\nImportant    --> [2]"
                              "\nCrucial      --> [3]")
        todoList.list.append(copy.copy(todo))
        answer = input("Would you like to contiue adding add tasks [Y/N]").lower()
        i += 1
    return todoList

createLoadAnswer = input("Create or Load a ToDo list: [C/L]").lower()

if createLoadAnswer == "c":
    addTasksAnswer = input("Would you like to add tasks [Y/N]").lower()
    if addTasksAnswer == "y":
        todoList = createTasks()
        choice = menu();
        while choice != "q":
            match choice:
                case "r":

                case "a":

                case "d":

                case "dd":

                case "p":

                case "s":
                    saveToDoList(todoList)
                case "q":



            choice = menu();
            

else:
    print(0)
    
