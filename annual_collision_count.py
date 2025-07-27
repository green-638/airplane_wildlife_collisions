import pandas as pd

def annual_collision_count(df, arpts, start_year=1990, end_year=2024):
    ''' creates pandas dataframe with incident counts for selected items
    within selected timeframe
    
    Args:
        df (dataframe): the main dataframe
        arpts (list of str): list of airports
        start_year (int): starting year of timeframe
        end_year (int): ending year of timeframe
        
    Returns:
        pandas dataframe: contains data for species, year, incident count
    '''
    # main dataframe
    dfs = []

    for year in range(start_year, end_year+1):
        current_year = df[(df['AIRPORT'].isin(arpts)) &
                            (df['INCIDENT_YEAR'] == year)]
        total_count = len(current_year)
            
        # insert current year's data into dataframe
        current_data = pd.DataFrame({'Year': [year],
                                'Total Count': [total_count]})
        
        # concat data to main dataframe
        dfs.append(current_data)
   
    combined_df = pd.concat(dfs, ignore_index=True)
    return combined_df