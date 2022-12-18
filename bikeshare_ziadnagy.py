import time
import pandas as pd
import numpy as np

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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city_list=['chicago','new york city','washington']
    city=input(str('please choose your city from chicago,new york city or washington:   ')).lower()
    
    while city not in city_list:
        city=input('non-listed city please choose city from chicago, new york city, washington:   ' ).lower()
        
        
     
    # get user input for month (all, january, february, ... , june)
    month_list=['januar','february','march','april','may','june','all']
    month=input("please choose your month or put all for no filter:   ").lower()
    while month not in month_list:
        month=input('non-listed month please choose your month from january to june:    ').lower()
        
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day_list=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    day=input('please choose your day of week:   ').lower()
    while day not in day_list:
        day=input('wrong day of week please enter your day correctly:    ')
    print('-'*50)
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    common_month=df['month'].mode()[0]
    print('The most common month is: {}'.format(common_month))

    # display the most common day of week
    
    common_day=df['day_of_week'].mode()[0]
    print('The most common day is: {}'.format(common_day))

    # display the most common start hour
    common_start_hour=df['Start Time'].mode()[0]
    print('The most common start hour is: {}'.format(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    
    common_start_station=df['Start Station'].mode()[0]
    print('The most commonly used start station is: {}'.format(common_start_station))
    
    # display most commonly used end station
    
    common_end_station=df['End Station'].mode()[0]
    print('The most commonly used end station is: {}'.format(common_end_station))

    # display most frequent combination of start station and end station trip
    
    df['start_to_end']=df['Start Station']+' '+df['End Station']
    most_start_to_end_station_trip=df['start_to_end'].mode()[0]
    print('The most frequent combination of start station and end station trip is: {}'.format(most_start_to_end_station_trip))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    
    total_travel_time=df['Trip Duration'].sum()
    print('The total travel time is: {}'.format(total_travel_time))

    # display mean travel time
    
    mean_travel_time=df['Trip Duration'].mean()
    print('The mean travel time is: {}'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    
    try:
        print(df['User Type'].value_counts())
    except:
        print('The column is not here')
        
    # Display counts of gender
    
    try:
        print(df['Gender'].value_counts())
    except:
        print('The column is not here')

    # Display earliest, most recent, and most common year of birth
     
    
    try:
        birth_year=df['Birth Year']

        earliest_year = birth_year.min()
        
        print('The most earliest birth year is: {}'.format(earliest_year))
        
        print('The column is not here')
        
        birth_year=df['Birth Year']
        most_recent_birthday=birth_year.max()
        print('The most recent birth year is: {}'.format(most_recent_birthday))
       
        
        most_common_year =birth_year.value_counts().idxmax()
        print("The most common birth year is: {}".format(most_common_year))
    
    except:
        print('This data is not available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)

def display_raw_data(city):
    print('\n Raw data is available to check. \n')
    display_raw =input( 'Do you want to have a look on the raw data? yes or no:  ')
    
    while display_raw == 'yes':
       
        try:
            
            for chunk in pd.read_csv(CITY_DATA[city],chunksize=6):
                print(chunk)
                display_raw = input('\nDo you like to see another 5 rows of the raw data? yes or no: .\n')
               
                if display_raw != 'yes':
                    print('Thank you!')
                    break
            break
        except KeyboardInterrupt:
                        print('Thank You!')
                        





                    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
