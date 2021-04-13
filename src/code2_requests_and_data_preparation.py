
import os
import sys
import pandas as pd

dir_ = "./data_processed/"
st = "v1regional_sp_2021_03_05.csv"
st2 = "v1charts.csv"
dropping_lst = ["rank"]

def export_df_to_csv(dataf,st):
    dataf.to_csv(dir_+ "v2" + st[2:], index = False)
    if True:
        print('Step 1 of !: export as new .csv = SUCCESSFULL')
        print("Ended process: exported ", st, "to: v2" + st[2:], "in: ", dir_)    
    else:
        print('NOT succesfull, check format')
    return dataf


'''
import os
import sys
import pandas as pd
import requests
import json

dir_ = "./data_processed/"
st = "v1regional_sp_2021_03_05.csv"
st2 = "v1charts.csv"
dropping_lst = ["rank"]

#dfspot = import_csv(dir_,st1)
#dfsp = dfspot[:5]
#dfs = dfsp[["song", "artist"]]

def import_csv_and_prep (dir_ ,st,dropping_lst):
    print("Initializing process for: ", st, "from: ", dir_)
    dataframe = pd.read_csv(dir_ + st)
    dataframe_slice = dataframe[:5]
    dataf = dataframe_slice.copy()
    dataf.drop (dropping_lst, axis = 1, inplace = True)
    print("Step 1 of 1: import, cleaning = SUCCESSFULL")
    print("Ended process: imported and prepared ",st)
    return dataf


#import_csv_and_prep (dir_, st2,dropping_lst)

dataf = import_csv_and_prep (dir_, st,dropping_lst)

apikey = os.getenv("tok")

def creating_urls(dataf):
    apikey = os.getenv("tok")
    songs = [song for song in list(dataf.song.values)]
    artists = [artist for artist in list(dataf.artist.values)]
    hits_lst = list(map(lambda x, y: [x, y], songs, artists))
    title = [(f"{song}".upper(), f"{artist}".upper()) for i, (song,artist) in enumerate(hits_lst)]
    url = ["https://api.musixmatch.com/ws/1.1/matcher.lyrics.get?format=json&callback=callback&q_track={song}&q_artist={artist}&apikey={apikey}".format(song = song, artist = artist, apikey = apikey) for i,(song,artist) in enumerate(hits_lst)]#format(song = song, artist = artist, apikey = apikey)]

    no_1 = url[0]
    no_2 = url[1]
    no_3 = url[2]
    no_4 = url[3]
    no_5 = url[4]

    print (no_1)

    give_it_to_me = [no_1,no_2,no_3,no_4,no_5]

    for each in give_it_to_me:
        response = requests.get(each)
        res = response.json()
        lyrics = res["message"]["body"]["lyrics"]["lyrics_body"]
        print(title)
        print(lyrics)
    return lyrics

creating_urls(dataf)
'''
