# Monarch-Backfill-Balance-History-From-Transactions
The goal of this script is to backfill the balance history of Monarch money accounts based on an exported transaction history.

## Installation
This program requires Python 3 to be installed on your system and added to your path. https://www.python.org/downloads/

If you have git installed, use the command:

`git clone https://github.com/ChrisQGeorge/Monarch-Backfill-Balance-History-From-Transactions.git`


Otherwise, download the Zip file by hitting the "code" button and clicking "download zip" and then extract

## Setup
### To import monarch transactions
1. Import any transactions into the account in Monarch
2. Export the transactions using the "Edit" dropdown and clicking "Download Transactions"
3. Place the file in the "import" directory
4. run the main.py file with the command "python main.py" in the terminal in the project directory
5. Follow the instructions in the terminal
6. When the instructions prompt for an account value, please put the actual value of the account (positive for asset, negative for liability) rather than the absolute value
7. A generated file will appear in the "Export" directory
8. Go to the account in Monarch, hit the edit button, click "Upload Balance History" and select the generated file 
9. You're done!

### To import Mint trends balance history
1. Go to the trends tab in Mint
2. Select the assets or debts tab and select a particular account
3. Go to the bottom of the page and click the "Export to CSV" button
4. Move the file to the "Import" directory
5. run the main.py file with the command "python main.py" in the terminal in the project directory
6. Follow the instructions in the terminal
7. A generated file will appear in the "Export" directory
8. Go to the account in Monarch, hit the edit button, click "Upload Balance History" and select the generated file 
9. You're done!

Note: You may find that the balances go into the negative or otherwise being incorrect. This is most likely
caused by duplicate transactions or incorrect transactions. To fix this, you will need to clean your transaction history, and you can use the balances
as an indicator of where to look. Remember that this will start at the newest transaction and work backward, so if you have a bad balance at a given date,
look for transactions after that date.
