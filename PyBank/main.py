#------------------------------------------------------------
# Python script that analyzes records in the budget_data file
#------------------------------------------------------------

#Read the csv file by importing the module and setting the path
import os
import csv

#Open the file in read mode
with open('./Resources/budget_data.csv', 'r') as budget_file_csv:

    #Create an object to read
    csvreader = csv.DictReader(budget_file_csv, delimiter=',')

    #Create lists to store the columns data
    date_col = []
    profit_losses_col = []

    #For each column in the object
    for col in csvreader:

        #Add each month to a list and count the total items in the list
        date_col.append(col["Date"])
        total_months = len(date_col)

        #Add each month's profit/loss to a list and convert to integer
        profit_losses_col.append(col["Profit/Losses"])
        profit_losses_col = [int(i) for i in profit_losses_col]

        #Calculate the net total profit/loss        
        net_total = 0
        for i in profit_losses_col:
            net_total += i

            #Calculate the profit/loss change and store in a list
            changes_col = [profit_losses_col[i + 1] - profit_losses_col[i] for i in range(len(profit_losses_col) - 1)]

    #Calculate the average pofit/loss change
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
#Reference: https://geeksforgeeks.org/writing-to-file-in-python/
with open('./analysis/analysis_results.txt', 'w') as f:
    #Define the data to write as a list
    analysis_results = ['Financial Analysis',
                    '', '-------------------------------------------------',
                    '', 'Total Months: ' + str(total_months),
                    '', 'Total: $' + str(net_total),
                    '', 'Average Change: $' + str(average_change),
                    '', 'Greatest Increase in Profits: ' + str(increase_month) + " ($" + str(increase) + ")",
                    '', 'Greatest Decrease in Profits: ' + str(decrease_month) + " ($" + str(decrease) + ")"]
    #Use a loop to write each line in list to the file
    for line in analysis_results:
        f.write(line + '\n')
        print(line)