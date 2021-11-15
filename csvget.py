import datetime as dt
import pandas_datareader.data as web
import pandas as pd
import matplotlib.pyplot as plt

today = dt.datetime.today()
start = today + dt.timedelta(-90)
end = today

df = web.DataReader("TSLA", "yahoo", start, end)
df.to_csv("TSLA90DAYS.csv")

plt.plot(df["Close"])
plt.show()