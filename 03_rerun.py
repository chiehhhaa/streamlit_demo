import streamlit as st
import pandas as pd
import numpy as np
from datetime import date, timedelta
import string
import time

# ? Build a function to create random sales data
@st.cache_data
def get_data():
    product_names = ['Widget' + letter for letter in string.ascii_uppercase] 
    # >ascii_uppercase is a string of uppercase letters, we use to create a uppercase product names
    average_daily_sales = np.random.normal(1_000, 300, len(product_names))
    products = dict(zip(product_names, average_daily_sales))
    # > zip is a function that takes two lists and returns a list of tuples

    data = pd.DataFrame({})
    sales_data = np.arange(date(2023, 1, 1), date(2024, 1, 1), timedelta(days=1))
    for product, sales in products.items():
        data[product] = np.random.normal(sales, 300, len(sales_data))
    data.index = sales_data
    data.index = data.index.date
    return data

# ? Build a function to show the daily sales
# ? Create a function to filter the date
@st.fragment
def show_daily_sales(data):
    with st.container(height=100):
        selected_date = st.date_input(
            'Pick a data',
            value=date(2023, 1, 1),
            min_value=date(2023, 1, 1),
            max_value=date(2023, 12, 31),
            key='selected_date',
        )
# > st.date_input() is a widget that allows the user to select a date

    if 'previous_date' not in st.session_state:
        st.session_state.previous_date = selected_date
    # > Check that 'previous_date' is not in st.session_state and create it.
    previous_date = st.session_state.previous_date
    st.session_state.previous_date = selected_date
    is_new_month = selected_date.replace(day=1) != previous_date.replace(day=1)
    if is_new_month:
        st.rerun()
    
    with st.container(height=510):
        st.header(f'Best sellers, {selected_date:%Y/%m/%d}')
        top_ten_products = data.loc[selected_date].sort_values(ascending=False)[0:10]
        cols = st.columns([1, 4])
        cols[0].dataframe(top_ten_products) 
        cols[1].bar_chart(top_ten_products)
    # > Find a way to display the top 10 products in a bar chart

    with st.container(height=510):
        st.header(f'Worst sellers, {selected_date:%Y/%m/%d}')
        bottom_ten_products = data.loc[selected_date].sort_values()[0:10]
        cols = st.columns([1, 4])
        cols[0].dataframe(bottom_ten_products)
        cols[1].bar_chart(bottom_ten_products)
    # > Find a way to display the bottom 10 products in a bar chart

def show_monthly_sales(data):
    selected_date = st.session_state.selected_date
    this_month = selected_date.replace(day=1)
    next_month = (selected_date.replace(day=28) + timedelta(days=4)).replace(day=1)
    # > Use `February` to calculate the number of days in the next month

    st.container(height=100, border=False)

    with st.container(height=510):
        st.header(f'Daily sales for all products, {this_month:%B %Y}')
        monthly_sales = data[(data.index < next_month) & (data.index >= this_month)]
        st.write(monthly_sales)
    with st.container(height=510):
        st.header(f'Monthly sales for all products, {this_month:%B %Y}')
        st.bar_chart(monthly_sales.sum())

data = get_data()
show_daily_sales(data)
show_monthly_sales(data)

