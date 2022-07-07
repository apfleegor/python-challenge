# PyPoll
# Alexandra Pfleegor
# instructions: help a small, rural town modernize its vote counting process

# import necessary libraries
import os
import csv

# create path for CSV file
poll_csv = os.path.join('Resources', 'election_data.csv')


# define a function to analyize the votes
# election_data is a list of lists
def py_poll (election_data):

    # calculate the total number of votes cast
    total_votes = len(election_data)

    # create a complete list of candidates who received votes
    candidates = [election_data[0][2]]
    for vote in election_data:
        if vote[2] not in candidates:
            candidates.append(vote[2])

    # calculate the total number of votes each candidate won
    num_votes = []
    for candidate in candidates:
        votes = 0
        for vote in election_data:
            if vote[2] == candidate:
                votes += 1
        num_votes.append(votes)
    
    # calculate the percentage of votes each candidate won
    percent_votes = [(votes / total_votes) * 100 for votes in num_votes]

    # determine the winner of the election based on popular vote.
    winner_index = num_votes.index(max(num_votes))
    winner = candidates[winner_index]

    # print the analysis to the terminal and export a text file with the results
    # declare the file path for the results
    output_path = os.path.join("analysis", "PyPoll_Analysis.txt")

    # print the analysis to a text file
    with open(output_path, 'w') as f:
        f.write("Election Results\n")
        f.write("-------------------------\n")
        f.write("Total Votes: " + str(total_votes) + "\n")
        f.write("-------------------------\n")
        for candidate in candidates:
            index = candidates.index(candidate)
            f.write(candidate + ": " + str("{:.3f}".format(percent_votes[index])) + "% (" + str(num_votes[index]) + ")\n")
        f.write("-------------------------\n")
        f.write("Winner: " + winner + "\n")
        f.write("-------------------------\n")

    # print results to terminal
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {str(total_votes)}")
    print("-------------------------\n")
    for candidate in candidates:
        index = candidates.index(candidate)
        percent = str("{:.3f}".format(percent_votes[index]))
        print(f"{candidate}: {percent}% ({str(num_votes[index])})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

# read in the CSV file
with open(poll_csv, 'r') as csvfile:

    # split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # loop through the data to create an input for the function
    election_data = [row for row in csvreader]
    
    # run the function
    py_poll(election_data)