import pandas as pd

def avg_monthly_collisions(df, arpts, start_year=1990,
                           end_year=2024):
    '''creates a dataframe that contains monthly averages for collisions
    
    Args:
        df (dataframe): the main dataframe
        arpts (list of str): airports to select from dataframe
        start_year (int): starting year of timeframe
        end_year (int): ending year of timeframe
        
    Returns:
        dataframe: contains data for month and average count
    '''
    avgs_list = []

    for month in range(1,13):
        # select rows with matching airport and month within timeframe
        filter = df[(df['AIRPORT'].isin(arpts)) &
                (df['INCIDENT_YEAR'] >= start_year) &
                (df['INCIDENT_YEAR'] <= end_year) &
                (df['INCIDENT_MONTH'] == month)]
        
        # get annual counts for current month
        count = filter.groupby('INCIDENT_YEAR')\
            ['INCIDENT_MONTH'].value_counts()
            
        # set avg count to zero if zero rows
        if len(count.index) == 0:
            count = 0
        else:
            # calculate avg count for current month
            avg = (sum(count.values.tolist()) / (end_year - start_year))
            
        # create dataframe for current month's avg
        current_avg = pd.DataFrame({'Month': [month],
                                    'Average Count': [avg]})
        
        avgs_list.append(current_avg)
        
    # combine all averages into single dataframe
    all_avgs = pd.concat(avgs_list, ignore_index=True)
    return all_avgs