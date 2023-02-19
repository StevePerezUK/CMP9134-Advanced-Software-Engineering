#!/usr/bin/env python3

c_profit_percentage = .23
c_sales_growth = 1.05

def forecast_profit_and_sales():
    l_total_sales = float(input("Please enter the annual projected amount of total sales: "))
    print("\nPredicted profit = {0:016_.2f}\n".format(round(l_total_sales*c_profit_percentage,2)))
    print("Sales forecast:\n")
    l_total_sales_cumlative = l_total_sales  
    for year in range(10):
        year += 1
        l_total_sales_cumlative *= c_sales_growth 
        print("Year\t{0:02}\tSales = {1:016_.2f}\tProfit = {2:016_.2f}".format(year,round(l_total_sales_cumlative,2),round(l_total_sales_cumlative * c_profit_percentage,2)))

forecast_profit_and_sales()