# Monarch-Backfill-Balance-History-From-Transactions
The goal of this script is to backfill the balance history of Monarch money accounts based of an exported transaction history.

## Installation
This program requires Python 3 to be installed on your system and added to your path. https://www.python.org/downloads/
This also assumes you have Excel or another way to manipulate CSV files and set cell formatting.

If you have git installed, use the command:

`git clone https://github.com/ChrisQGeorge/Monarch-Backfill-Balance-History-From-Transactions.git`


Otherwise, download the Zip file by hitting the "code" button and clicking "download zip" and then extract

## Setup

1. Import any transactions into the account in Monarch
2. Export the transactions using the "Edit" dropdown and clicking "Download Transactions"
3. If using Excel format the date format to "general" to convert to the number of days since 1900 and save
4. Place the file in the "import" directory
5. run the main.py file with the command "python main.py" in the terminal in the project directory
6. Follow the instructions in the terminal
  * Note: If you get an error at this step, try deleting the content in the merchant, category, Original Statement,	Notes, and tags columns, but do not delete the columns themselves; they should just be blank. There should be gaps between the date, account, and amount columns.
  * If you do delete the column data, the table should look like the following [Date][    ][    ][Account][    ][Amount][    ]; it should not look like [Date][Account][Amount]
8. Open the generated CSV file in the "export" directory
9. Format the dates to the format "yyyy-mm-dd" and save
10. Go to the account in Monarch, hit the edit button, click "Upload Balance History" and select the generated file 
11. You're done!

Note: You may find that the balances go into the negative or otherwise being incorrect. This is most likely
caused by duplicate transactions or incorrect transactions. To fix this, you will need to clean your transaction history, and you can use the balances
as an indicator of where to look. Remember that this will start at the newest transaction and work backward, so if you have a bad balance at a given date,
look for transactions after that date.
