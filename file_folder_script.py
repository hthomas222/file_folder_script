import os
from rich.console import Console
from rich.table import Table
from rich import print
import sys
import shutil


def file_saver():
    old_location = console.input("[bold blue]Enter the location of where the file is currently located at: ")
    New_location = console.input("[bold blue]Enter the location of where the file is wanted: ")
    shutil.move(old_location, New_location)

def folder_creation():
    folder = console.input("[bold blue]Enter the location of where you want to create a folder: ")
    name_of_folder = console.input("[bold blue]Enter the name of the folder you are wanting to create: ")
    os.chdir(folder)
    os.mkdir(name_of_folder)

def file_creation():
    folder = console.input("[bold blue]Enter the location of where you want to create a file: ")
    name_of_file = console.input("[bold blue]Enter the name of file: ")
    os.chdir(folder)
    with open(name_of_file) as file:
        file.read()

def folder_mover():
    old_location = console.input("[bold blue]Enter the location of where the file is currently located at: ")
    New_location = console.input("[bold blue]Enter the location of where the file is wanted: ")
    shutil.move(old_location, New_location)    


def check(test):
    if test == "2":
        return test
    if test == "1":
        sys.exit()
    sel = ["1", "2"]
    while test not in sel:
            console.log("Please enter either 1 or 2")
            test = console.input("[bold red]Select 1 to exit |""[bold green]| Select 2 to continue: ")
    return test



test = ""
while test != "1":
    print()
    table = Table(title="Auto Filer")
    table.add_column("NUM", style="green")
    table.add_column("TASK", style="red")
    table.add_column("Description", style="blue")

    table.add_row("1", "File_Mover", "This will move a file to a the place of your desire.")
    table.add_row("2", "Folder_Creation", "This will create the folder of your desire.")
    table.add_row("3", "File_Creation", "This will move a file.")
    table.add_row("4", "Folder_Mover", "This will move a folder.")
    console = Console()
    console.print(table)
    print()
    selection = console.input("[bold green]Enter a number to execute the command: ")
    if selection == "1":
        file_saver()
    elif selection == "2":
        print()
        folder_creation()
        print()
    elif selection == "3":
        print()
        file_creation()
        print()
    elif selection == "4":
        print()
        folder_mover()
        print()
    else:
        console.log("[bold red]Please enter a valid choice!")
    print()
    test = console.input("[bold red]Select 1 to exit |""[bold green]| Select 2 to continue: ")
    if test != "1":
        x = check(test)
        if x == "1":
            sys.exit()
