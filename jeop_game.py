import csv
with open('jeop_quest.csv', newline='') as csvfile:
 quest = csv.DictReader(csvfile)
 rows = list(quest)
 for row in rows[0:4]:
    print(row)



# This code gives a KEY error

# with open('jeop_quest.csv', newline='') as csvfile:
#  quest = csv.DictReader(csvfile)
#  rows = list(quest)
#  for row in rows[0:4]:
#     print(row['Show Number'], row['Air  Date'], row['Round'])

    
 # This code works
# data = csv.DictReader(open("jeop_quest.csv"))
# print("CSV file as a dictionary ROW-------------------------------------------------------------------------------:\n")
# for row in data:
#    print(row)

