import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
#checking for the right input for city
    while True:
        try:
            city = str(input('You want to see data for Chicago, New York City or Washington?  ')).lower()
            if city == 'chicago' :
                print('Your city of choice is {}'.format(city).title())
                break
            elif city == 'new york city':
                print('Your city of choice is {}'.format(city).title())
                break
            elif city == 'washington':
                print('Your city of choice is {}'.format(city).title())
                break
            else:
                print('That is not one of the cities you can explore')
        except:
            print('That is not one of the cities you can explore')
#checking for the right input for month

    while True:
        try:
            month = str(input('You want to filter by a specific month or see data for all months?  '))
            if month == 'january':
                print('You chose to filter by {}'.format(month).title())
                break
            elif month == 'february':
                print('You chose to filter by {}'.format(month).title())
                break
            elif month == 'march':
                print('You chose to filter by {}'.format(month).title())
                break
            elif month == 'april':
                print('You chose to filter by {}'.format(month).title())
                break
            elif month == 'may':
                print('You chose to filter by {}'.format(month).title())
                break
            elif month == 'june':
                print('You chose to filter by {}'.format(month).title())
                break
            elif month == 'all':
                print('You chose to not filter by any month')
                break
            else:
                print('That is not a valid month that you can filter by')
        except:
            print('That is not a valid month that you can filter by')
#checking for the right input for day

    while True:
        try:
            day = str(input('You want to filter by day or see data for all days?  '))
            if day == 'monday':
                print('You chose to filter by {}'.format(day).title())
                break
            elif day == 'tuesday':
                print('You chose to filter by {}'.format(day).title())
                break
            elif day == 'wednesday':
                print('You chose to filter by {}'.format(day).title())
                break
            elif day == 'thursday':
                print('You chose to filter by {}'.format(day).title())
                break
            elif day == 'friday':
                print('You chose to filter by {}'.format(day).title())
                break
            elif day == 'saturday':
                print('You chose to filter by {}'.format(day).title())
                break
            elif day == 'sunday':
                print('You chose to filter by {}'.format(day).title())
                break
            elif day == 'all':
                print('You chose to not filter by any day')
                break
            else:
                print('That is not a valid day that you can filter by')
        except:
            print('That is not a valid day you can filter by')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.weekday_name


    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    popular_month = str(df['month'].value_counts().idxmax())
    datetime_month = datetime.datetime.strptime(popular_month, '%m')
    popular_month = datetime_month.strftime('%B')
    print('The most popular month is {}'.format(popular_month))

    popular_day = df['day_of_week'].value_counts().idxmax()
    print('\nThe most popular day is {}'.format(popular_day))

    df['hour'] = pd.DatetimeIndex(df['Start Time']).hour
    popular_hour = df['hour'].value_counts().idxmax()
    print('\nThe most popular hour is {}:00'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    start_station = df['Start Station'].value_counts().idxmax()
    print('The most common start station is {}'.format(start_station))

    end_station = df['End Station'].value_counts().idxmax()
    print('\nThe most common end station is {}'.format(end_station))

    trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('\nThe most common trip is from {} to {}'.format(trip[0], trip[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_time = df['Trip Duration'].sum().sum()
    print('The total travel time is {} seconds or {} hours'.format(total_time, round(total_time / 3600, 2)))

    mean_time = df['Trip Duration'].mean()
    print('\nThe mean travel time is {} seconds or {} hours'.format(mean_time, round(mean_time / 3600, 2)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    while True:
        try:
            user_types = df['User Type'].value_counts()
            print('There are {} that are characterized as customers and {} that are characterized as subscribers'.format(user_types['Customer'], user_types['Subscriber']))
            break
        except:
            print('There is no user type data for this city')
            break

    while True:
        try:
            gender_counts = df['Gender'].value_counts()
            print('\nThere are {} male and {} female customers in our clientele'.format(gender_counts['Male'], gender_counts['Female']))
            break
        except:
            print('\nThere is no gender data for this city')
            break


    while True:
        try:
            recent_year = df['Birth Year'].max()
            earliest_year = df['Birth Year'].min()
            common_year = df['Birth Year'].value_counts().idxmax()
            print('\nThe most common birth year of the customers is {} with {} being the most recent and {} being the earliest birth year'.
                  format(int(common_year), int(recent_year),int(earliest_year)))
            break
        except:
            print('\nThere is no birth year data for this city')
            break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
