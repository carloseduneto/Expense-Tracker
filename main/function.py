"""
Requirements

Application should run from the command line and should have the following features:

    Users can add an expense with a description and amount.
    Users can update an expense.
    Users can delete an expense.
    Users can view all expenses.
    Users can view a summary of all expenses.
    Users can view a summary of expenses for a specific month (of current year).

Here are some additional features that you can add to the application:

    Add expense categories and allow users to filter expenses by category.
    Allow users to set a budget for each month and show a warning when the user exceeds the budget.
    Allow users to export expenses to a CSV file.
"""
import json
import os
fileName = "main/allExpenses.json"

# Create a JSON file
def createJsonFile(data):
    with open(fileName, mode="w", encoding="utf-8") as write_file:
        json.dump(data, write_file, indent=4)


# Read a JSON File
def listAllitems():
    with open(fileName, mode="r", encoding="utf-8") as read_file:
        fileContent = json.load(read_file)
        return fileContent
    
#Add new item to list
def addNewItem(item, allitems):
    allitems.append(item)
    return allitems


#Add new Task to JSON
def additemToJson(itemRegistry):
    listOfitems = listAllitems()
    listOfitemsAdded = addNewItem(itemRegistry, listOfitems)
    createJsonFile(listOfitemsAdded)
    print("sucessfull added")

data = {
    "id" : 2,
    "description" : "Lettuce",
    "amount" : 2.48
}

# additemToJson(data)

# expense-tracker add --description "Lunch" --amount 20

import click

@click.command()
@click.option("--name", prompt="Digite seu nome", help="Nome da pessoa a cumprimentar.")
@click.option("--repeat", default=1, help="Quantas vezes repetir a saudação.")
def hello(name, repeat):
    """Exibe uma saudação personalizada."""
    for _ in range(repeat):
        click.echo(f"Olá, {name}!")

if __name__ == "__main__":
    hello()

