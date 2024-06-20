import streamlit as st
import pandas as pd
from function import plot_monthly_avg_wind_speed, plot_precipitation_days_distribution, plot_temperature_heatmap
import os

##st.title('Global Climate Change Data Visualization')
st.markdown("<h1 style='text-align: center;'>Global Climate Change Data Visualization</h1>", unsafe_allow_html=True)
st.markdown("""
This application provides a comprehensive visualization of global climate change data. 
The goal is to make climate change trends accessible and understandable to a non-technical audience by offering 
interactive visualizations of global temperature changes and precipitation patterns.
""")

data_dir = 'data'
data_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
location_names = [os.path.splitext(f)[0] for f in data_files]

default_location = location_names[0] if location_names else None
default_year = 2023

st.sidebar.header('User Input Features')
selected_location = st.sidebar.selectbox('Select Location', location_names, index=location_names.index(default_location) if default_location else 0)
selected_file = os.path.join(data_dir, selected_location + '.csv')

df = pd.read_csv(selected_file)
df['DATE'] = pd.to_datetime(df['DATE'], format='%Y-%m')

years = list(reversed(range(1948, 2024)))
year_index = years.index(default_year)
year = st.sidebar.selectbox('Select Year', years, index=year_index)

df_year = df[df['DATE'].dt.year == year]

st.header(f'{selected_location} in {year}')

st.subheader('Monthly Average Wind Speed')
st.markdown(f"""
First let's look at the average wind speed for each month in {year}. This line chart shows how the wind speed changes throughout the year. You can see the line going up and down which tells us that wind speeds are higher in some months and lower in others. This helps us understand the windy and calm periods over the year.
""")
st.pyplot(plot_monthly_avg_wind_speed(df_year, year))

st.markdown("***")


st.subheader('Monthly Distribution of Precipitation Days')
st.markdown("""
Next we have a bar chart that shows how many days each month had significant rainfall. The blue bars represent days with more than 0.1 inch of rain and the orange bars represent days with more than 1.0 inch of rain. This chart helps us see which months were rainier and how intense the rainfall was. For example you can see that some months had many rainy days while others had very few.
""")
st.pyplot(plot_precipitation_days_distribution(df_year, year))

st.markdown("***")


st.subheader('Temperature Distribution Heatmap by Month')
st.markdown("""
The third visualization is a heatmap showing the average maximum and minimum temperatures for each month. In this heatmap colors represent temperatures - cooler colors like blue indicate lower temperatures while warmer colors like red indicate higher temperatures. This heatmap helps us quickly see how temperatures vary from month to month and we can easily spot the hottest and coldest months.
""")
st.pyplot(plot_temperature_heatmap(df_year, year))


st.markdown("***")
st.markdown("""
### About Us
If you have any questions or feedback, please contact us at [haoq4@ucla.edu](mailto:haoq4@ucla.edu).
""")


st.markdown("***")
st.markdown("""
### Data Source
The data used in this application is sourced from the National Oceanic and Atmospheric Administration (NOAA).
""")
