#PyBank Script: Analyzing budget data records
#                   -months included
#                   -net total profits/losses
#                   -changes in profits/losses & average of changes
#                   -greatest increase in profits
#                   -greatest decrease in profits

#choose csv file to read from
#file='Resources/budget_data.csv'

#with open(file, 'r') as text:
#    lines=text.read()
#    print(lines)

#lets us create file path across operating systems
import os

#enables the reading of csv files
import csv

#set the path to chosen csv file
csvpath=os.path.join('Resources','budget_data.csv')

#translating our csv file to be read in python
with open(csvpath) as csvfile:
    
    #specify variable and delimiter
    csvreader=csv.reader(csvfile, delimiter=',')

    print(csvreader)
    
    #to read out header row
    csv_header=next(csvreader)
    print(f"CSV Header: {csv_header}")
   
    #read each row after header
    for row in csvreader:
        print(row)