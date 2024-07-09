#------------------------------------------------------------
# Python script that analyzes records in the budget_data file
#------------------------------------------------------------

#Read the csv file by importing the module and setting the path
import os
import csv

#Define the path to the csv
budget_file_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

#Create lists to store column data
date_col = []
profit_losses_col = []

#Open and read csv
with open(budget_file_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read the header row
    column_names = next(csvreader)

    #Loop through the csv data
    for row in csvreader:

        #Make a list for each column
        date_col.append(row[0])
        profit_losses_col.append(row[1])
        
        #Add each month to a list and count the total items in the list
        total_months = len(date_col)

        #Add each month's profit/loss to a list and convert to integer
        profit_losses_col = [int(i) for i in profit_losses_col]

        #Calculate the net total profit/loss        
        net_total = 0
        for i in profit_losses_col:
            net_total += i

            #Calculate the profit/loss change and store in a list
            changes_col = [profit_losses_col[i + 1] - profit_losses_col[i] for i in range(len(profit_losses_col) - 1)]

    #Calculate the average profit/loss change
    average_change = round(sum(changes_col) / (total_months - 1),2)

    #Add a 0 at the start of the changes_col list ad zip the dates and changes lists together
    changes_col.insert(0,profit_losses_col[0])
    changes_date_col = list(zip(date_col,changes_col))

    #Find the greatest increase of profit/loss, index for location in list, and find the month using that location in dates list 
    increase = max(changes_col)
    increase_index = changes_col.index(increase)
    increase_month = date_col[increase_index]

    #Find the greatest decrease of profit/loss, index for location in list, and find the month using that location in dates list
    decrease = min(changes_col)
    decrease_index = changes_col.index(decrease)
    decrease_month = date_col[decrease_index]

#Print results to terminal and text file by first opening the file, when with ends file autmoatically closes.
with open('PyBank/analysis/analysis_results.txt', 'w') as f:
    
    #Define the data to write as a list
    analysis_results = ["Financial Analysis",
                    "", "-------------------------------------------------",
                    "", "Total Months: " + str(total_months),
                    "", "Total: $" + str(net_total),
                    "", "Average Change: $" + str(average_change),
                    "", "Greatest Increase in Profits: " + str(increase_month) + " ($" + str(increase) + ")",
                    "", "Greatest Decrease in Profits: " + str(decrease_month) + " ($" + str(decrease) + ")"]
    
    #Define the data as a list to write to file
    #Reference: https://geeksforgeeks.org/writing-to-file-in-python/
    for line in analysis_results:
        f.write(line + '\n')
        print(line)