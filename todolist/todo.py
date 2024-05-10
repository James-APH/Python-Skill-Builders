# Author: James Huston
# Email:  jamzhuston@gmail.com
# Description:
#
#

from datetime import date
from enum import Enum
import copy
import os


#
# Enum to manage various file states
#
class File_State(Enum):
    NONEXISTENT_FILE = 1
    EMPTY_DIRECTORY = 2
    EMPTY_FILE = 3
    VALID = 4


#
# function to check if a file is in the correct form
#
def file_guard(directory, file):
    file_state = File_State
    if len(os.listdir(f"{directory}/")) == 0:
        return file_state.EMPTY_DIRECTORY
    elif not os.path.isfile(f"{directory}/{file}.csv"):
        return file_state.NONEXISTENT_FILE
    elif os.stat(f"{directory}/{file}.csv").st_size == 0:
        return file_state.EMPTY_FILE
    else:
        return file_state.VALID


#
# function to get a file from a directory
#
def get_file(directory):
    file_state = File_State
    file = ""
    while file_guard(directory, file) == file_state.NONEXISTENT_FILE:
        os.listdir(f"{directory}/")
        file = str(input("Enter the name of the list you would like to access? "))
    return file


#
# class for todo
#
class ToDo:
    #
    # constructor for todo
    #
    def __init__(
        self, number: int, task: str, time: str, priority: int, date: date
    ) -> None:
        self.date = date
        self.task = task
        self.time = time
        self.number = number
        self.priority = priority

    #
    # convert a todo to a string (for csv file)
    #
    def to_string(self):
        return f"{self.number},{self.task},{self.priority},{self.time},{self.date}"

    #
    # declare a todo from a string (from csv file)
    #
    @classmethod
    def from_string(cls, string):
        string_partition = string.split(",")
        number, task, priority, time, date = string_partition
        return cls(number, task, priority, time, date)


#
# class for todolist
#
class ToDoList:
    #
    # constructor for todolist
    #
    def __init__(self, save_file: str, directory: str) -> None:
        self.save_file = save_file
        self.directory = directory
        self.path = f"{self.directory}/{self.save_file}.csv"
        self.todos = []

    #
    # function to load tasks from a file
    #
    def load_tasks(self):
        file_state = File_State
        if file_guard(self.directory, "") == file_state.EMPTY_DIRECTORY:
            print("NO FILES TO LOAD")
            self.todos = []
        else:
            file = get_file(self.directory)
            file = open(self.path)
            data = file.readlines()
            for x in data:
                self.todos.append(copy.copy(ToDo.from_string(x)))

    #
    # function to read out the todo list
    #
    def read_tasks(self):
        for x in self.todos:
            print(
                "#:                 Task:      Priority:      Time To Complete:     Date Started:"
            )
            print(
                f"{x.taskNumber}. | {x.task} | {x.priority} | {x.time} | {x.todaysDate}"
            )

    #
    # function to save tasks in the todo list
    #
    def save_tasks(self):
        open(self.path, "w").close()
        if not self.todos:
            print("saved")
        else:
            file = open(self.path, "r+")
            data = file.readlines()
            emptyfile = file_guard(self.directory, self.save_file) == 3
            for todo in self.todos:
                if not emptyfile and todo.asString() in data:
                    continue
                data.append(todo.asString())
            file.writelines(data)
            file.close()

    #
    # function to delete tasks from the todo list
    #
    def delete_tasks(self):
        if not self.todos:
            print("ToDoList is empty")
        else:
            taskToDelete = int(
                input("Enter the number of the task you would like to delete: ")
            )
            if taskToDelete < 0 or taskToDelete >= len(self.todos):
                while taskToDelete < 0 or taskToDelete >= len(self.todos):
                    taskToDelete = int(input("Enter a valid task to delete: "))
                self.todos.pop(taskToDelete - 1)
                self.__re_order_task_number()

    #
    # function to edit tasks in the todo list
    #
    def edit_tasks(self):
        if not self.todos:
          print("ToDoList is empty")
        else:
            taskToEdit = int(
                input("Enter the number of the task you would like to edit: ")
            )
            if taskToEdit < 0 or taskToEdit > len(self.todos):
                while taskToEdit < 0 or taskToEdit > len(self.todos):
                    taskToDelete = int(input("Enter a valid task to edit: "))


    #
    # function to add tasks to the todo list
    #
    def add_tasks(self):
        i = 1
        answer = input("Would you like to add some tasks? [Y/N]").lower()
        while answer != "n":
            number = i
            task = input("What is the task: ").lower()
            _date = date.today()
            time = input("How long should this take you? ")
            priority = int(
                input(
                    "How Important is this task?"
                    "\nNice To Have --> [1]"
                    "\nImportant -----> [2]"
                    "\nCrucial -------> [3]"
                )
            )

            todo = ToDo(number, task, time, priority, _date)
            self.todos.append(copy.copy(todo))
            answer = input("Would you like to contiue adding add tasks [Y/N]").lower()
            i += 1
        self.__re_order_task_number()

    #
    # function to run on delete and after rotp
    #
    def __re_order_task_number(self):
        i = int(1)
        for x in self.todos:
            x.taskNumber = i
            i += 1


#
# function to output a menu for the user
#
def menu():
    return input(
        "Would you like to:"
        "\nAdd Tasks ---------------> [A]"
        "\nRead Tasks --------------> [R]"
        "\nSave Tasks --------------> [S]"
        "\nEdit tasks --------------> [E]"
        "\nDelete Tasks ------------> [D]"
        "\nQuit --------------------> [Q]"
    ).lower()


#
# function to create a new todolist
#
def create_to_do_list():
    fileName = input("What would you like to call this todo list? ")
    todoList = ToDoList(fileName, "todos")
    todoList.add_tasks()
    return todoList


#
# function to load a todo list
#
def load_to_do_list():
    fileName = input("What is the name of the list you would like to load? ")
    todoList = ToDoList(fileName, "todos")
    todoList.load_tasks()
    return todoList


#
# UI:
#
answer = input("Create or Load a ToDo list: [C/L]").lower()

if answer == "c":
    todoList = create_to_do_list()
else:
    todoList = load_to_do_list()
choice = menu()
while choice != "q":
    match choice:
        case "a":
            todoList.add_tasks()
        case "r":
            todoList.read_tasks()
        case "s":
            todoList.save_tasks()
        case "e":
            todoList.edit_tasks()
        case "d":
            todoList.delete_tasks()
        case _:
            print("Not a command")
    choice = menu()
