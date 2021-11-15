import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import pandas_datareader as web
from tkinter import *



today = dt.datetime.now()

start = today + dt.timedelta(-90)
end = dt.datetime.now()

df = web.DataReader('TSLA', 'yahoo', start, end)

plt.plot(df)
plt.show()

print (df)
#