import csv

# Reads csv a prints it in lists
with open('jeop_quest.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter= '\t')

    for line in reader:
        print(line[1])   #prints lines ([1] prints index 1)

