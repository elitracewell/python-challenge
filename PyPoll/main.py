import os
import csv

# Define file path
file_path = os.path.join("Resources", "election_data.csv")
output_path = os.path.join("analysis", "election_analysis.txt")

# Initialize variables
total_votes = 0
candidates = {}
winner_votes = 0
winner = ""

# Read in the CSV file
with open(file_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip header row
    header = next(csvreader)
    
    # Loop through rows in CSV
    for row in csvreader:
        # Increment total votes
        total_votes += 1
        
        # Check if candidate is in dictionary of candidates
        if row[2] in candidates:
            candidates[row[2]] += 1
        # If candidate is not in dictionary, add them and set their vote count to 1
        else:
            candidates[row[2]] = 1

#  Print election results to terminal and export to text file
with open(output_path, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    
    # Loop through candidates dictionary to calculate and print their stats
    for candidate, votes in candidates.items():
        vote_percentage = round((votes/total_votes)*100, 3)
        txtfile.write(f"{candidate}: {vote_percentage}% ({votes})\n")
        
        # Check if candidate is the new winner
        if votes > winner_votes:
            winner_votes = votes
            winner = candidate
            
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")
    
    # Print results to terminal
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    
    # Loop through candidates dictionary to calculate and print their stats
    for candidate, votes in candidates.items():
        vote_percentage = round((votes/total_votes)*100, 3)
        print(f"{candidate}: {vote_percentage}% ({votes})")
        
        # Check if candidate is the new winner
        if votes > winner_votes:
            winner_votes = votes
            winner = candidate
            
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")