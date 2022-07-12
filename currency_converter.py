# In order for the program to get real-time exchange rate, I used this link: https://api.exchangerate-api.com/v4/latest/USD
# The link is in JSON format where:
#   Base - USD:     Our base currency is in USD where when we convert to any currency we first convert it to USD then to whatever currency we wish to do
#   Date and time:  The last updated date and time of the rates
#   Rates:          The exchange rate of currencies with the USD base currency

# Importing the necessary libraries
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
