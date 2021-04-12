import numpy as np
import pandas as pd


def import_csv_and_clean_and_lowercase_and_export(dir_incoming,dir_outgoing,st,dropping_lst,renamed_lst,lowering_lst):    
    dataframe = pd.read_csv (dir_incoming + st)
    dataframe_slice = dataframe[:100]
    dataf = dataframe_slice.copy()
    dataf.drop (dropping_lst, axis = 1, inplace = True)
    dataf.reset_index  (drop = True, inplace = True)
    dataf.columns = renamed_lst
    dataf = dataf.apply(lambda x: x.str.lower() if x.name in lowering_lst else x)
    print("Success: import, cleaning, lowercase! Showing first 5 rows for your reference: ", dataf.head(5))
    dataf.to_csv(dir_outgoing + "v1" + st, index = False)
    if True:
        print('Success: export as new .csv. Now importing first 5 rows from new file to check flow and format: ')
        check_exported_file = pd.read_csv(dir_outgoing + "v1" + st , nrows = 5)
        if True:
            print(check_exported_file)
            print('Success! File exported correctly to: ', dir_outgoing + "v1" + st)
        else:
            print('NOT succesfull, cannot show first rows of .csv, check format')
