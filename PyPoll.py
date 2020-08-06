# The data we need to retrieve
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote

# Steps:
# 1. Open the data file.
# 2. Write down the names of all the candidates.
# 3. Add a vote count for each candidate.
# 4. Get the total votes for each candidate.
# 5. Get the total votes cast for the election.

print("Elections! Elections! Elections!")

import csv
dir(csv)

# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

#1. Open the file to load
with open(file_to_load) as election_data:

# To do: perform analysis
    print(election_data)





import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)


# Create a filename variable to a direct or indirect path to the file.
file_to_save =os.path.join("Resources","election_analysis.txt") 
# Using the with statement open the file as a text file.
with open(file_to_save,"w") as txt_file:
    # Write three counties to the file.
    txt_file.write("Counties in the Election:\nArapahoe\nDenver\nJefferson")

import csv
import os
#assign a variable to load a file from path
file_to_load = os.path.join("Resources", "election_results.csv")

#assign a variable to save the file to a path
file_to_save = os.path.join("analysis","election_analysis.txt")

#open the election results and read the file
with open(file_to_load) as election_data:

    #to do: read and analyze the data here
    #read the file object with the reader function
    file_reader = csv.reader(election_data)

 # Read and print the header row.
    headers = next(file_reader)
    print(headers)