import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

from Home import message
import pandas as pd 
data = pd.read_csv('Car_data.csv', index_col=None)
data.drop(columns='Unnamed: 0', axis=1, inplace=True)
def main():
    
    if st.checkbox('Coefficient de variation'):
        corr = data.corr()
        fig1, ax = plt.subplots(figsize=(10,6))
        sns.heatmap(corr)
        st.pyplot(fig1)
        st.warning(pd.DataFrame(data.corr()["selling_price"]))
    
if __name__ == '__main__':
    main()
    

