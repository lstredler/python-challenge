#import modules
import os
import csv
import numpy as np
#-------------------------------------------
#READ CSV FILE BUDGET_DATA
csvpath = os.path.join('budget_data.csv')

date = " "
profits_losses = 0
net_total = 0 
total_months = 0
total_volume = 0 
tuple1 = " "
tuple2 = 0

###calculate average
def average(numbers):
    length = len(numbers)
    total = 0.0
    for value in numbers:
        total+= value
    return total/length

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader) #pop one row 
    print(f"CSV Header: {csv_header}")

    total_months = 0
    for row in csvreader:
        print(row[0])
        total_months +=1
        total_volume += int(row[1])
        average_change = total_volume/total_months
        arr = np.array([row[0],row[1]])
        #max_element = np.amax(arr,row[1])
        #tuple1,tuple2 = (date), (profits_losses)
       

# Print out the budget data stored in dictionary 
print(f"Total Months: {total_months}")
print(f"Net Total: {total_volume}")
print(f"Average Change: {average_change}")
print (f"Greatest Increase in Profits: {arr}")
print(f"Greatest Decrease in Losses: {arr}")


