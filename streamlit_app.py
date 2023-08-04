import streamlit
import pandas

streamlit.title('Healthy dinners count')
streamlit.header('🥣 Big Breakfast')
streamlit.text('🥗 Steak & 2 Eggs')
streamlit.text('🐔 Ham mashed Cauliflower and redeye gravity')
streamlit.text('🥑🍞 Full English') 
   
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
