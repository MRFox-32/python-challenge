#------------------------------------------------------------
# Python script that analyzes records in the election_data file
#------------------------------------------------------------

#Read the csv file by importing the module and setting the path
import os
import csv

#Define the path to the csv
election_data_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

#Create lists to store column data
ballotid_col = []
candidate_col = []

#Open and read the csv
with open(election_data_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Read the header row
    column_names = next(csvreader)

    #Loop through the csv data
    for row in csvreader:

        #Make a list for each column
        ballotid_col.append(row[0])
        candidate_col.append(row[2])

        #Count the total number of votes
        total_votes = len(ballotid_col)

    #Create a list of unique Candidate names and sort
    candidate_list = list(set(candidate_col))
    candidate_list.sort()

    #Create a list of the total number of votes per candidate
    popular_vote = [candidate_col.count(x) for x in candidate_list]

    #Create a list that calculates the percentage of votes for each candidate
    for i in popular_vote:
        percentage = [round((popular_vote[i] / total_votes) * 100, 3) for i in range(len(popular_vote))]
    
    #Identify the winner: find max popular vote, index location in list, find candidate name using location in list
    winner_votes = max(popular_vote)
    winner_index = popular_vote.index(winner_votes)
    winner = candidate_list[winner_index]
    
#Print results to terminal and text file by first opening the file, when with ends file autmoatically closes.
with open('PyPoll/analysis/analysis_results.txt', 'w') as f:
    
    #Define the data as a list to write to file
    analysis_results = ["Election Results",
                    "", "-----------------------------------------",
                    "", "Total Votes: " + str(total_votes),
                    "", "-----------------------------------------",
                    "", str(candidate_list[0]) + ": " + str(percentage[0]) + "% " + "(" + str(popular_vote[0]) + ")",
                    "", str(candidate_list[1]) + ": " + str(percentage[1]) + "% " + "(" + str(popular_vote[1]) + ")",
                    "", str(candidate_list[2]) + ": " + str(percentage[2]) + "% " + "(" + str(popular_vote[2]) + ")",
                    "", "-----------------------------------------",
                    "", "Winner: " + str(winner), "", "-----------------------------------------"]
    
    #Use a loop to write each line in list to the file
    #Reference: https://geeksforgeeks.org/writing-to-file-in-python/
    for line in analysis_results:
        f.write(line + '\n')
        print(line)