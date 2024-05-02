import streamlit as st 

message = 'Bienvenu dans cette nouvelle page'
selected_year = st.selectbox("Année", [])  # Placeholder for future options


def main():
    
    # choix  sub bard
    choix = st.sidebar.radio('Sous Menu', ['Documentaion', 'Description', 'Accueil'])
    if choix == 'Documentaion':
        st.subheader('Voici la documentaion')
        st.write(message)
        st.write('Merci pour votresoutient ici nous vous nontrons comment est developper cette application restreint.')
        
    if choix == 'Description':
        st.subheader('Voici la description')
        st.write('Merci de bien suivre des instruction si pour la bonne utilisation de notr application merci')
        
    elif choix == 'Accueil':
        st.header('PAGE ACCUEIL')
        st.title('Gestion de plusieurs pages streamlit')
        st.write(message)
            
    
if __name__ == '__main__':

    main()