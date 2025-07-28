import pandas as pd

def load_data():
    ''' loads dataset into dataframe
    
    Returns:
        dataframe: contains incident year and species name
    '''
    df = pd.read_csv('Public.csv',
                     dtype={'AIRPORT_LATITUDE': str,
                            'AIRPORT_LONGITUDE': str,
                            'FLT': str,
                            'AMO': str,
                            'BIRD_BAND_NUMBER': str},
                     na_values=['UNKNOWN'])
    
    select_columns = ['INCIDENT_YEAR', 'INCIDENT_MONTH', 'AIRPORT', 'SPECIES',
                      'SKY', 'TIME_OF_DAY', 'PHASE_OF_FLIGHT']
    
    # create dataframe with selected columns
    df = pd.DataFrame(data=df, columns=select_columns)
    # drop rows with N/A values
    df = df.dropna(thresh=8)
    df = df.reset_index(drop=True)
    
    return df
