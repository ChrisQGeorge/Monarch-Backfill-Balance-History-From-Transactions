# Monarch-Backfill-Balance-History-From-Transactions
The goal of this script is to backfill the balance history of Monarch money accounts based of an exported transaction history.

## Installation
This program requires Python 3 to be installed on your system and added to your path. https://www.python.org/downloads/

If you have git installed, use the command:

`git clone https://github.com/ChrisQGeorge/Monarch-Backfill-Balance-History-From-Transactions.git`


Otherwise, download the Zip file by hitting the "code" button and clicking "download zip" and then extract

## Setup

1. Import any transactions into the account in Monarch
2. Export the transactions using the "Edit" dropdown and clicking "Download Transactions"
3. If using Excel format the date format to "general" to convert to the number of days since 1900 and save
4. Place the file in the "import" directory
5. run the main.py file with the command "python main.py" in the terminal
6. Follow the instructions in the terminal
7. Open the generated CSV file in the "export" directory
8. Format the dates to the format "yyyy-mm-dd" and save
9. Go to the account in Monarch, hit the edit button, click "Upload Balance History" and select the generated file 
10. You're done!
