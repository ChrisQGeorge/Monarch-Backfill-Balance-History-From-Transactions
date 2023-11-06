import os
import re
import csv
import pathlib
import platform
from datetime import datetime, timedelta



def getPath(inpString):
    system = platform.system()

    if system == "Linux":
        return str(pathlib.Path(__file__).parent) + "/"+inpString+"/"
    else:
        return str(pathlib.Path(__file__).parent) + "\\"+inpString+"\\"


def exportBalances(balances):
    expPath = getPath("export")
    exportFiles = os.listdir(expPath)

    baseFileName = "balances"
    fileName = baseFileName + ".csv"
    
    i = 1
    while fileName in exportFiles:
        fileName = baseFileName + " (" + str(i) + ").csv"
        i = i+1


    with open(expPath + fileName, 'w', newline='') as writeFile:
        fileWrite = csv.writer(writeFile)
        
        for balance in balances:
            fileWrite.writerow(balance)


def selectImportFile(importDir):

    filenames = os.listdir(importDir)
    print("Which file would you like to import? :\n")
    i = 1
    for name in filenames:
        print(str(i) + ": " + name)
        i += 1

    usrInp = input(": ")

    while not 1 <= int(usrInp) <= i:
        print("Error: Please select one of the files")
        usrInp = input(": ")

    selection = importDir + filenames[int(usrInp)-1]

    return selection

def getBalanceFromTransactions(transactions):

    tally = 0
    i = min(transactions.keys())
    end = max(transactions.keys())

    while i <= end:
        if i not in transactions.keys():
            transactions[i] = [i, tally, account]
        else:
            tally = transactions[i][1]
            account = transactions[i][2]

        i += 1
    
    balances = [["Date","Balance","Account"]]

    keys = list(transactions.keys())
    keys.sort(reverse=True)

    for date in keys:
        balances.append([(datetime(1899, 12, 30) + timedelta(days=int(transactions[date][0]))).strftime('%Y-%m-%d'), transactions[date][1]/100, transactions[date][2]])
        
    return balances


def importMintTransactions():
    importDir = getPath("import")
    selection = selectImportFile(importDir)




def importMintBalances():
    importDir = getPath("import")
    selection = selectImportFile(importDir)
    accountName = input("What is the Monarch account name?")
    loadTable = []
    with open(str(selection), newline='') as impFile:
        unsortedTable = csv.reader(impFile)

        next(unsortedTable)

        table = sorted(unsortedTable, key = lambda row: datetime.strptime(row[0], "%b-%y"))
        
        for row in table:
            date = (datetime.strptime(row[0], '%b-%y') - datetime(1899, 12, 30)).days
            balance = row[1].replace("$", '').replace(",", '')
            loadTable.append([date, balance, accountName])

    balances = [["Date","Balance","Account"]]
    currDate = loadTable[0][0]
    i = 0
    runningBalance = loadTable[0][1]
    while i <= len(loadTable)-1:

        while currDate <= loadTable[i][0]:

            if currDate == loadTable[i][0]:runningBalance = loadTable[i][1]

            balances.append([((datetime(1899, 12, 30) + timedelta(days=int(currDate))).strftime('%Y-%m-%d')), runningBalance, accountName])
            currDate += 1
        i += 1


    return balances







def importMonarchTransactions():
    importDir = getPath("import")
    selection = selectImportFile(importDir)
    runningBal = int(float(re.sub(",|\$","",input("What is the current account balance?: ")))*100)
    transactions = {}

    with open(str(selection), newline='') as impFile:
        unsortedTable = csv.reader(impFile)

        next(unsortedTable)

        table = sorted(unsortedTable, key = lambda row: datetime.strptime(row[0], "%Y-%m-%d"), reverse=True)

        for row in table:
            if not row[0] == "Date":
                date = (datetime.strptime(row[0], '%Y-%m-%d') - datetime(1899, 12, 30)).days
                account = row[3]
                amount = int(float(row[6])*100)
                transactions[date] = [date, runningBal, account]

                runningBal -= amount

        transactions[date-1] = [date-1, runningBal, account]
    
    return getBalanceFromTransactions(transactions)

def menu():
    usrInput = ""
    balances = []
    while True:

        usrInput = input(
            "\
Would you like to import from:\n\
1.Monarch\n\
2.Mint\n\
e.Exit\n\
:"
            #3.YNAB
            #4.Rocket Money
            #5.Empower(Formerly Personal Capital)
            #6.Quicken
            #7.Copilot
        )

        if usrInput == "e":
            break
        elif usrInput == "1":
            balances = importMonarchTransactions()
            break

        elif usrInput == "2":
            while True:
                usrInput = input(#1.Convert Mint transactions to Monarch balances\n\
                    "Would you like to:\n\
1.Convert Mint trend account balances to Monarch balances\n\
e.Exit\n\
:"
                )
                if usrInput == "e":
                    break
                elif usrInput == "1":
                    balances = importMintBalances()
                    break
                #elif usrInput == "2":
                #    balances = importMintBalances()
                #    break
                else:
                    print("Error: Please select one of the available options:")
            break
        else:
            print("Error: Please select one of the available options:")
    
    if balances != []:
        exportBalances(balances)


if __name__ == "__main__":
    menu()
