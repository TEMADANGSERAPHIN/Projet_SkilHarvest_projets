import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

from Home import message
import pandas as pd 
data = pd.read_csv('Car_Price_Prediction.csv')
data1 = pd.read_csv('Car_data.csv', index_col=None)

def main():
    st.subheader('Raw data')
    st.header('')
    st.write(data.head())
    st.write(data.shape)
   
    st.subheader('Data processing')
    st.write(data1.head())
    st.write(data1.shape)
    
if __name__ == '__main__':
    main()
    

