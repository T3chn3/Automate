import csv

#simple loop over all elements in a CSV
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
for row in exampleReader:
    print('Row #' + str(exampleReader.line_num)+' '+ str(row))

#exampleData = list(exampleReader)
#print(exampleData)