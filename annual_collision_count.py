import pandas as pd

def annual_collision_count(df, arpts, start_year=1990, end_year=2024):
    ''' creates pandas dataframe with incident counts for selected items
    within selected timeframe
    
    Args:
        df (dataframe): the main dataframe
        arpts (list of str): airports to select from dataframe
        start_year (int): starting year of timeframe
        end_year (int): ending year of timeframe
        
    Returns:
        pandas dataframe: contains data for species, year, incident count
    '''
    # list of dataframes
    dataframes = []

    for year in range(start_year, end_year+1):
        # select rows with matching airport and year
        current_year = df[(df['AIRPORT'].isin(arpts)) &
                            (df['INCIDENT_YEAR'] == year)]
        
        # annual count
        total_count = len(current_year)
            
        # create dataframe for current year's data
        current_data = pd.DataFrame({'Year': [year],
                                'Total Count': [total_count]})
        
        dataframes.append(current_data)
        
    # combine all annual counts into single dataframe
    combined_df = pd.concat(dataframes, ignore_index=True)
    return combined_df