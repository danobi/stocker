#!/usr/bin/python
import yql
import datetime

DATATABLES_URL = 'store://datatables.org/alltableswithkeys'
HISTORICAL_URL = 'http://ichart.finance.yahoo.com/table.csv?s='
YAHOO_QUOTES = 'yahoo.finance.quotes'

#Returns a YQL object of the historical data
def get_historical_data(symbol):
    yql_object = yql.Public()
    query = 'select * from csv where url=\'%s\' and columns=\"Date,Open,High,Low,Close,Volume,AdjClose\"'% (HISTORICAL_URL + symbol)
    return yql_object.execute(query,env=DATATABLES_URL)

#Gets current quotes (today) and returns a YQL object
def get_current_quotes(symbol):
    yql_object = yql.Public()
    query = 'select * from "%s" where symbol="%s"' % (YAHOO_QUOTES,symbol)
    return yql_object.execute(query,env=DATATABLES_URL)

#Returns list of all formatted returns 
#startdate and enddate MUST be accurate(ie. trades occured that day) and real dates of type date
#interval is in DAYS
def get_returns(data,interval,startdate,enddate):
    return_list = []
    old_sell_price = 0.0
    new_sell_price = 0.0
    old_sell_date = datetime.date(startdate.year,startdate.month,startdate.day)
    for row in reversed(data.rows):
        raw_current_date = row['Date']

        #When the current date is 'Date', it generates an error
        if raw_current_date == 'Date':
            continue

        date_list = raw_current_date.split('-')
        current_date = datetime.date(int(date_list[0]),int(date_list[1]),int(date_list[2]))

        #Check if within bounds
        if current_date >= startdate and current_date <= enddate:
            #Format and append data
            if current_date == old_sell_date:
                old_sell_price = row['Close']
            elif current_date >= old_sell_date + datetime.timedelta(days=interval):
                new_sell_price = row['Close']

                #Calculate return
                _return = (float(new_sell_price) / float(old_sell_price)) - 1
                return_list.append("\"%s - %s\",%.4f" % (old_sell_date,current_date,_return))

                #update variables
                old_sell_date = datetime.date(int(current_date.year),int(current_date.month),int(current_date.day))
                old_sell_price = row['Close']
    return return_list

"""Beginning of execution
#This code should run and do stuff if uncommented, but won't display anything
#Fix/change it to make it work if you want
symbol = raw_input("Please enter in stock symbol: ")
action = raw_input("What information would you like? (returns, current,TBA): ")
if action == 'returns':
    raw_startdate = raw_input("Please enter start date (YYYY-MM-DD): ")
    raw_enddate = raw_input("Please enter end date (YYYY-MM-DD): ")
    raw_interval = raw_input("Please enter sample rate (week,month,year): ")

    Format dates
    start_list = raw_startdate.split('-')
    end_list = raw_enddate.split('-')
    startdate = datetime.date(int(start_list[0]),int(start_list[1]),int(start_list[2]))
    enddate = datetime.date(int(end_list[0]),int(end_list[1]),int(end_list[2]))

    #Format interval
    interval = 0
    if raw_interval == 'week':
        interval = 7
    elif raw_interval == 'month':
        interval = 31  #TODO: make this more accurate
    else:
        interval = 365 #TODO: make this more accurate

    #Pull data
    data = get_historical_data(symbol)

    #Get return data
    csv_data = get_returns(data,interval,startdate,enddate)

elif action == 'current':
    data = get_current_quotes(symbol)
"""

