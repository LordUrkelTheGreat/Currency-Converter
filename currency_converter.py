# In order for the program to get real-time exchange rate, I used this link: https://api.exchangerate-api.com/v4/latest/USD
# The link is in JSON format where:
#   Base - USD:     Our base currency is in USD where when we convert to any currency we first convert it to USD then to whatever currency we wish to do
#   Date and time:  The last updated date and time of the rates
#   Rates:          The exchange rate of currencies with the USD base currency

# Importing the necessary libraries
#import pip._vendor.requests as requests
import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk

# Creating a currency converter class which will allow us to get the real-time exchange rate, convert the currency, and then return the converted amount
class realTimeCurrencyConverter():
    # Create class constructor
    def __init__(self, url):
        # requests.get(url) will load the page into the program
        # The .json() will convert that page into a JSON file
        # Finally all of it gets stored it into data
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    # Converts whatever amount of currency inputed to the requested currency
    def convert(self, fromCurrency, toCurrency, amount):
        # Store amount into dummy variable
        initialAmount = amount

        # If fromCurrency is not USD then convert it to USD (our base currency)
        if fromCurrency != 'USD':
            amount = (amount / self.currencies[fromCurrency])

        # Limit the precision to 4 decimal places
        amount = round(amount * self.currencies[toCurrency], 4)

        # Return converted amount
        return amount

# Creating a currency converter UI class
class currencyConverterUI(tk.Tk):
    # Create class constructor
    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title = 'Currency Converter'
        self.currencyConverter = converter

        # Currency converter object is used to convert currencies
        # The code below will create a Frame
        self.geometry("500x200")

        # Title
        self.introLabel = Label(self, text = 'Welcome to the Real Time Currency Convertor', fg = 'blue', relief = tk.RAISED, borderwidth = 3)
        self.introLabel.config(font = ('Courier', 15, 'bold'))

        # 2nd label
        self.dateLabel = Label(self, text = f"1 Indian Rupee equals {self.currencyConverter.convert('INR', 'USD', 1)} USD \n Date: {self.currencyConverter.data['date']}", relief = tk.GROOVE, borderwidth = 5)

        # Label placement
        self.introLabel.place(x = 10, y = 10)
        self.dateLabel.place(x = 130, y = 50)

# Opens GUI for an infinite loop
if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = realTimeCurrencyConverter(url)
    currencyConverterUI(converter)
    mainloop()