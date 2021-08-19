import streamlit as st
import numpy as np
import pandas as pd

# Write a Text
st.title('Welcome to the MVP')

# Dataframes
# st.write("Here is the first table")
# st.write(pd.DataFrame({'first_col':[1,2,3,4,5],'second_col':[6,7,8,9,10]}))

# Magic commands: On console if we simply type out a variable it gets printed; here also it gets published w/o write()

df = pd.DataFrame({'first_col':[1,2,3,4,5],'second_col':[6,7,8,9,10]})
df

# Simple Line chart
st.line_chart(df)

# Widgets bring in the much needed interactivity

# checkbox
st.checkbox('Select Me')

# dropdown
option = st.selectbox(
	'Which number you select?',df['first_col'])

'you selected :', option

# Layouts

# sidebar
option = st.sidebar.selectbox('Im a sidebar', df['first_col'])

# Layout widgets side by side
left_col, right_col = st.columns(2)
pressed = left_col.button('Press Me')

if pressed:
	right_col.write("Great")

# Expander View
expander = st.expander("FAQ")
expander.write("Write your text")

# Progress Bars
import time

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(10):
	latest_iteration.text(f'Iteration {i+1}')
	bar.progress(i + 1)
	time.sleep(0.1)
	
