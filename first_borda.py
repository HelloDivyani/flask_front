# importing csv module 
import csv 
  
#print 'Enter the number of input files'
#n=input('Enter the number of input files : ')

# csv file name 
#print 'Enter the file names'
features=[]
#for file in range(int(n)):

#    files.append(raw_input('Enter the file name : '))


  # reading csv file 
with open('process3.csv', 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    filename = csvreader.next() 
    #print(filename)

    # extracting each data row one by one 
    for file in csvreader: 
        #print ('file : ',file)
        for name in file:
            features.append(name)

csvfile.close()
file=filename[0]

with open(file, 'r') as csvfile:
    score=[]
    i=1
    fields=[]

    csvreader = csv.reader(csvfile)
    for f in features:
        if f=='1':
            rows=[]
            fields = csvreader.next()
            csvreader.next()
            for row in csvreader :
                rows.append(row[0])

            x = csvreader.line_num - 1
      
            for row in rows: 
                score.append(x-i)         
                i=i+1
                print "%s\t%d"%(row,score[i-2])

      

csvfile.close()

with open(file, 'r') as csvfile:
    score=[]
    i=1
    fields=[]
    csvreader = csv.reader(csvfile)
    for f in features:
        if f=='2':
            rows=[]
            fields = csvreader.next()
            csvreader.next()
            for row in csvreader :
                rows.append(row[5])

            x = csvreader.line_num - 1
  
            for row in rows: 
                score.append(x-i+1)         
                i=i+1
                print "%s\t%d"%(row,score[i-2])


      

csvfile.close()





















'''
#print files
#print files
#filename = "top_100_mentions.csv"
for filename in files:
    # initializing the titles and rows list 
    fields = [] 
    rows = []
    score = [] 
    x=0
    i=1
    #print filename
 
    # reading csv file 
    with open(filename, 'r') as csvfile: 
        # creating a csv reader object 
        csvreader = csv.reader(csvfile) 
          
        # extracting field names through first row 
        fields = csvreader.next() 
      
        # extracting each data row one by one 
        for row in csvreader: 
            rows.append(row) 
      
            # get total number of rows 
        #print("Total no. of rows: %d"%(csvreader.line_num)) 
        x = csvreader.line_num - 1
        #print('X : %d'%x)
      
        # printing the field names 
        #print('Field names are:' + ', '.join(field for field in fields)) 
          
        #  printing first 5 rows 
        #print('\nFirst 5 rows are:\n') 
        for row in rows: 
            # parsing each column of a row 
            for col in row: 
                score.append(x-i+1)
                #print('x-i+1',x-i+1);
                i=i+1
                print "%s\t%d"%(col,score[i-2])
                

            #print('\n') 
        csvfile.close()

'''