#pip install pandas
import pandas as pd


def dataframe(table):
    #Loading the dataset
    con_table = table
    
    '''lis = []
    for index, row in resume_data.iterrows():
            my_list =[row[0], row[1]]
            # append the list to the final list
            lis.append(my_list)'''
    tup = tuple(con_table.itertuples(index=False, name=None))

    # Print the list
    return tup
    
def dataframe_1(table):
    #Loading the dataset
    con_table = table
    
    '''lis = []
    for index, row in resume_data.iterrows():
            my_list =[row[0], row[1]]
            # append the list to the final list
            lis.append(my_list)'''
    tup = tuple(con_table.itertuples(index=True, name=None))

    # Print the list
    return tup