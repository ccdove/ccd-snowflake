import streamlit
import pandas
import requests


streamlit.title('Healthy dinners count')
streamlit.header('🥣 Big Breakfast')
streamlit.text('🥗 Steak & 2 Eggs')
streamlit.text('🐔 Ham mashed Cauliflower and redeye gravity')
streamlit.text('🥑🍞 Full English') 
   
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# add picklist
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), [ 'Avocado', 'Lime' ])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# display data from file
#       streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())


