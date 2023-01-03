import numpy as np
import pandas as pd


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