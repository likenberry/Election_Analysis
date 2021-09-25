# The data we need to retrieve.
# Add our dependecies.
import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:


    # To do: read and analyze the data here:
    # Read the file oject with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as text_file:

    # Create a header and a line break
    text_file.write("Counties in the Election\n")
    text_file.write("-------------------------\n")
    # Write some counties to the file.
    text_file.write("Arapahoe\nDenver\nJefferson")
    

# Close the file using with close statement (always remember to close an open file)
    text_file.close
# 1. The total number os votes cast
# 2. A complete list of candidates
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winder of the election based on popular vote.

