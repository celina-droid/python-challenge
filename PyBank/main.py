import os
import sys
import csv
#open CSV File
csvpath = os.path.join('PyBank/budget_data.csv')
with open(csvpath) as csvfile:
    #Read and delimit the data
    csvreader=csv.reader(csvfile,delimiter=',')
    #Initialize Variable
    months=0
    profit_loss=0
    # Counts the Total Rows
    rows=[r for r in csvreader]
    #Defaulting to the First Value available in the Sheet
    change_profit_loss= 0 #int(rows[1][1])
    maxprof = [0, 0]
    minprof  = [0, 9999999999999999]
    maxprof[1] = 0
   
    #Looping through Data
    for i in range(2,len(rows)):
        
        months=months+1
        row=rows[i]
        profit_loss= int(row[1]) + profit_loss
        
        #Excluding the Header Row
        if i > 1:
            if int(row[1])-int(rows[i-1][1]) > maxprof[1]: #check if current change in profit is greater than maxprof change already known
                maxprof[1] = int(row[1])-int(rows[i-1][1]) #then make maxprof to be the current change
                maxprof[0] = row[0]
            if int(row[1])-int(rows[i-1][1]) < minprof[1]:  #check if current change in profit/loss is less than minprof change already known
                 minprof[1] = int(row[1])-int(rows[i-1][1]) # Then make minprof to be the current change
                 minprof[0] = row[0]
            change_profit_loss=change_profit_loss + float(row[1])-float(rows[i-1][1]) 
        
#Calculating Average and Average Change in profit_loss
average_change_profit_loss='{0:.2%}'.format(change_profit_loss/months)

#Printing the Outputs
print("Financial Analysis")
print("------------------")
print("Total Months: " + str(months))
print("Total: " +"$" +str(profit_loss))       
print("Average Change: " +"$"+ str(average_change_profit_loss))
print("Greatest Increase in profit_:" + str(maxprof[0])+" ($" + str(maxprof[1])+")")
print("Greatest Decrease in loss:" + str(minprof[0])+" ($" + str(minprof[1])+")")

