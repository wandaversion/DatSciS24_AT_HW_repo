#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)
print(df.columns)

# 'hour_beginning' ->  datetime
df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])
df['weekday'] = df['hour_beginning'].dt.dayofweek
weekdays_df = df[df['weekday'] < 5]

# by day of the week
pedestrian_counts_by_day = weekdays_df.groupby('weekday')['Pedestrians'].sum()
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
counts = [pedestrian_counts_by_day[i] for i in range(5)]
plt.figure(figsize=(10, 6))
plt.plot(days_of_week, counts, marker='o')
plt.title('Pedestrian Counts by Weekday')
plt.xlabel('Day of the Week')
plt.ylabel('Total Pedestrian Counts')
plt.grid(True)
plt.show()

# pedestrian counts on Bridge 2019, by weather
bridge_2019 = df[(df['hour_beginning'].dt.year == 2019) & (df['location'] == 'Brooklyn Bridge')]
weather_counts = bridge_2019.groupby('weather_summary')['Pedestrians'].sum().sort_values()

plt.figure(figsize=(12, 8))
weather_counts.plot(kind='bar')
plt.title('Pedestrian Counts by Weather Summary for Brooklyn Bridge in 2019')
plt.xlabel('Weather Summary')
plt.ylabel('Total Pedestrian Counts')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

def categorize_time_of_day(hour):
    if 5 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 17:
        return 'Afternoon'
    elif 17 <= hour < 21:
        return 'Evening'
    else:
        return 'Night'

df['time_of_day'] = df['hour_beginning'].dt.hour.apply(categorize_time_of_day)
time_of_day_counts = df.groupby('time_of_day')['Pedestrians'].sum()

plt.figure(figsize=(10, 6))
time_of_day_counts.reindex(['Morning', 'Afternoon', 'Evening', 'Night']).plot(kind='bar')
plt.title('Pedestrian Activity Patterns Throughout the Day')
plt.xlabel('Time of Day')
plt.ylabel('Total Pedestrian Counts')
plt.tight_layout()
plt.show()
