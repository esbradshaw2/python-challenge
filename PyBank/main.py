#PyBank Script: Analyzing budget data records
#                   - total # months included
#                   -net total profits/losses
#                   -changes in profits/losses & average of changes
#                   -greatest increase in profits
#                   -greatest decrease in profits


#with open(file, 'r') as text:
#    lines=text.read()
#    print(lines)

#lets us create file path across operating systems
import os

#enables the reading of csv files
import csv

#set the path to chosen csv file
csv_file=os.path.join('Resources','budget_data.csv')

#specifying column index to extract total number of months
column_index_date = 0

#empty list to store column data
column_list = []

#read csv file & extract data
with open(csv_file, 'r') as file:
    csv_reader=csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        column_list.append(row[column_index_date])
        month_count=len(column_list)

print("Total Months: ", month_count)








