#  The data we need to retrieve
# 1.  The total number of votes cast
# 2.  A complete list of candidates who received votes
# 3.  The percentage of votes each candidate won
# 4.  The total number of votes each candidate won
# 5.  The winner of the election based on popular vote.
import csv
import os
#print csv
#print os
# Assign a variable for the file to load and the path.
# file_to_load = os.path.join("Resources", "election_results.csv")
#file_to_load = 'election_results.csv'
#file_to_load =  'C:\Users\mflow\Test_Election_Analysis\Resources\election_results.csv'
# Open the election results and read the file.
# with open(file_to_load) as election_data:
#file_to_save = "election_analysis.txt"
#outfile = open(file_to_save, "w")
#outfile.write("Hello all")
#outfile.close()
f = open("election_results.csv")
#print(f.read())
# Read the file object with the reader function
# Read the file object with the reader function.
file_reader = csv.reader(f)
# Print the header row.
headers = next(file_reader)
print(headers)
#file_reader = csv.reader(f)
#for row in file_reader:
#   print(row)

    # Print the file object.
 #    print(election_data)
 #    print (file_to_load)
print("I AM DONE")

# Create a filename variable to a direct or indirect path to the file.
file_to_save =  ("election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Hello Worlda")