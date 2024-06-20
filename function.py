import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path_csv = 'data/SEATTLE TACOMA AIRPORT.csv'
df = pd.read_csv(file_path_csv)

df['DATE'] = pd.to_datetime(df['DATE'], format='%Y-%m')

def plot_monthly_avg_wind_speed(dataframe, year):
    monthly_avg_wind = dataframe.groupby(dataframe['DATE'].dt.to_period('M'))['AWND'].mean()
    plt.figure(figsize=(12, 6))
    monthly_avg_wind.plot(kind='line')
    plt.title(f'{year} Monthly Average Wind Speed')
    plt.xlabel('Month')
    plt.ylabel('Average Wind Speed (mph)')
    plt.grid(True)
    return plt

def plot_precipitation_days_distribution(dataframe, year):
    monthly_precip_days = dataframe.groupby(dataframe['DATE'].dt.to_period('M'))[['DP01', 'DP10']].sum()
    monthly_precip_days.index = monthly_precip_days.index.strftime('%B')
    ax = monthly_precip_days.plot(kind='bar', stacked=True, figsize=(12, 6))
    plt.title(f'{year} Monthly Distribution of Precipitation Days')
    plt.xlabel('Month')
    plt.ylabel('Number of Days')
    plt.legend(['Days with >0.1 inch Precipitation', 'Days with >1.0 inch Precipitation'])
    plt.grid(True)
    ax.set_xticklabels(monthly_precip_days.index, rotation=0, ha='right')
    return plt

def plot_temperature_heatmap(dataframe, year):
    dataframe['Month'] = dataframe['DATE'].dt.to_period('M')
    temp_pivot = dataframe.pivot_table(index='Month', values=['TMAX', 'TMIN'], aggfunc='mean').reset_index()
    temp_pivot['Month'] = temp_pivot['Month'].astype(str)
    temp_pivot = temp_pivot.set_index('Month')

    plt.figure(figsize=(12, 6))
    sns.heatmap(temp_pivot, annot=True, cmap='coolwarm', cbar=True)
    plt.title(f'{year} Temperature Distribution Heatmap by Month')
    plt.xlabel('Month')
    plt.ylabel('Temperature (F)')
    return plt
