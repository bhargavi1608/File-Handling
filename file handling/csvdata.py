# For reading csv file


# import csv
# file = open("data.csv","r")
# readObj = csv.reader(file)
# for row in readObj:
#     print(row)
# file.close

# writing a csv file

import csv
file = open("data.csv","w")
csvWriter = csv.writer(file)
header=["name","rollno"]
data =[
   
    ["Abhinaya","23951A0504"],
    ["Ashritha","23951A0501"],
    ["Rachel","23951A0517"]
]
csvWriter.writerow(header)
csvWriter.writerows(data)