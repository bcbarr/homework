import csv
import os

#variables
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
tooley_votes = 0

#find the data
election_data = os.path.join('Resources', 'election_data.csv')

#read the file
with open(election_data) as csvfile:

	# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #uncomment to print
    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    #uncomment to show header
    #print(f"CSV Header: {csv_header}")

    #read through each row
    for row in csvreader:
    	total_votes += 1

    	if row[2] == str("Khan"):
    		khan_votes += 1

    	if row[2] == str("Correy"):
    		correy_votes += 1

    	if row[2] == str("Li"):
    		li_votes += 1

    	if row[2] == str("O'Tooley"):
    		tooley_votes += 1

if khan_votes > correy_votes and khan_votes > li_votes and khan_votes > tooley_votes:
	winner = ("Khan")

if correy_votes > khan_votes and correy_votes > li_votes and correy_votes > tooley_votes:
	winner = ("Khan")

if li_votes > correy_votes and li_votes >khan_votes and li_votes > tooley_votes:
	winner = ("Khan")

if tooley_votes > correy_votes and tooley_votes > li_votes and tooley_votes > khan_votes:
	winner = ("Khan")

print("Election Results")
print("------------------------------------------------------------------------------------")
print(("Total Votes: ") + str(total_votes))
print("------------------------------------------------------------------------------------")
print("Khan: " + "{:.2%}".format(khan_votes/total_votes) + " (" + str(khan_votes) + ")")
print("Correy: " + "{:.2%}".format(correy_votes/total_votes) + " (" + str(correy_votes) + ")")
print("Li: " + "{:.2%}".format(li_votes/total_votes) + " (" + str(li_votes) + ")")
print("O'Tooley: " + "{:.2%}".format(tooley_votes/total_votes) + " (" + str(tooley_votes) + ")")
print("------------------------------------------------------------------------------------")
print("Winner: " + str(winner))

text_file = open("electrion_results.txt", "w")
text_file.write("Election Results\n")
text_file.write("-----------------------------------------------------------------\n")
text_file.write(("Total Votes: ") + str(total_votes) + "\n")
text_file.write("Khan: " + "{:.2%}".format(khan_votes/total_votes) + " (" + str(khan_votes) + ")\n")
text_file.write("Correy: " + "{:.2%}".format(correy_votes/total_votes) + " (" + str(correy_votes) + ")\n")
text_file.write("Li: " + "{:.2%}".format(li_votes/total_votes) + " (" + str(li_votes) + ")\n")
text_file.write("O'Tooley: " + "{:.2%}".format(tooley_votes/total_votes) + " (" + str(tooley_votes) + ")\n")
text_file.write("------------------------------------------------------------------------------------\n")
text_file.write("Winner: " + str(winner))
