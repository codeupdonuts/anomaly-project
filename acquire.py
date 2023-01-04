import numpy as np
import pandas as pd
import env
import datetime


###############################################################
  ##############       Primary Function       ##############
#######  slices txt file and returns logs in dataframe  #######
###############################################################
def acquire_curriculum_data():
    '''This function gets curriculum data from the local repo, which is stored
    as a .txt file'''
    #Get the data from text file on local repo
    df = pd.read_table("anonymized-curriculum-access.txt", sep = '\s', header = None, 
                   names = ['date', 'time', 'page', 'id', 'cohort', 'ip'])
    df.date = pd.to_datetime(df.date + ' ' + df.time)
    df = df.drop(columns=['time'])
    df = df.set_index(df['date'])
    df = df.drop(columns=['date'])               
    return df



  ######################################################
####### formats dataframe for exploring curriculum #######
  ######################################################

def curriculum_dataframe():
    '''
    This function takes in the 'anonymized-curriculum-access' dataframe and returns
    a dataframe with unique names for pages which were accessed on the server
    
    '''
    df = acquire_curriculum_data()
    endpoint = df['page'].unique()
    curriculum_df = pd.DataFrame(endpoint)
    curriculum_df.rename(columns={0: 'pages'}, inplace = True)

    return curriculum_df 
  

###########-----------_Acquire from SQL with additional features---------####

def acquire_cohort_logs(user=env.user, password=env.password, host=env.host):
    '''
    This function queries the Codeup MySQL curriculum_logs database and returns a dataframe
    '''
    url = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/curriculum_logs'
    query = '''
    SELECT date, path as endpoint, user_id, cohort_id, name, start_date, end_date, ip as source_ip, program_id
        FROM logs l
        LEFT JOIN cohorts c ON l.cohort_id = c.id;
    '''
    df = pd.read_sql(query, url)
    #Save file to csv
    df.to_csv('cohort_logs.csv')
    return df
  
  ##########------------Clean the above df using date time and mapping-------#####
  
def clean_cohort_logs(df):
    #Get csv from file
    df = pd.read_csv('cohort_logs.csv', index_col=[0])
    #Changing date, start and end dates to datetime fields
    df["date"]= pd.to_datetime(df["date"])
    df["start_date"]= pd.to_datetime(df["start_date"])
    df["end_date"]= pd.to_datetime(df["end_date"])
    #Setting index as date time
    #Set datetime index
    df = df.set_index(df.date)
    #Creating new column for program length
    df['program_length'] = df.end_date - df.start_date
    #Create column with program name
    #Change data types as needed
    df["program_id"]= df["program_id"].astype(str)
    #Copying these values to a new column program name
    df['program_name'] = df['program_id']
    #Mapping the real names of the program
    df["program_name"] = df["program_name"].map({'1.0':'full stack PHP','2.0':'full stack Java','3.0':'data science','4.0':'front end'})
    
    return df