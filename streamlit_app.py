import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError



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
def get_fruity_advice_data(this_fruit_choice):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
         #     streamlit.text(fruityvice_response.json())
         # flaytyens json? 
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
     streamlit.error('Please select a fruit to get information')
  else:
    streamlit.header("Fruityvice Fruit Advice!")   
    back_from_function = get_fruity_advice_data(fruit_choice)
             # creates a dataframe of flattened data?
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#  my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit list is:")
streamlit.dataframe(my_data_rows)

your_fruit_choice = streamlit.text_input('Would you care to add a fruit')
