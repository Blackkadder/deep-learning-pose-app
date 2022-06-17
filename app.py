# libraries
import streamlit as st
import seaborn as sns

# page config
st.set_page_config(page_icon="📈", page_title="App", layout = 'wide')

# load sample dataset
iris = sns.load_dataset('iris')


# Heading
st.markdown('# HELLO WOrLD!')

# body
st.dataframe(iris)


