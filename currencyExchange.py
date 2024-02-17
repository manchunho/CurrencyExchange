from tkinter import messagebox, ttk
import tkinter as tk
import requests

def output():
    
    # API request to retrive exchange rate data in json format
    url = 'https://api.hkma.gov.hk/public/market-data-and-statistics/monthly-statistical-bulletin/er-ir/er-eeri-daily?offset=0'
    response = requests.get(url)
    data = response.json()
    
    # Input currency
    exchangeRate_In = data['result']['records'][0].get(input_currency.get().lower())
    
    # Output currency
    exchangeRate_Out = data['result']['records'][0].get(output_currency.get().lower())
    
    if (exchangeRate_In is None):
        exchangeRate_In = 1
    if (exchangeRate_Out is None):
        exchangeRate_Out = 1
    
    # Calculate exchange rate
    result = float(input_cost.get()) * float(exchangeRate_In) / float(exchangeRate_Out)
    exchangeRateNumlb["text"] = float(exchangeRate_In) / float(exchangeRate_Out)
    output_cost["text"] = result
    
    # latest date
    latestUpdate = data['result']['records'][0]['end_of_day']
    LatestUpdateValuelb["text"] = latestUpdate
    
#Tkinter
win = tk.Tk()
win.title('Currency Exchange')
win.geometry('300x200')
win.resizable(False, False)
win.iconbitmap('')

#Label
InputCostlb = tk.Label(text="Input cost:", fg="black",height=1)
InputCostlb.place(x=0 ,y=0)

InputAmountlb = tk.Label(text="Input amount:",fg="black",height=1)
InputAmountlb.place(x=0 ,y=30)

exchangeRatelb = tk.Label(text="Exchange Rate:",fg="black",height=1)
exchangeRatelb.place(x=0 ,y=60)

exchangeRateNumlb = tk.Label(text="",fg="black",height=1)
exchangeRateNumlb.place(x=100 ,y=60)

Outputlb = tk.Label(text="Output cost:",fg="black",height=1)
Outputlb.place(x=0 ,y=90)

output_cost = tk.Label(text="",fg="black",height=1)
output_cost.place(x=100 ,y=120)

OutputAmountlb = tk.Label(text="Output amount:",fg="black",height=1)
OutputAmountlb.place(x=0 ,y=120)

LatestUpdatelb = tk.Label(text="Latest update:",fg="red",height=1)
LatestUpdatelb.place(x=0 ,y=180)

LatestUpdateValuelb = tk.Label(text="",fg="red",height=1)
LatestUpdateValuelb.place(x=90 ,y=180)

#Entry
input_currency = ttk.Combobox(values=["AUD","BEF","CAD","CHF","CNY","DEM","EUR","FRF","GBP","HKD","IDR","INR","ITL",
                                      "JPY","KRW","MYR","NLG","PHP","SGD","THB","TWD","USD","ZAR"])
input_currency.current(9)
input_currency.place(x=100, y=0)

input_cost = tk.Entry(width=23)
input_cost.insert(0, "1") 
input_cost.place(x=100 ,y=30)

output_currency = ttk.Combobox(values=["AUD","BEF","CAD","CHF","CNY","DEM","EUR","FRF","GBP","HKD","IDR","INR","ITL",
                                       "JPY","KRW","MYR","NLG","PHP","SGD","THB","TWD","USD","ZAR"])
output_currency.current(21)
output_currency.place(x=100, y=90)

#Button
enter_btn = tk.Button(text="Enter",height=1,command=output)
enter_btn.place(x=150 ,y=150)

win.mainloop()
