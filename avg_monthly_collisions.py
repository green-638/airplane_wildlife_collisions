import pandas as pd

def avg_monthly_collisions(df, arpts, start_year=1990,
                           end_year=2024):
    '''creates a dataframe that contains monthly averages for collisions
    
    Args:
        df (dataframe): the main dataframe
       
        start_year (int): starting year of timeframe
        end_year (int): ending year of timeframe
        
    Returns:
        dataframe: contains data for species/airport, incident month, and
            incident count
    '''
    avgs_list = []

    for month in range(1,13):
        filter = df[(df['AIRPORT'].isin(arpts)) &
                (df['INCIDENT_YEAR'] >= start_year) &
                (df['INCIDENT_YEAR'] <= end_year) &
                (df['INCIDENT_MONTH'] == month)]
        
        count = filter.groupby('INCIDENT_YEAR')\
            ['INCIDENT_MONTH'].value_counts()
        # set avg count to zero if zero records
        if len(count.index) == 0:
            count = 0
        else:
            # calculate avg count
            avg = (sum(count.values.tolist()) / (end_year - start_year))
            
        current_avg = pd.DataFrame({'Month': [month],
                                    'Average Count': [avg]})
        
        avgs_list.append(current_avg)
    
    all_avgs = pd.concat(avgs_list, ignore_index=True)
    return all_avgs