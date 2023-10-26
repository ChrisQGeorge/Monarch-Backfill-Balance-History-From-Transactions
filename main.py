import os
import re
import csv
import pathlib


if __name__ == "__main__":
    impPath = str(pathlib.Path(__file__).parent) + "\\import\\"
    expPath = str(pathlib.Path(__file__).parent) + "\\export\\"
    filenames = os.listdir(impPath)

    print("Which file would you like to import? :\n")
    i = 1
    for name in filenames:
        print(str(i) + ": " + name)
        i += 1
    
    usrInp = input(": ")

    transactions = {}

    while not 1 <= int(usrInp) <= i:
        print("Error: Please select one of the files")
        usrInp = input(": ")
    
    selection = impPath + filenames[int(usrInp)-1]

    runningBal = int(float(re.sub(",|\$","",input("What is the current account balance?: ")))*100)
    
    with open(selection, newline='') as impFile:
        table = csv.reader(impFile, delimiter=',', quotechar='|')

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
        
    exportFiles = os.listdir(expPath)

    baseFileName = "balances"
    fileName = baseFileName + ".csv"
    
    i = 1
    while fileName in exportFiles:
        fileName = baseFileName + str(i) + ".csv"


    with open(expPath + fileName, 'w', newline='') as writeFile:
        fileWrite = csv.writer(writeFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        
        for balance in balances:
            fileWrite.writerow(balance)
