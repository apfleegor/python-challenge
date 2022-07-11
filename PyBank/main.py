# PyBank
# Alexandra Pfleegor
# instructions: create a Python script to analyze the financial records of your company

# import necessary libraries
import os
import csv

# create path for CSV file
budget_csv = os.path.join('Resources', 'budget_data.csv')

# define a function to analyize the records
# company data is a list of lists
def py_bank (company_data):

    # calculate total number of months included in the dataset
    total_months = len(company_data)

    # calculate net total amount of "Profit/Losses" over the entire period
    net_total = 0
    for month in company_data:
        net_total += int(month[1])

    # create list for changes in profit / losses
    changes = []
    for i in range(total_months - 1):
        change = int(company_data[i + 1][1]) - int(company_data[i][1])
        changes.append(change)
    
    # calculate changes in "Profit/Losses" over the entire period, and then the average of those changes
    total_changes = sum(changes)
    average_changes = total_changes / (total_months - 1)

    # calculate greatest increase in profits (date and amount) over the entire period
    greatest_inc = max(changes)
    increase_index = (changes.index(greatest_inc)) + 1

    # calculate greatest decrease in profits (date and amount) over the entire period
    greatest_dec = min(changes)
    decrease_index = (changes.index(greatest_dec)) + 1

    # print the analysis to the terminal and export a text file with the results
    # declare the file path for the results
    output_path = os.path.join("analysis", "PyBank_Analysis.txt")

    # write results in text file
    with open(output_path, 'w') as f:
        f.write("Financial Analysis\n")
        f.write("----------------------------\n")
        f.write("Total Months: " + str(total_months) + "\n")
        f.write("Total: $" + str(total_changes) + "\n")
        f.write("Average Change: $" + str("{:.2f}".format(average_changes)) + "\n")
        f.write("Greatest Increase in Profits: " + company_data[increase_index][0] + "($" + str(greatest_inc) + ")\n")
        f.write("Greatest Decrease in Profits: "+ company_data[decrease_index][0] + "($" + str(greatest_dec) + ")")

    # print results to terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {str(total_months)}")
    print(f"Total: ${str(total_changes)}")
    print("Average Change: $" + str("{:.2f}".format(average_changes)))
    print(f"Greatest Increase in Profits: {company_data[increase_index][0]} (${str(greatest_inc)})")
    print(f"Greatest Decrease in Profits: {company_data[decrease_index][0]} (${str(greatest_dec)})")


# read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # loop through the data to create an input for the function
    budget_data = [row for row in csvreader]
    
    # run the function
    py_bank(budget_data)
