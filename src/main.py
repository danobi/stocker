#!/usr/bin/python
import stocker
import os.path
import yql
import matplotlib.pyplot as plt
import datetime

#This function assumes that filename is valid and not currently in use
def export_csv(filename,data):
    myfile = open(filename,'a')
    for i in range(0,len(data)):
        myfile.write('\n' + data[i])
    myfile.close()

#Takes in CSV data and displays a graph
def export_returns_graph(data):
    #First we create 2 lists: dates and returns
    dates = []
    returns = []
    index = 0
    for line in data:
        items = []
        items = line.split(',')
        #dates.append(items[0])
        dates.append(index)
        index += 1
        returns.append(float(items[1]))

    #Make graph
    plt.plot(dates,returns)
    plt.xlabel('Data points')
    plt.ylabel('Return value')
    #plt.axis(dates[0],dates[len(dates)-1],min(returns),max(returns))
    plt.show()

startdate = datetime.date(2000,02,01)
enddate = datetime.date(2014,02,01)
data = stocker.get_historical_data('AAPL')
csv_data = stocker.get_returns(data,7,startdate,enddate)
export_returns_graph(csv_data)


