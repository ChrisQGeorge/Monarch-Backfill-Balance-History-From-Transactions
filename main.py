import os
import re
import csv
import pathlib
import platform




def getPath(inpString):
    system = platform.system()
    impPath = str(pathlib.Path(__file__).parent) + "\\import\\"
    expPath = str(pathlib.Path(__file__).parent) + "\\export\\"

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
        fileName = baseFileName + str(i) + ".csv"
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

def importMintTransactions():
    pass

def importMintBalances():
    pass


def importMonarchTransactions():
    importDir = getPath("import")
    selection = selectImportFile(importDir)
    runningBal = int(float(re.sub(",|\$","",input("What is the current account balance?: ")))*100)
    transactions = {}

    print(selection)
    with open(str(selection), newline='') as impFile:
        table = csv.reader(impFile)

        for row in table:
            if not row[0] == "Date":
                date = int(row[0])
                account = row[3]
                amount = int(float(row[6])*100)
                transactions[date] = [date, runningBal, account]

                runningBal -= amount

        transactions[date-1] = [date-1, runningBal, account]
    
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
        balances.append([transactions[date][0], transactions[date][1]/100, transactions[date][2]])
        
    return balances

def menu():
    importDir = getPath("import")
    filenames = os.listdir(importDir)

    exitBool = False
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
            break
    
    if balances != []:
        exportBalances(balances)








if __name__ == "__main__":
    menu()
