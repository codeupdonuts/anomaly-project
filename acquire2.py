import numpy as np
import pandas as pd
import os

###############################################################
  ##############       TWO Primary Functions       ##############
#######  acquires dataframe, cleans and returns it  #######
   #######  chronological or nonchronological formats  #######
###############################################################


def get_df():
    '''
    This function acquires a dataframe from the given text file,
    cleans it, and then returns it for use
    '''

    df = acquire_curriculum_data()
    df = cleaning(df)

    return df

def chron_df():
    '''
    This function acquires a dataframe from the given text file,
    cleans it, and then returns it for use
    '''

    df = acquire_curriculum_data()
    df = cleaning(df)
    df.date = pd.to_datetime(df.date + ' ' + df.time)
    df = df.drop(columns=['time'])
    df = df.set_index(df['date'])
    df = df.drop(columns=['date'])   

    return df

###############################################################
  ##############       Acquisition Functions       ##############
###############################################################

####### acquires and formats dataframe from txt file  #######


####### acquires and formats dataframe from txt file  #######
def acquire_curriculum_data():
    '''This function gets curriculum data from the local repo, which is stored
    as a .txt file'''

    
    df = pd.read_csv('curriculum-access-log.csv') 
    
        #Get the data from text file on local repo
        #df = pd.read_table("anonymized-curriculum-access.txt", sep = '\s', header = None, 
        #            names = ['date', 'time', 'page', 'id', 'cohort', 'ip'])
                
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




#######################################################
#######        calls wrangling functions        #######
#######################################################

def cleaning(df):
    df = fix_programs(df)

    return df


##################################################
#######         wrangling functions        #######
##################################################

#######       program column fix       ########
def fix_programs(df):

    map_dict = {
        1.0: 'php',
        2.0: 'java',
        3.0: 'data_science',
        4.0: 'front-end'
        }
    df['program_id'] = df['program_id'].map(map_dict)
    df.rename(columns={'program_id': 'program'}, inplace = True)

    return df



