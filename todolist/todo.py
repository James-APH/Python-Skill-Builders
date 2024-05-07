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
# add stages (todo, doing, done)


from datetime import date
import copy
import os
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

class ToDoList:
    #
    # constructor for todolist
    #
    def __init__(self, saveFile) -> None:
        self.directory = "todos"
        self.todos = []
        self.saveFile = ""
    #
    # function to check if a file exists
    #
    def checkToDoExists(self, fileName):
      path = f'todos/{fileName}.csv'
      return os.path.isfile(path)
    #
    # function to load tasks from a file
    #
    def loadTasks(self):
      if len(os.listdir(f'{self.directory}/')) == 0:
        print("No Files exist")
      else:
        fileName = ""
        while not self.checkToDoExists(fileName):
          fileName = str(input("What is the name of the todolist that you would like to load? "))
        file = open(f'{self.directory}/{fileName}.csv')
        data = file.readlines()
        for x in data:
          stringAsList = x.split(',')
          self.todos.append(copy.copy(ToDo(stringAsList[0], stringAsList[1], stringAsList[2], stringAsList[3])))

    #
    # function to read out the todo list
    #
    def readTasks(self):
      for x in self.todos:
        print("#:                 Task:      Priority:      Time To Complete:     Date Started:")
        print(f"{x.taskNumber}. | {x.task} | {x.priority} | {x.time} | {x.todaysDate}")
    #
    # function to save tasks in the todo list
    #
    def saveTasks(self):
        if not self.todos:
            print("Nothing to save")
        else:
            print("Saving tasks")
            f = open(f'{self.directory}/{self.saveFile}', 'r+')
            data = f.readlines()
            i = int(0)
            for x in self.todos:
              str = f'{x.taskNumber},{x.task},{x.priority},{x.time},{x.todaysDate}'
              if str == data[i]:
                continue
              data[i] = str
              i += 1
            f.writelines(data)
            f.close()
    #
    # function to delete tasks from the todo list
    #
    def deleteTasks(self):
      if not self.todos:
        print("ToDoList is empty")
      else:
        taskToDelete = int(input("Enter the number of the task you would like to delete: "))
        if taskToDelete < 0 or taskToDelete > len(self.todos):
          while taskToDelete < 0 or taskToDelete >= len(self.todos):
            taskToDelete = int(input("Enter a valid task to delete: "))
          self.todos.pop(taskToDelete-1)
          self.__re_Order_Task_Number()
    #
    # function to edit tasks in the todo list
    #
    def editTasks(self):
      if not self.todos:
        print("ToDoList is empty")
      else:
        taskToEdit = int(input("Enter the number of the task you would like to edit: "))
        if taskToEdit < 0 or taskToEdit > len(self.todos):
          while taskToEdit < 0 or taskToEdit > len(self.todos):
            taskToDelete = int(input("Enter a valid task to edit: "))
    #
    # function to add tasks to the todo list
    #
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
                              "\nImportant -----> [2]"
                              "\nCrucial -------> [3]")
        todo = ToDo(taskNumber, task, time, priority)
        self.todos.append(copy.copy(todo))
        answer = input("Would you like to contiue adding add tasks [Y/N]").lower()
        i += 1
      self.__re_Order_Task_Number()
    #
    # function to run on delete and after rotp
    #
    def __re_Order_Task_Number(self):
      i = int(1)
      for x in self.todos:
        x.taskNumber = i
        i+=1
#
# function to output a menu for the user
#
def menu():
    return input("Would you like to:"
                "\nAdd Tasks ---------------> [A]"
                "\nRead Tasks --------------> [R]"
                "\nSave Tasks --------------> [S]"
                "\nEdit tasks --------------> [E]"
                "\nDelete Tasks ------------> [D]"
                "\nQuit --------------------> [Q]").lower()
#
# function to create a new todolist
#
def createToDoList():
  fileName = input("What would you like to call this todo list? ")
  todoList = ToDoList(fileName)
  todoList.addTasks()
  return todoList
#
# function to load a todo list
#
def loadToDoList():
  fileName = input("What is the name of the ToDo list you would like to load? ")
  todoList = ToDoList(fileName)
  todoList.loadTasks()
  return todoList


#
# UI:
#
createLoadAnswer = input("Create or Load a ToDo list: [C/L]").lower()

if createLoadAnswer == "c":
  todoList = createToDoList()
else:
  todoList = loadToDoList()
choice = menu()
while choice != "q":
  match choice:
    case "a":
      todoList.addTasks()
    case "r":
      todoList.readTasks()
    case "s":
      todoList.saveTasks()
    case "e":
      todoList.editTasks()
    case "d":
      todoList.deleteTasks()
    case _:
      print("Not a command")
  choice = menu()
