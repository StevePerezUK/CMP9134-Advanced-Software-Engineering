#!/usr/bin/env python3

# Function implementation 
#c_profit_percentage = .23
# c_sales_growth = 1.05

# def forecast_profit_and_sales():
#     l_total_sales = float(input("Please enter the annual projected amount of total sales: "))
#     print("\nPredicted profit = {0:016_.2f}\n".format(round(l_total_sales*c_profit_percentage,2)))
#     print("Sales forecast:\n")
#     l_total_sales_cumlative = l_total_sales  
#     for year in range(10):
#         year += 1
#         l_total_sales_cumlative *= c_sales_growth 
#         print("Year\t{0:02}\tSales = {1:016_.2f}\tProfit = {2:016_.2f}".format(year,round(l_total_sales_cumlative,2),round(l_total_sales_cumlative * c_profit_percentage,2)))

# forecast_profit_and_sales()

# OOP implementation


class ForecastInput(object):

    def __init__(self):
        # Constants
        self.c_years = 10
        self.c_profit_percentage = .23
        self.c_sales_growth = 1.05
        # Variables
        self.annual_sales = float(0)
        self.total_sales = float(0)
        self.cumulative_year_sales = float(0)
        self.current_year_profit = float(0)

    def get_annual_sales(self):
        try:
            self.annual_sales = float(input("Please enter the annual projected amount of total sales: "))
        except ValueError:
            print("Please enter a valid number")
            return 1

class CalcForecast(ForecastInput):

    def forecast(self):
        self.get_annual_sales() 

    def sales_growth(self):
        self.cumulative_year_sales *= self.c_sales_growth

    def annual_profit(self):
        return self.cumulative_year_sales * self.c_profit_percentage
    
    def set_first_year_sales(self):
        self.cumulative_year_sales = self.annual_sales


class ReportForecast(CalcForecast):

    def report(self):
        self.forecast()
        print("\nFirst year predicted profit = {0:016_.2f}\n".format(round(self.annual_sales * self.c_profit_percentage,2)))
        print("Sales forecast:\n")
        self.set_first_year_sales()
        for year in range(self.c_years):
            year += 1
            self.sales_growth()
            print("Year\t{0:02}\tSales = {1:016_.2f}\tProfit = {2:016_.2f}".format(year,round(self.cumulative_year_sales,2),round(self.annual_profit(),2)))


sales_forecast = ReportForecast()
sales_forecast.report()

