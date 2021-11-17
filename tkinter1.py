import tkinter as tk
import datetime as dt
import pandas_datareader.data as web
#import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
#import numpy as np

def plot():

    today = dt.datetime.today()
    start = today + dt.timedelta(-90)
    end = today

    fig = Figure(figsize=(5,5), dpi = 100)
    df = web.DataReader("TSLA", "yahoo", start, end)

    stockPrice1 = [26,35,36,37,30,32]
    stockPrice2 = [23,34,43,30,35,43]
    dates=[0,0,0,0,0,0]

    for i in range(6):
        dates[i] = dt.datetime.today() + dt.timedelta(5-i)
        dates[i] = dates[i].strftime("%Y-%m-%d")

    plot1 = fig.add_subplot(212)
    plot1.plot(dates, stockPrice1)
    plot1.plot(dates, stockPrice2)

    plot2 = fig.add_subplot(211)
    plot2.plot(df["Close"])
    #plot1.plot(dates, df["Close"])

    canvas = FigureCanvasTkAgg(fig, master = window)
    canvas.draw()
    canvas.get_tk_widget().pack()

window = tk.Tk()

window.title("TSLA 90 Calender Days")
window.geometry("500x500")

plot_button = tk.Button(master = window, command = plot, height = 2, width = 10, text = "Plot TSLA")
plot_button.pack()

window.mainloop()
