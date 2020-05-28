import csv
with open('jeop_quest.csv', newline='') as csvfile:
 quest = csv.DictReader(csvfile)
 rows = list(quest)
 for row in rows[2:4]:
    print(row)

    

# data = csv.DictReader(open("jeop_quest.csv"))
# print("CSV file as a dictionary ROW-------------------------------------------------------------------------------:\n")
# for row in data:
#    print(row)

