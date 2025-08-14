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
import datetime
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
    item["id"]=(allitems[-1]["id"])+1
    allitems.append(item)
    return allitems


#Add new item to JSON
def additemToJson(itemRegistry):
    listOfitems = listAllitems()
    listOfitemsAdded = addNewItem(itemRegistry, listOfitems)
    createJsonFile(listOfitemsAdded)
    print("sucessfull added")


#Update tasks
def updateItemJson(itemSelect, newNameToItem, parameterToUpdate):
    listOfItems =  listAllitems()
    for i in range(len(listOfItems)):
        if(listOfItems[i]["id"]==itemSelect):
            listOfItems[i][parameterToUpdate] = newNameToItem

    createJsonFile(listOfItems)

now = datetime.datetime.now()
now = now.strftime("%Y-%m-%d %H:%M:%S")




# additemToJson(data)

# expense-tracker add --description "Lunch" --amount 20

import click

@click.command(name="add")
@click.option("--description", prompt="Type expense's name:", help="Expense's name:")
@click.argument("amount")
def addExpense(description, amount):
    data={
        "id": 0,
        "date": now,
        "description":description,
        "amount":amount
    }
    additemToJson(data)

#Update
@click.command(name="update")
@click.option("--id", prompt="Type expense's id:", help="Expense's id:")
@click.argument("parameter")
@click.argument("new")
def update(id, new, parameter):
    updateItemJson(int(id), new, parameter)



#List
@click.command()
def list():
    allitems = listAllitems()
    print(
            "ID ","\t",
            "AMOUNT\t\t",
            "DESCRIPTION\t\t",
            "DATE\t",
        )
    for i in range (len(allitems)):
        print(
        allitems[i]["id"],"\t",
        allitems[i]["amount"], "\t\t",
        allitems[i]["description"], "\t\t",
        allitems[i]["date"], "\t",
        )

@click.group()
def expensesTracker():
    pass

expensesTracker.add_command(addExpense)
expensesTracker.add_command(update)
expensesTracker.add_command(list)



if __name__ == "__main__":
    # print(now)
    expensesTracker()

