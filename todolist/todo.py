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
  def __init__(self, taskNumber, task, time, priority) -> None:
    self.taskNumber = taskNumber
    self.todaysDate = date.today()
    self.task = task
    self.time = time
    self.priority = priority

  def setTaskNumber(self)





class ToDoList:
    def __init__(self, saveFile) -> None:
        self.todos = []
        self.saveFile = ""

    def loadTasks():
        print("this function will load the tasks to a list from a file")

    def readTasks(self):
      for x in self.todos:
        print("#:                 Task:      Priority:      Time To Complete:     Date Started:")
        print(f"{x.taskNumber}. | {x.task} | {x.priority} | {x.time} | {x.todaysDate}")

    def saveTasks(self):
        if not self.todos:
            print("Nothing to save")
        else:
            print("Saving tasks")
            f = open("%s.csv" %self.saveFile, 'x')
            for x in self.todos:
                f.write(f'{x.taskNumber},{x.task},{x.priority},{x.time},{x.todaysDate}')

    def deleteTask(self):
      if not self.todos:
        print("ToDoList is empty")
        return
      taskToDelete = int(input("Enter the number of the task you would like to delete: "))
      if taskToDelete < 0 or taskToDelete > len(self.todos):
        while taskToDelete < 0 or taskToDelete >= len(self.todos):
          taskToDelete = int(input("Enter a valid task to delete: "))
        self.todos.pop(taskToDelete-1)

    def editTask(self):
      if not self.todos:
        print("ToDoList is empty")
        return
      taskToEdit = int(input("Enter the number of the task you would like to edit: "))
      if taskToEdit < 0 or taskToEdit > len(self.todos)
        while taskToEdit < 0 or taskToEdit > len(self.todos):
          taskToDelete = int(input("Enter a valid task to edit: "))

    def addTasks(self):
      i = 1
      answer = input("Would you like to add some tasks? [Y/N]").lower()
      while answer != "n":
        taskNumber = i
        task = input("What is the task: ").lower()
        todaysDate = date.today()
        time = input("How long should this take you? ")
        priority = input("How Important is this task?"
                              "\nNice To Have --> [1]"
                              "\nImportant    --> [2]"
                              "\nCrucial      --> [3]")
        todo = ToDo(taskNumber, task, time, priority)
        self.todos.append(copy.copy(todo))
        answer = input("Would you like to contiue adding add tasks [Y/N]").lower()
        i += 1
















def menu():
    return input("Would you like to:"
                "\nRead Tasks --------------> [R]"
                "\nAdd Tasks ---------------> [A]"
                "\nDelete a Task -----------> [D]"
                "\nDelete the Task List ----> [DD]"
                "\nAlter a tasks priority --> [P]"
                "\nSave Tasks --------------> [S]"
                "\nQuit --------------------> [Q]").lower()


def createToDoList():
  fileName = input("What would you like to call this todo list? ")
  todoList = ToDoList(fileName)
  todoList.addTasks()
  return todoList



createLoadAnswer = input("Create or Load a ToDo list: [C/L]").lower()

if createLoadAnswer == "c":
    addTasksAnswer = input("Would you like to add tasks [Y/N]").lower()
    if addTasksAnswer == "y":
       # todoList = createTasks()
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
