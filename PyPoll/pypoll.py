import os
import csv
#---------------------------------
#READ CSV FILE ELECTION_DATA
csvpath = os.path.join('Election_data.csv')

#create dictionary for candidate name
candidates = {}
candidates = dict()

# a dictionary of a candidate 
candidates = {"name":"Khan"}

## Add candidates to the dictionary 
candidates["name"] = "Correy"
candidates["name"] = "O'Tooley"
candidates["name"] = "Li"

candidates_list = [
    "Khan", 
    "Correy", 
    "O'Tooley", 
    "Li"]

candidates["name"] = candidates_list
#--------------------------------------------------
#create other variables in dictionary 
voter_county = {
    "county_1": "Marsh",
    "county_1": "Queen",
    "county_3": "Bamoo",
    "county_4": "Trandee"
}

## Other varaibles for calculation 
Voter_ID = 0
total_votes = 0 

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
        Voter_ID = row[0]
        total_votes = len(row[0])


#Print variable values
print(f"Election Results")
print(f"Total Votes: {total_votes}")
print(f"{candidates_list}")
print(f"Winner: Kahn")

# percentage of votes received, total number of votes

#print winner of the election 
# print only the candidates name 
#print(candidates)
