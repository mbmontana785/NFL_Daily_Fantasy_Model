import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import os

def get_current_weekday():
    # Get the current day of the week as a string (e.g., Monday, Tuesday)
    return datetime.today().weekday()

def get_next_sunday(day_of_week):
    today = datetime.today()
    if day_of_week == 0:
        target_date = today - timedelta(days = 1)
    # elif day_of_week == 1:
    #     target_date = today - timedelta(days = 2)
    else:
        days_ahead = 6 - today.weekday()  # Calculate days until Sunday (Sunday is day 6)
        target_date = today + timedelta(days=days_ahead)
    
    # Return the date in the format %Y-%m-%d
    formatted_date = target_date.strftime('%Y-%m-%d')
    
    return formatted_date

def calculate_nfl_week(date):
    # Convert date to datetime object if it's not already
    if isinstance(date, str):
        date = datetime.strptime(date, '%Y-%m-%d')

    start_date = datetime(2024, 9, 8)  

    # Calculate the difference in days
    days_diff = (date - start_date).days

    # Calculate the week number
    week = (days_diff // 7) + 1

    return week

def get_current_year():
    # Use datetime to get the current year
    current_year = datetime.today().year
    return current_year