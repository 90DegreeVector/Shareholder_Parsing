"""
Import the bank_accounts.py (which is uploaded here as a .txt file, you'll have to rename it to .py) file and use the account_info list to generate a CSV file from the list of dictionaries.
There should be a header (the keys in the dict) and then the rest of the data.  One thing to add in for both the header and the in the data is the last_activity_date and then a formatted date in the data.
Call the file bank_account_info.csv.

BONUS:
At the end of writing the file print out, in a nice format, some statistics such as M-F ratio, average bank account value, max and min ages, how many people per state.

NOTE:  This can all be done in ONE loop.   Don’t over complicate this!!  Without the bonus, it took me 7 lines of code!!
"""

import bank_accounts as ba
from datetime import datetime
import csv

header = []
ages = []

for k in ba.account_info[0]:
    header.append(k)
header.append('last_activity_date')
stats = {'total_bank_account': 0, 'gender': {'Male': 0, "Female": 0}}
print(header)
balance = []
with open('bank_account_info.csv', 'w', newline='') as csvfile:
    bankwriter = csv.DictWriter(csvfile, fieldnames=header)
    bankwriter.writeheader()
    for n in ba.account_info:

        n['last_activity_date'] = datetime.today()
        stats['total_bank_account'] += int(n['balance'])
        balance.append(int(n['balance']))
        ages.append(int(n['age']))

        if n['gender'] == 'M':
            stats['gender']['Male'] += 1
        else:
            stats['gender']['Female'] += 1
        bankwriter.writerow(n)



stats['Max Age>'] = max(ages)
stats['Min Age'] = min(ages)
stats['gender']['Ratio'] = stats['gender']['Male']/stats['gender']['Female']
stats['Avg Bank Account'] = stats['total_bank_account']/len(ba.account_info)
stats['Max Bank Account'] = max(balance)
stats['Min Bank Account'] = min(balance)
print(stats)
