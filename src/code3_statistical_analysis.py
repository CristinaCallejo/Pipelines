import os
import sys
import pandas as pd

dir_incoming= "./data_processed/"
st = "v2regional_sp_2021_03_05.csv"
st2 = "v2charts.csv"

#dfspot = import_csv(dir_,st1)
#dfsp = dfspot[:5]
#dfs = dfsp[["song", "artist"]]

def import_csv(dir_incoming,st):
    print("Initializing process for: ", st, "from: ", dir_incoming)
    dataframe = pd.read_csv(dir_incoming + st)
    dataframe_slice = dataframe[:5]
    dataf = dataframe_slice.copy()
    #dataf.drop (dropping_lst, axis = 1, inplace = True)
    print("Step 1 of 1: import, SUCCESSFULL")
    print("Ended process: imported ",st)
    return dataf
    
#import_csv_and_prep (dir_, st2,dropping_lst)
#dataf = import_csv_and_prep (dir_, st,dropping_lst)

