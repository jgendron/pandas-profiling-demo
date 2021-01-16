# packages for data ETL
import re
import pandas as pd

def column_name_processing(file):
    '''
    A function included only to remove code non-relevant to the demonstration.
    Specifically, it processes the raw text and extract column names.
    
    ***
    Input: A space-delimited file from the UCI ML repository
    Output: returns processed columns names as list
    ***
    '''
    # --- Column Names ---
    # Step 1
    pattern = re.compile(r'(\d+)(:)(.+)') #find three regex groups to positively id a data dictionary item

    # Step 2
    col_text = []

    for line in file:
        string = line.decode("utf-8") #convert from byte to string
        if re.search(pattern, string):
            var_name = re.search(pattern, string)[3].strip().lower()
            var_name = var_name.replace('?','')
            col_text.append(var_name.replace(' ','_'))

    # Step 3
    col_text.insert(25,'type_of_lesion_2')
    col_text.insert(26,'type_of_lesion_3')
    
    return col_text


def data_file_processing(url, cols):
    '''
    A function included only to remove code non-relevant to the demonstration.
    Specifically, it processes the raw text into a csv file.
    
    ***
    Input: A space-delimited file from the UCI ML repository
    Output: returns processed comma-separated value file
    ***
    '''
    # --- Data ---
    # Step 1
    csv = pd.read_csv(url, 
                       na_values='?',
                       sep='\s+',
                       header = None,
                       names=cols,
                       dtype = {'surgery':'str',
                                'type_of_lesion':'str',
                                'type_of_lesion_2':'str',
                                'type_of_lesion_3':'str',
                                }
                       )
    # Step 2
    csv.drop('cp_data', axis=1, inplace=True)
    
    return csv