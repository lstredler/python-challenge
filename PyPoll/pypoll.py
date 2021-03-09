#import modules
import os
import csv
#-------------------------------------------
#READ CSV FILE ELECTION_DATA
csvpath = os.path.join('Election_data.csv')

County = " "
Candidate = " "
total_votes = 0 
voter_id = 0
voter_county = " "
voter_name = " "    

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    head = next(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader) #pop one row 
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)
        total_votes +=1

#Print variable values
print(f"Election Results")
print(f"Total Votes: {total_votes}")
#print voter name, percentsge of votes received, total number of votes

#print winner of the election 
