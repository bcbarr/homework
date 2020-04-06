

import csv
import os

#find the data
budget_data = os.path.join('Resources', 'budget_data.csv')

# initial set total to 0
total_pl = 0								#set initial total profit/loss
month = 0									#set initial value for month counter
greatest_increase = 0						#set value for greatest increase each month for data
greatest_decrease = 0						#set value for greatest decrease each month for data
previous_month_pl = 0						#sets initial value for the previous months's profit loss to calculate change
change_list = []							#creates an empty list to place change values into

#read the file
with open(budget_data) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #uncomment to print
    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    #uncomment to show header
    #print(f"CSV Header: {csv_header}")

# Read each row of data after the header
    for row in csvreader:

    	#grab the date for that row
    	date = row[0]
    	
    	#add 1 to the month counter
    	month += 1

    	#Sum the total profit loss for all data
    	total_pl += int(row[1])

    	#Calculate the change in profit/loss each month and save to a list
    	change = (int(row[1])-previous_month_pl)
    	change_list.append(change)

    	#check to see if change is the greatest increase
    	if change > greatest_increase:
    		greatest_increase = change
    		greatest_increase_date = date

    	if change < greatest_decrease:
    		greatest_decrease = change
    		greatest_decrease_date = date

    	#set the previous month profit/loss to the next amount
    	previous_month_pl = int(row[1])

    	

    	
#Calculate the mean of the changes over the period
change_sum = sum(change_list)				#first sum all numbers in list
average_change = change_sum/month 			#divide by number of months(values)




#Print a nice Summary to consol
print("Financial Analysis")
print("-----------------------------------------------------------------")
print("Total Months: " + str(month))
print("Total: $" + str(total_pl))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + str(greatest_increase_date) + " " + "$"+ str(greatest_increase))
print("Greatest Decrease in Profits: " + str(greatest_decrease_date) + " " + "$"+ str(greatest_decrease))

#write the summary to a text file


text_file = open("Financial Analysis.txt", "w")
text_file.write("Financial Analysis\n")
text_file.write("-----------------------------------------------------------------\n")
text_file.write("Total Months: " + str(month) + "\n")
text_file.write("Total: $" + str(total_pl) + "\n")
text_file.write("Average Change: $" + str(average_change) + "\n")
text_file.write("Greatest Increase in Profits: " + str(greatest_increase_date) + " " + "$"+ str(greatest_increase) + "\n")
text_file.write("Greatest Decrease in Profits: " + str(greatest_decrease_date) + " " + "$"+ str(greatest_decrease))

