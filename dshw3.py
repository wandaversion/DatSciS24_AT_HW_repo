#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime

url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)

# Data Diagnostics
# print(df.isnull().sum())
# print(df.describe())
# fill missing

df.sort_values(by='hour_beginning', inplace=True)
df[['weather_summary', 'temperature', 'precipitation']] = df[
    ['weather_summary', 'temperature', 'precipitation']].fillna(method='ffill')
df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])
df['weekday'] = df['hour_beginning'].dt.dayofweek
df['hour'] = df['hour_beginning'].dt.hour

# 1
df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])
df['weekday'] = df['hour_beginning'].dt.dayofweek
weekdays_df = df[df['weekday'] < 5]
by_day = weekdays_df.groupby('weekday')['Pedestrians'].sum()
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
counts = [by_day[i] for i in range(5)]

plot_data = pd.DataFrame({
    'Week-day': days,
    'Pedestrian Count': counts
})

sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))
sns.lineplot(data=plot_data, x='Week-day', y='Pedestrian Count', marker='o')
plt.title('Pedestrian Count by Weekday')
plt.xlabel('Day of the Week')
plt.ylabel('Pedestrian Count')
plt.show()

# 2
df_2019weather = df[(df['hour_beginning'].dt.year == 2019) & (df['location'] == 'Brooklyn Bridge')]
cor_dat = df_2019weather[['Pedestrians', 'temperature', 'precipitation']]

correlation_matrix = cor_dat.corr()

# heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Matrix - Temperature vs Precipitation Count')
plt.show()

# 3
time_map = {
        (0, 4): 'Night',
        (5, 11): 'Morning',
        (12, 16): 'Afternoon',
        (17, 19): 'Evening',
        (20, 23): 'Night'
}

def time_daymap(hour):
    for (start, end), value in time_map.items():
        if start <= hour <= end:
            return value
    return "Undefined"

df['time_of_day'] = df['hour'].apply(time_daymap)
order = ['Morning', 'Afternoon', 'Evening', 'Night']

# by time of day
plt.figure(figsize=(10, 6))
sns.countplot(data=df,
              x='time_of_day',
              hue='time_of_day',
              order=['Morning', 'Afternoon', 'Evening', 'Night'],
              palette='coolwarm',
              legend=False)
plt.title('Pedestrian Counts by Time of Day')
plt.xlabel('Time of Day')
plt.ylabel('Count')
plt.tight_layout()
plt.show()
