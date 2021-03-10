#import modules
import os
import csv
import numpy as np
#-------------------------------------------
#READ CSV FILE BUDGET_DATA
csvpath = os.path.join('..', 'Resources','budget_data.csv')

date = " "
profits_losses = 0
net_total = 0 
total_months = 0
total_volume = 0 
max_min = []

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

    for row in csvreader:
        print(row)
        total_months +=1
        total_volume += int(row[1])
        length = len(row[1])
        average_change = total_volume/length
        arr = np.array([row[0],row[1]])

       
# Print out the budget data to terminal 
print(f"Total Months: {total_months}")
print(f"Net Total: {total_volume}")
print(f"Average Change: {average_change}")
print (f"Greatest Increase in Profits: {arr}")
print(f"Greatest Decrease in Losses: {arr}")

# export data to text file int analysis folder - specify file to write  
output_path = os.path.join("..", "output", "Analysis")

#with open(output_path, 'w') as outfile:  
    #csvwriter = csv.writer(csvfile, delimiter=',')
    #csvwriter.writerow(['Total Months:', '86'])
    #csvwriter.writerow(['Net Total:' , '$38,382,578'])
    #csvwriter.writerow(['Average Change:' , '-2315.12'])
    #csvwriter.writerow(['Greatest Increase in Profits', 'Feb-2012 ($1926159)'])
    #csvwriter.writerow(['Greatest Decrease in Losses:', 'Sep-2013 ($-2196167)'])    