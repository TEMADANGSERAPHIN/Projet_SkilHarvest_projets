from sklearn.ensemble import RandomForestRegressor
import streamlit as st 
import pandas as pd
import joblib

model_load = joblib.load(filename="model_RF.plk")
data = pd.read_csv('Car_data.csv', index_col=None)
data.drop(columns="Unnamed: 0", axis=1, inplace=True)

X = data.drop(columns="selling_price")
y = data.selling_price

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=45)

modele = RandomForestRegressor(n_estimators=100, random_state=42)
modele.fit(X_train, y_train)



st.write(X_test)

def main():
    
    # choix  sub bard
    choix = st.sidebar.radio('Predictions Option', ['Test', 'Future'])
    if choix == 'Test':
        y_pred = modele.predict(y_train)
        st.write(y_train)
        
    if choix == 'Future':
        pass
            
        
if __name__ == '__main__':

    main()
