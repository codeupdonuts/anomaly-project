
##------------------------Acquire----------------------##

def acquire_curriculum_data():
    '''This function gets curriculum data from the local repo, which is stored
    as a .txt file'''
    #Get the data from text file on local repo
    df = pd.read_table("anonymized-curriculum-access.txt", sep = '\s', header = None, 
                   names = ['date', 'time', 'page', 'id', 'cohort', 'ip'])
    return df