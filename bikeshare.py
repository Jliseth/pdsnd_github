# This project is to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


month_list = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city = ''


    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while city.lower() not in CITY_DATA.keys():
       city = input('Please choose one of 3 cities, Chicago, New York City, or Washington which you like to expplore: \n').lower()
        
       if city not in CITY_DATA.keys():
            print('\nSorry, you can only enter either Chicago, New York, or Washington.  Try again. \n')
            continue
       else:
            break                    
     
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month = ''
    while month.lower() not in month_list:
       month = input('Please select one of months between january and june, or type \'all\' to apply no month filter: \n').lower()
    
       if month not in month_list:
          print('Sorry you have to enter one of months between january and june, or all.  Try again. \n')
          continue
       else:
          break
    
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while day.lower() not in day_list:
       day = input('Please select day of the week, e.g. monday, tuesday, ...sunday, or type \'all\' to view all data: \n').lower()
    
       if day not in day_list:
          print('Please enter day of the week, e.g. monday, tuesday, ...sunday, or all.  Try again. \n')
          continue
       else:
         break


    print('-'*40)
    return city, month, day


# function - load data from csv files
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
    # load data into a dataframe with the specified city
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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


# function - find popular month, day, and hour for bike trip
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month_num = df['month'].mode()[0]
    popular_month = months[popular_month_num -1]
    print('\nThe most common month: ', popular_month.title())

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('\nThe most common day of week: ', popular_day)

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    
    # TO DO: display the most common start hour
    popular_start_hour = df['hour'].mode()[0]
    print('\nThe most common start hour: ', popular_start_hour)

    # print the time taken to process this function
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
# function - find ppopular start and end stations of bike trip
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('\nThe most common used start station: ', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('\nThe most common used end station: ', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['StartToEnd'] = df['Start Station'] + ' To ' + df['End Station']
    popular_combination_station = df['StartToEnd'].mode()[0]
    print('\nThe most frequent combination of start station and end station trip: ', popular_combination_station)
    
    # print the time taken to process this function
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# function - find bike trip duration    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time in seconds
    total_travel_seconds = df['Trip Duration'].sum()
    
    # convert total travel time in days (86400 second in a day)
    total_travel_days  = total_travel_seconds  // 86400
    print('\nTotal travel time is approx. ', total_travel_days, ' days')

    # TO DO: display mean travel time
    average_travel_time = int(df['Trip Duration'].mean())
    print('\nThe average trip took ', average_travel_time, ' seconds')
    
        
    # print the time taken to process this function
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# function - report bikeshare users statistics
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print('\nThese are bikeshare user types and total numbers in each type:  \n', user_type_counts)

    # TO DO: Display counts of gender
    # only Chicago and New York City contain 'Gender' column, hence try clause is implemented
    try:
        gender_counts = df['Gender'].value_counts()
        print('\nHere are bikeshare user numbers in each gender group:  \n', gender_counts)
    except:
       print('\nThere is no gender information in this city bikeshare file.')

    
    # TO DO: Display earliest, most recent, and most common year of birth
    # again, only Chicago and New York City contain 'Birth Year' column, hence try clause is implemented
    try:
        earliest_birth_year = int(df['Birth Year'].min())
        
        latest_birth_year = int(df['Birth Year'].max())
        
        most_common_year = int(df['Birth Year'].mode()[0])
        print(f"\nThe earliest birth year of users is: {earliest_birth_year}\nThe most recent birth year of users is: {latest_birth_year}\nThe most common year of birth is: {most_common_year}")
    except:
       print('\nThere is no birth year information in this city bikeshare file.')

     # print the time taken to process this function
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 

# function - show some rows of data upon user request until user types 'no'
def display_data(df):
    """Ask user whether she wants to see data."""
    view_data = input('Would you like to view 5 rows of individual trip data?  Enter yes or no  \n').lower()

  
    # TO DO:initialize variables
    start_loc = 0
    view_data = True
    
    while (view_data):
        # display 5 rows of data
        print(df.iloc[start_loc:start_loc+5])
        
        # increment by 5 the start location
        start_loc += 5
        
        # Ask user if she wants to see more data
        view_display = input('Do you wish to continue?  Enter yes or no  \n').lower()
        
        if view_display == "no":
            view_data = False
            break
 
       

# function - compile specific information per user request
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
