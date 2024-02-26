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

#specifying column indexes for date and profit/loss
column_index_date = 0
column_index_pl = 1

#empty lists to store column data
column_list_date = []
column_list_pl =[]

#read csv file & extract data
with open(csv_file, 'r') as file:
    csv_reader=csv.reader(file)

    #skips header row
    next(csv_reader)

    for row in csv_reader:

        #adds the values in the specified rows of the specified column into respective lists
        column_list_date.append(row[column_index_date])
        column_list_pl.append(row[column_index_pl])

        #converting profit/loss column values into integers
        pl_as_numbers=[int(value) for value in column_list_pl]
        
        #count number of items in list using len function
        month_count=len(column_list_date)
        net_total_pl=sum(pl_as_numbers)

print("Total Months: ", month_count, (f"Total: ${net_total_pl}"))








