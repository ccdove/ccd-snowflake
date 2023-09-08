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
streamlit.dataframe(fruits_to_show)


# display data from file
#       streamlit.dataframe(my_fruit_list)
# function
def get_fruity_advice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
          #     streamlit.text(fruityvice_response.json())
          # flaytyens json? 
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
     streamlit.error('Please select a fruit to get information')
  else:
    back_from_function = get_fruity_advice_data(fruit_choice)
             # creates a dataframe of flattened data?
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()
   
def get_fruit_load_list():
   with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from fruit_load_list")
        return my_cur.fetchall()

if streamlit.button('Get fruit load list'):
      my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
      my_data_rows = get_fruit_load_list()
      my_cnx.close()
      streamlit.dataframe(my_data_rows)
#  my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")

def insert_a_fruit(add_fruit):
  with my_cnx.cursor() as my_cur:
       my_cur.execute("insert into fruit_load_list values('" + add_fruit + "')")
       return "thanks for adding " + add_fruit

streamlit.header("The fruit list is:")
your_fruit_choice = streamlit.text_input('Would you care to add a fruit')

if streamlit.button('Add fruit to list'):
      my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
      back_from_function = insert_a_fruit(your_fruit_choice)
      my_cnx.close()
