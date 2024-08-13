'''
PART 1: PRE-PROCESSING
- Tailor the code scaffolding below to load and process the data
- Write the functions below
    - Further info and hints are provided in the docstrings
    - These should return values when called by the main.py
'''

import pandas as pd

def load_data():
    '''
    Load data from CSV files
    
    Returns:
        model_pred_df (pd.DataFrame): DataFrame containing model predictions
        genres_df (pd.DataFrame): DataFrame containing genre information
    '''
    # Your code here
    model_pred_df = pd.read_csv('data/prediction_model_03.csv')
    #print (model_pred_df.head(10))

    genres_df = pd.read_csv('data/genres.csv')
    #print (model_pred_df.head(10))

    return (model_pred_df, genres_df)

def process_data(model_pred_df, genres_df):
    '''
    Process data to get genre lists and count dictionaries
    
    Returns:
        genre_list (list): List of unique genres
        genre_true_counts (dict): Dictionary of true genre counts
        genre_tp_counts (dict): Dictionary of true positive genre counts
        genre_fp_counts (dict): Dictionary of false positive genre counts
    '''
    # Your code here

    genre_true_counts = {}
    genre_tp_counts = {}
    genre_fp_counts = {}

    genre_list = genres_df['genre'].tolist()
    for r in genre_list:
        genre_true_counts[r]=0
        genre_tp_counts[r]=0
        genre_fp_counts[r]=0

    #print (model_pred_df.head(10))
    actualGs= model_pred_df['actual genres']
    #print(actualGs)

    for r in actualGs:
        #print(r)
        for i in eval(r):
            #print(i)
            genre_true_counts[i] = genre_true_counts.get(i,0) +1

    positiveDF = model_pred_df[model_pred_df['correct?'] == 1]
    #print(positiveDF.head(10))

    for p in positiveDF['predicted']:
        genre_tp_counts[p] = genre_tp_counts.get(p,0) +1

    falseDF = model_pred_df[model_pred_df['correct?'] == 0]
    #print(positiveDF.head(10))

    for f in positiveDF['predicted']:
        genre_fp_counts[f] = genre_fp_counts.get(f,0) +1

    #for row in model_pred_df:
    #    if model_pred_df['correct?'] == 1 :
    #        genre_tp_counts[row['predicted']] = genre_tp_counts.get(row['predicted'],0) +1
    #    else:
    #        genre_fp_counts[row['predicted']] = genre_fp_counts.get(row['predicted'],0) +1

    #print(genre_true_counts)
    #print(genre_tp_counts)
    #print(genre_fp_counts)
    #print(genres_list)

    return genre_list, genre_true_counts, genre_tp_counts, genre_fp_counts