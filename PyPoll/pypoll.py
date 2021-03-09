#import modules
import os
import csv
import string
import random
#-------------------------------------------
#READ CSV FILE BUDGET_DATA
csvpath = os.path.join('Election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader) #pop one row 
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)

#--------------------------------------------------------------
#define variables 
def print_percentages(Election_data):
    Voter_ID = int(Election_data[0])
    County = str(Election_data[1])
    Candidate = str(Election_data[2])

print(Voter_ID)
