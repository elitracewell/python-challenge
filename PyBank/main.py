import os
import csv

# Set the path for the csv file
csvpath = os.path.join(".", "Resources", "budget_data.csv")

# Set the path for the output file
output_path = os.path.join(".", "analysis", "financial_analysis.txt")

# Initialize variables
total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
profit_loss_change_list = []
greatest_increase = ['', 0]
greatest_decrease = ['', 9999999999999999999]

# Read the csv file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Loop through the rows in the csv file
    for row in csvreader:
        # Calculate the total number of months
        total_months += 1

        # Calculate the total profit/loss
        total_profit_loss += int(row[1])

        # Calculate the profit/loss change
        profit_loss_change = int(row[1]) - previous_profit_loss
        profit_loss_change_list.append(profit_loss_change)

        # Calculate the greatest increase in profits
        if profit_loss_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = profit_loss_change

        # Calculate the greatest decrease in profits
        if profit_loss_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = profit_loss_change

        # Set the previous profit/loss to the current profit/loss for the next iteration
        previous_profit_loss = int(row[1])

# Calculate the average change in profit/loss
average_profit_loss_change = sum(profit_loss_change_list[1:]) / len(profit_loss_change_list[1:])

# Format the results
results = f"""Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_profit_loss}
Average Change: ${round(average_profit_loss_change, 2)}
Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})
Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})"""

# Print the results to the terminal
print(results)

# Write the results to the output file
with open(output_path, "w") as outfile:
    outfile.write(results)