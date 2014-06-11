#!/usr/bin/python
import yql

DATATABLES_URL = 'store://datatables.org/alltableswithkeys'
HISTORICAL_URL = 'http://ichart.finance.yahoo.com/table.csv?s='

yql_object = yql.Public()

#for current quotes
query = 'select * from yahoo.finance.quotes where symbol="FB"'
result = yql_object.execute(query,env=DATATABLES_URL)

#for historical data
symbol = 'FB'
query2 = 'select * from csv where url=\'%s\' and columns=\"Date,Open,High,Low,Close,Volume,AdjClose\"'% (HISTORICAL_URL + symbol)
result2 = yql_object.execute(query2,env=DATATABLES_URL)
#print (result2.raw)
#print type(result2.raw)
print result2.pformat_raw()

#def 
