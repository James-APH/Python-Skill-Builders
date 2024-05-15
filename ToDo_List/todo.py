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
        print(os.listdir(f"{directory}/"))
        file = str(input("Enter the name of the list you would like to access?\n"))
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
    def __init__(self, file: str, directory: str) -> None:
        self.file = file
        self.directory = directory
        self.path = f"{self.directory}/{self.file}.csv"
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
            self.file = get_file(self.directory)
            self.path = f"{self.directory}/{self.file}.csv"
            file_reader = open(self.path)
            data = file_reader.readlines()
            for x in data:
                self.todos.append(copy.copy(ToDo.from_string(x)))

    #
    # function to read out the todo list
    #
    def read_tasks(self):
        for x in self.todos:
            print(
                f"NUMBER: {x.number}\nTASK: {x.task}\nPRIORITY: {x.priority}\nTIME: {x.time}\nDATE: {x.date}\n"
            )

    #
    # function to save tasks in the todo list
    #
    def save_tasks(self):
        open(self.path, "w").close()
        if not self.todos:
            print("Saved!")
        else:
            file_writer = open(self.path, "w")
            for todo in self.todos:
                file_writer.write(f"{todo.to_string()}\n")
            file_writer.close()
            print("Saved!")

    #
    # function to delete tasks from the todo list
    #
    def delete_tasks(self):
        if not self.todos:
            print("ToDoList is empty")
        else:
            task_to_delete = (
                int(input("Enter the number of the task you would like to delete:\n"))
                - 1
            )
            if task_to_delete < 0 or task_to_delete >= len(self.todos):
                while task_to_delete < 0 or task_to_delete >= len(self.todos):
                    task_to_delete = int(input("Enter a valid task to delete:\n")) - 1
            del self.todos[task_to_delete]
            self.__re_order_task_number()

    #
    # function to edit tasks in the todo list
    #
    def edit_tasks(self):
        if not self.todos:
            print("ToDoList is empty")
        else:
            task_number = int(
                input("Enter the number of the task you would like to edit:\n")
            )
            if task_number < 0 or task_number > len(self.todos):
                while task_number < 0 or task_number > len(self.todos):
                    task_number = int(input("Enter a valid task to edit:\n"))
            editing = "y"
            while editing == "y":
                edit = str(
                    input(
                        "What would you like to edit?"
                        "\ntask description --> [D]"
                        "\ntask priority -----> [P]"
                        "\ntask time ---------> [T]\n"
                    ).lower()
                )
                match edit:
                    case "d":
                        self.todos[task_number - 1].task = str(
                            input("Enter the new description:\n")
                        )
                    case "p":
                        self.todos[task_number - 1].priority = int(
                            input("Enter the new priority:\n")
                        )
                    case "t":
                        self.todos[task_number - 1].time = str(
                            input("Enter the new time:\n")
                        )
                editing = str(
                    input("Would you like to keep editing this task? [Y/N]\n").lower()
                )

    #
    # function to add tasks to the todo list
    #
    def add_tasks(self):
        if not self.todos:
            i = 1
        else:
            i = self.todos[len(self.todos) - 1].number + 1
        answer = input("Would you like to add some tasks? [Y/N]\n").lower()
        while answer != "n":
            number = i
            task = input("What is the task:\n").lower()
            _date = date.today()
            time = input("How long should this take you?\n")
            priority = int(
                input(
                    "How Important is this task?"
                    "\nNice To Have --> [1]"
                    "\nImportant -----> [2]"
                    "\nCrucial -------> [3]\n"
                )
            )

            todo = ToDo(number, task, time, priority, _date)
            self.todos.append(copy.copy(todo))
            answer = input(
                "Would you like to continue adding add tasks [Y/N]\n"
            ).lower()
            i += 1
        self.__re_order_task_number()

    #
    # function to run after deleteing an element
    #
    def __re_order_task_number(self):
        i = int(1)
        for x in self.todos:
            x.number = i
            i += 1


#
# function to output a menu for the user
#
def menu():
    return str(
        input(
            "Would you like to:"
            "\nAdd Tasks ---------------> [A]"
            "\nRead Tasks --------------> [R]"
            "\nSave Tasks --------------> [S]"
            "\nEdit tasks --------------> [E]"
            "\nDelete Tasks ------------> [D]"
            "\nQuit --------------------> [Q]\n"
            "\n"
        )
    ).lower()


#
# function to create a new todolist
#
def create_to_do_list():
    fileName = input("What would you like to call this todo list?\n")
    todoList = ToDoList(fileName, "todos")
    todoList.add_tasks()
    return todoList


#
# function to load a todo list
#
def load_to_do_list():
    todoList = ToDoList("", "todos")
    todoList.load_tasks()
    return todoList


#
# UI:
#
answer = input("Create or Load a ToDo list: [C/L]\n").lower()

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
