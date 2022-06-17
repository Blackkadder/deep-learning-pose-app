# libraries
import streamlit as st
import seaborn as sns


def main():
    # page config
    st.set_page_config(page_icon="📈", page_title="App", layout = 'wide')

    # load sample dataset
    iris = sns.load_dataset('iris')


    # Heading
    st.markdown('# HELLO WOrLD!')
    st.markdown('**The** quick brown *fox* runs over the lazy dog.')
    st.image('https://c.ndtvimg.com//yoga_625x300_1529482160763.jpg')
    # body
    st.dataframe(iris)


if __name__ == "__main__":
   
    main()


