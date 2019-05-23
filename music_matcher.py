import os

import IPython.display as ipd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import sklearn as skl
#import sklearn.utils, sklearn.preprocessing, sklearn.decomposition, sklearn.svm
#import librosa
#import librosa.display
import ast

#import utils

METADATA_DIR = "./fma_metadata/"

def load(filepath):
    """
    Based off code from the fma github
    """
    filename = os.path.basename(filepath)
    if "features" in filename:
        return pd.read_csv(filepath, index_col=0, header=[0, 1, 2])
    if "echonest" in filename:
        return pd.read_csv(filepath, index_col=0, header=[0, 1, 2])
    if "genres" in filename:
        return pd.read_csv(filepath, index_col=0)
    if "tracks" in filename:
        tracks = pd.read_csv(filepath, index_col=0, header=[0, 1])

        COLUMNS = [("track", "tags"), ("album", "tags"), ("artist", "tags"),
                   ("track", "genres"), ("track", "genres_all")]
        for column in COLUMNS:
            tracks[column] = tracks[column].map(ast.literal_eval)

        COLUMNS = [("track", "date_created"), ("track", "date_recorded"),
                   ("album", "date_created"), ("album", "date_released"),
                   ("artist", "date_created"), ("artist", "active_year_begin"),
                   ("artist", "active_year_end")]
        for column in COLUMNS:
            tracks[column] = pd.to_datetime(tracks[column])

        SUBSETS = ("small", "medium", "large")
        tracks["set", "subset"] = tracks["set", "subset"].astype(
                "category", categories=SUBSETS, ordered=True)

        COLUMNS = [("track", "genre_top"), ("track", "license"),
                   ("album", "type"), ("album", "information"),
                   ("artist", "bio")]
        for column in COLUMNS:
            tracks[column] = tracks[column].astype("category")

        return tracks

def load_data(composers_to_learn=None):
    tracks = load(METADATA_DIR + "tracks.csv")
    #genres = load(METADATA_DIR + "genres.csv")
    #features = load(METADATA_DIR + "features.csv")
    #echonest = load(METADATA_DIR + "echonest.csv")

    tracks = tracks[tracks["track", "genre_top"] == "Classical"]
    tracks = tracks[tracks["track", "composer"].notnull()]
    composer_dict = {}
    for index, row in tracks.iterrows():
        composer = row["track", "composer"]
        if composers_to_learn:
            for c in composers_to_learn:
                if c in composer:
                    composer = composers_to_learn[composers_to_learn.index(c)]
        if composers_to_learn and composer not in composers_to_learn:
            continue
        if composer not in composer_dict:
            composer_dict[composer] = [row]
        else:
            composer_dict[composer] += [row]

    return composer_dict

def count_data(composer_dict):
    count_dict = {}
    for composer in composer_dict:
        count_dict[composer] = len(composer_dict[composer])
    return count_dict

if __name__=="__main__":
    composers_to_learn = ["Bach", "Haydn"]
    composer_data = load_data()
    count_dict = count_data(composer_data)
    print(count_dict)
