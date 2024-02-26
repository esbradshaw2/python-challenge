#PyBank Script: Analyzing budget data records
#                   - total # months included
#                   -net total profits/losses
#                   -changes in profits/losses & average of changes
#                   -greatest increase in profits
#                   -greatest decrease in profits

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

#open csv file & read
with open(csv_file, 'r') as file:
    csv_reader=csv.reader(file)

    #skips header row
    next(csv_reader)

    #start to extract data
    for row in csv_reader:

        #adds the values in the specified rows of the specified column into respective lists
        column_list_date.append(row[column_index_date])
        column_list_pl.append(row[column_index_pl])

        #convert profit/loss column values into integers so we can treat them as numbers with our functions
        pl_as_numbers=[int(value) for value in column_list_pl]
        
        #count number of items in list using len function
        month_count=len(column_list_date)
        
        #add all profit/loss values together to get a net total
        net_total_pl=sum(pl_as_numbers)
        
        

        #empty list to store change values
        pl_changes = []

        #for each profit or loss value within the column...
        for pl_value in range(1, len(pl_as_numbers)):
            
            #calculate change from one row to the next
            calculated_changes = pl_as_numbers[pl_value] - pl_as_numbers[pl_value - 1]

            #add these change values to the empty list
            pl_changes.append(calculated_changes)

            #calculate average of all profit/loss changes over time, rounded to two decimal places
            average_pl_change = round((sum(pl_changes) / len(pl_changes)), 2)

            #find greatest increase and decrease in profit/loss by finding max and min value in profit/loss change list
            greatest_increase = max(pl_changes)
            greatest_decrease = min(pl_changes)

            #create a dictionary to store the change values and dates together so they can be cross-referenced
            pl_change_dictionary = {
                                    'change': pl_changes, 
                                    'date': column_list_date
                                    }
            
            #find the greatest increase value within the change list...
            date_index_1 = pl_change_dictionary['change'].index(max(pl_changes))

            #...and find the corresponding date for the greatest increase value
            #"plus 1" because a change doesn't actually happen corresponding with the first date
            corresponding_date_increase = pl_change_dictionary['date'][date_index_1 + 1]

            #find the greatest decrease value within change list...
            date_index_2 = pl_change_dictionary['change'].index(min(pl_changes))

            #... and find the corresponding date for the greatest decrease value
            corresponding_date_decrease = pl_change_dictionary['date'][date_index_2 + 1]

#print results to terminal
    #using "\n" to physically separate each value into different rows (stacked row by row in this file for organizational purposes)
print("Financial Analysis", "--------------------------", f"Total Months: {month_count}", f"Total: ${net_total_pl}", f"Average Change: ${average_pl_change}", f"Greatest Increase in Profits: {corresponding_date_increase} (${greatest_increase})", f"Greatest Decrease in Profits: {corresponding_date_decrease} (${greatest_decrease})", sep='\n')

#set the file name for the text file
file_name = "pybank_results.txt"

#export analysis to a text file
with open(file_name, 'w') as file:
    print("Financial Analysis", "--------------------------", f"Total Months: {month_count}", f"Total: ${net_total_pl}", f"Average Change: ${average_pl_change}", f"Greatest Increase in Profits: {corresponding_date_increase} (${greatest_increase})", f"Greatest Decrease in Profits: {corresponding_date_decrease} (${greatest_decrease})", sep='\n', file=file)

    

#save text file to analysis folder
    #file_name = "pybank_results.txt"
    #destination_folder = "analysis"
    #os.rename(file_name, os.path.join(destination_folder, file_name))