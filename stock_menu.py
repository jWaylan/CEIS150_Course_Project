#-*- coding: utf-8 -*-
"""
Created on Mon Aug 30 22:57:11 2021

@author: D99003734
"""
from datetime import datetime
from stock_class import Stock, DailyData
#from account_class import  Traditional, Robo
import matplotlib.pyplot as plt
import csv


def add_stock(stock_list):
   option = ""
   while option != "0":
        print("\nAdd Stock -----")
        symbol = input("Enter ticker symbol: ").upper()
        name = input("Enter company name: ")
        shares = float(input("Enter number of shares: "))
        new_stock = Stock(symbol, name, shares)
        stock_list.append(new_stock)
        option = input("Press Enter to add another stock or 0 to stop: ")


# Remove stock and all daily data
def delete_stock(stock_list):
    print("\nDelete Stock -----")
    print("Stock List: [", end="")
    for stock in stock_list:
        print(stock.symbol," ", end="")
    print("]")
    symbol = input("\nEnter stock to be deleted: ").upper()
    found = False
    i = 0
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            stock_list.pop(i)
        i += 1
    if found == True:
        print("Deleted",symbol)
    else:
        print("Symbol not found")
    _=input("\nPress enter to continue...")
    
    
# List stocks being tracked
def list_stocks(stock_list):
    print("\nStock List -----")
    print("SYMBOL\t\tNAME\t\tSHARES")
    print("=======================================")
    for stock in stock_list:
        print(stock.symbol," " * (14-len(stock.symbol)),stock.name," " * (14-len(stock.name)),stock.shares)
    print()
    _=input("\nPress enter to continue...")
    
# Add Daily Stock Data
def add_stock_data(stock_list):
    print("\nAdd Daily Stock Data ----")
    print("Stock List: [",end="")
    for stock in stock_list:
        print(stock.symbol," ",end="")
    print("]")
    symbol = input("\nWhich stock do you want to use?: ").upper()
    found = False
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            current_stock = stock
    if found == True:
        print("Ready to add data for: ",symbol)
        print("Enter Data Separated by Commas - Do Not use Spaces")
        print("Enter a Blank Line to Quit")
        print("Enter Date,Price,Volume")
        print("Example: 8/28/20,47.85,10550")
        data = input("\nEnter Date,Price,Volume: ")
        while data != "":
            date, price, volume = data.split(",")
            daily_data = DailyData(date,float(price),float(volume))
          
            current_stock.add_data(daily_data)
            data = input("Enter Date,Price,Volume: ")
        print("\nDate Entry Complete")
    else:
        print("Symbol Not Found ***")
    _ = input("Press Enter to Continue ***")


    
def investment_type(stock_list):
    print("This method is under construction")

# Function to create stock chart
def display_stock_chart(stock_list,symbol):
    print("This method is under construction")

# Display Chart
def display_chart(stock_list):
    print("This method is under construction")
  


                
 # Get price and volume history from Yahoo! Finance using CSV import.
def import_stock_csv(stock_list):
    print("This method is under construction")
    
   # Display Report 
def display_report(stock_list):
    print("This method is under construction")
    
def main_menu(stock_list):
    option = ""
    while True:
        print("\nStock Analyzer ---")
        print("\t1 - Add Stock")
        print("\t2 - Delete Stock")
        print("\t3 - List stocks")
        print("\t4 - Add Daily Stock Data (Date, Price, Volume)")
        print("\t5 - Show Chart")
        print("\t6 - Investor Type")
        print("\t7 - Load Data")
        print("\t0 - Exit Program")
        option = input("Enter Menu Option: ")
        if option =="0":
            print("\nGoodbye")
            break
        
        if option == "1":
            add_stock(stock_list)
        elif option == "2":
            delete_stock(stock_list)
        elif option == "3":
            list_stocks(stock_list)
        elif option == "4":
           add_stock_data(stock_list) 
        elif option == "5":
            display_chart(stock_list)
        elif option == "6":
            investment_type(stock_list)
        elif option == "7":
            import_stock_csv(stock_list)
        else:
            
            print("Goodbye")

# Begin program
def main():
    stock_list = []
    main_menu(stock_list)

# Program Starts Here
if __name__ == "__main__":
    # execute only if run as a stand-alone script
    main()