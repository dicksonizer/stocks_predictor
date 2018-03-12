import urllib.request
import os
import time

path = "/Users/Dickson/Desktop/MachineLearning/intraQuarter"
forward_path = "/Users/Dickson/Desktop/MachineLearning/forward_json"

def Check_Yahoo():
		statspath = path+'/_KeyStats'
		stock_list = sorted([x[0] for x in os.walk(statspath)])

		## Added a counter to call out how many files we've already added
		counter = 0
		for e in stock_list[1:]:

			try:
				e = e.replace("/Users/Dickson/Desktop/MachineLearning/intraQuarter/_KeyStats/","")
				## UPDATED URL 2017
				link = "https://query2.finance.yahoo.com/v10/finance/quoteSummary/"+e.upper()+"?modules=assetProfile,financialData,defaultKeyStatistics,calendarEvents,incomeStatementHistory,cashflowStatementHistory,balanceSheetHistory"
				resp = urllib.request.urlopen(link).read()
				save = forward_path+'/'+str(e)+".json"
				store = open(save,"w")
				store.write(str(resp))
				store.close()

				# Check which ones failed in console
				counter +=1
				print("Stored "+ e +".json")
				print("We now have "+str(counter)+" JSON files in the directory.")


			except Exception as e:
				print(str(e))
				

Check_Yahoo()