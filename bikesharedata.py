import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    # Lists used for printing choices.
    city_choices = ['Chicago', 'New York City', 'Washington']
    month_choices = ['January', 'February', 'March', 'April', 'May', 'June', 'All']
    day_choices = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All']

    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
        # retrieves the city to load.
        print("city - name of the city to analyze :\n")
        print(city_choices)
        city = input("Selection :").title()
        if city not in city_choices:
            print('please select from the available options: \n', city_choices)
            continue
        else:
            break

    while True:
        # retrieves the month to filter by.
        print('month - name of the month to filter by, or "all" to apply no month filter?')
        print(month_choices)
        month = input("Selection  :").title()
        if month not in month_choices:
            print('please select from the available options: \n', month_choices)
            continue
        else:
            break

    while True:
        # retieves the day to filter by.
        print('day - name of the day of week to filter by, or "all" to apply no day filter?')
        print(day_choices)
        day = input("Selection  :").title()
        if day not in day_choices:
            print('Please choose from the available options: \n', day_choices)
            continue
        else:
            break

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

    # applies the city input to read the cvs file associated.
    print('\nLoading the data... .. .. ..\n')
    time.sleep(2)
    df = pd.read_csv(CITY_DATA[city])

    # extracting from Start Time
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extracting month and day of week from start time
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'All':
        # appy month filter...
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'All':
        # apply day filter...
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\n\nCalculating The Most Frequent Times of Travel... .. .. ..\n\n')
    time.sleep(2)
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('\nMost Common Month:\n', popular_month)
    print('-'*40)

    # display the most common day of week.
    popular_day = df['day_of_week'].mode()[0]
    print('\nMost Common Day:\n', popular_day)
    print('-'*40)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('\nMost Common Hour:\n', popular_hour)
    print('-'*40)

    # calculates the time this process took
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n\nCalculating The Most Popular Stations and Trip... .. .. ..\n\n')
    time.sleep(2)
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print('\nThe most common start station is ---\n ', start_station)
    print('-'*40)

    # display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print('\nThe most common end station is --- \n', end_station)
    print('-'*40)

    # display most frequent combination of start station and end station trip
    combo_station = df.groupby(['Start Station', 'End Station']).count()
    print('\nThe most common station that were usewd in combination were --- \n',
        start_station, ' and ', end_station)
    print('-'*40)

    # calculates the time this process took
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\n\ncalculating statistics on trip duration... .. .. ..\n\n')
    time.sleep(2)
    print('-'*40)
    start_time = time.time()

    # display total travel time
    total_travel = sum(df['Trip Duration'])
    print('\nThe total travel time was ', total_travel/86400, ' Days\n')
    print('-'*40)

    # display mean travel time
    avg_travel = df['Trip Duration'].mean()
    print('\nThe average trip was \n', avg_travel/60, ' Minutes\n')
    print('-'*40)

    # calculates the time this process took
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\n\nCalculating User Stats... .. .. ..\n\n')
    time.sleep(2)
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print('\nUser types --- \n', user_type)
    print('-'*40)

    # Display counts of gender
    try:
        gender_type = df['Gender'].value_counts()
        print('\nThe gender of the users are --- \n', gender_type)
        print('-'*40)
    except KeyError:
        print('\nNo gender data available...\n')
        print('-'*40)

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        print('\nThe oldest user was born in ', earliest_year, '\n')
        print('-'*40)
    except KeyError:
        print('\nNo birth year data available...\n')
        print('-'*40)

    try:
        recent_year = df['Birth Year'].max()
        print('\nThe youngest user was born in ', recent_year, '\n')
        print('-'*40)
    except KeyError:
        print('\nNo data birth year available\n')
        print('-'*40)

    try:
        common_year = df['Birth Year'].value_counts().idxmax()
        print('\nThe average user was born in ', common_year, '\n')
        print('-'*40)
    except KeyError:
        print('\nNo birth year data available\n')
        print('-'*40)

    # calculates the time this process took
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """
    displays the raw data of the csv file 5 lines at a times
    """
    start_loc = 0
    end_loc = 5

    display_data = input('would you like to inspect the raw data? "Yes" or "No":\n').lower()

    if display_data == 'yes':
        while end_loc <= df.shape[0] - 1:
            print(df.iloc[start_loc:end_loc,:])
            start_loc += 5
            end_loc += 5

            end_data = input('Would you like to see more data? continue = "ENTER" Exit = "No" :\n').lower()
            if end_data == 'no':
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break




if __name__ == "__main__":
	main()
