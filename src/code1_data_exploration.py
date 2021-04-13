import os
import sys
import pandas as pd

dir_incoming = "./data_inputs/"
dir_outgoing = "./data_processed/"
st = "regional_sp_2021_03_05.csv"
st2 = "charts.csv"
dropping_lst = ["streams","url"]
dropping_lst2 = ["date","last-week","peak-rank","weeks-on-board"]
renamed_lst = ["rank","song","artist"]
lowering_lst = ["song","artist"]

def import_csv_and_clean_and_lowercase_and_export(dir_incoming,dir_outgoing,st,dropping_lst,renamed_lst,lowering_lst):    
    print("Initializing process for: ", st, "from: ", dir_incoming)
    dataframe = pd.read_csv (dir_incoming + st)
    dataframe_slice = dataframe[:100]
    dataf = dataframe_slice.copy()
    dataf.drop (dropping_lst, axis = 1, inplace = True)
    dataf.reset_index  (drop = True, inplace = True)
    dataf.columns = renamed_lst
    dataf = dataf.apply(lambda x: x.str.lower() if x.name in lowering_lst else x)
    print("Step 1 of 2: import, cleaning, lowercase = SUCCESSFULL")
    dataf.to_csv(dir_outgoing + "v1" + st, index = False)
    if True:
        print('Step 2 of 2: export as new .csv = SUCCESSFULL')
        print("Ended process: exported ", st, "to: v1" + st, "in: ", dir_outgoing)    
    else:
        print('NOT succesfull 2 of 2, cannot show first rows of .csv, check format')
    return dataf

datas = import_csv_and_clean_and_lowercase_and_export(
    dir_incoming,
    dir_outgoing,
    st,
    dropping_lst,
    renamed_lst,
    lowering_lst
)

datab = import_csv_and_clean_and_lowercase_and_export(
    dir_incoming,
    dir_outgoing,
    st2,
    dropping_lst2,
    renamed_lst,
    lowering_lst
    )
