import streamlit as st
import datetime as dt
import matplotlib.pyplot as plt
import pandas_datareader as web




st.title("Stock Analysis Assistant")
st.header("Poop")
#st.text_input("Input", value = "")
st.sidebar.title("Options")


option = st.sidebar.selectbox("Tabs", ("Screener" , "Analysis", "Simulator"))
st.header(option)

today = dt.datetime.now()

start = today + dt.timedelta(-90)
end = dt.datetime.now()

df = web.DataReader('TSLA', 'yahoo', start, end)
plt.plot(df['Close'])
st.pyplot(df["Close"])

#if option == "Analysis":
    #st.pyplot(df)