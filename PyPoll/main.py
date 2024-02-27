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

#specifying column indexes for date and profit/loss
column_index_voterid = 0
column_index_county = 1
column_index_candidate = 2

#empty lists to store column data
column_list_voterid = []
column_list_county = []
column_list_candidate = []

#open csv file & read
with open(csv_file, 'r') as file:
    csv_reader=csv.reader(file)

    #skips header row
    next(csv_reader)

    #start to extract data
    for row in csv_reader: