#PyPoll Script: analyzing votes and calculating:
#                   -total # votes cast
#                   -list of all candidates who recieved votes
#                   -percentage of votes each candidate won
#                   -total # votes each candidate won
#                   -winner of election based on popular vote

#lets us create file path across operating systems
import os

#enables the reading of csv files
import csv

#set the path to chosen csv file
csv_file=os.path.join('Resources','election_data.csv')

#specifying column indexes
column_index_candidate = 2

#empty lists to store column data
column_list_candidate = []

candidate_dict = {}

    # {name: count,
    #  name: count}

#open csv file & read
with open(csv_file, 'r') as file:
    csv_reader=csv.reader(file)

    #skips header row
    next(csv_reader)

    #start to extract data
    for row in csv_reader:

        #adds the values in the specified rows of the specified column into respective lists
        column_list_candidate.append(row[column_index_candidate])

        #count number of voters in list using len function
        vote_count=len(column_list_candidate)

        #find all candidates who recieved votes, and the total number of their votes
        name = row[2]
        if name in candidate_dict:
            candidate_dict[name] = candidate_dict[name] + 1
        else:
            candidate_dict[name]=1
        

#print results to terminal
#using "\n" to physically separate each value into different rows
print("Election Results", "--------------------------", f"Total Votes: {vote_count}", "--------------------------", sep='\n')

for name, count in candidate_dict.items():
    percentage = (count / vote_count) * 100
    print(f'{name}: {percentage:.3f}% ({count})')

#for name, count in candidate_dict.items():
    #candidate_winner = max(percentage)

print("--------------------------", "Winner: candidate_winner", "--------------------------", sep='\n')




#set the file name for the text file
file_name = "pypoll_results.txt"

#export analysis as the text file
with open(file_name, 'w') as file:
    print("Election Results", "--------------------------", f"Total Votes: {vote_count}", "--------------------------", sep='\n', file=file)

    for name, count in candidate_dict.items():
        percentage = (count / vote_count) * 100
        print(f'{name}: {percentage:.3f}% ({count})', file=file)

    #for name, count in candidate_dict.items():
        #candidate_winner = max(percentage)

    print("--------------------------", "Winner: candidate_winner", "--------------------------", sep='\n', file=file)
