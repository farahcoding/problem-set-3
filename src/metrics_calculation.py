'''
PART 2: METRICS CALCULATION
- Tailor the code scaffolding below to calculate various metrics
- Write the functions below
    - Further info and hints are provided in the docstrings
    - These should return values when called by the main.py
'''

import numpy as np
from sklearn.metrics import precision_recall_fscore_support
import pandas as pd

def calculate_metrics(model_pred_df, genre_list, genre_true_counts, genre_tp_counts, genre_fp_counts):
    '''
    Calculate micro and macro metrics
    
    Args:
        model_pred_df (pd.DataFrame): DataFrame containing model predictions
        genre_list (list): List of unique genres
        genre_true_counts (dict): Dictionary of true genre counts
        genre_tp_counts (dict): Dictionary of true positive genre counts
        genre_fp_counts (dict): Dictionary of false positive genre counts
    
    Returns:
        tuple: Micro precision, recall, F1 score
        lists of macro precision, recall, and F1 scores
    
    Hint #1: 
    tp -> true positives
    fp -> false positives
    tn -> true negatives
    fn -> false negatives

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)

    Hint #2: Micro metrics are tuples, macro metrics are lists

    '''

    # Your code here

    tc_g = 0
    tp_g = 0
    fp_g = 0
    fn_g = 0
    
    for g in genre_list:
        tc_g += genre_true_counts.get(g,0)
        tp_g += genre_tp_counts.get(g,0)
        fp_g += genre_fp_counts.get(g,0)
        fn_g += (genre_true_counts.get(g,0) - genre_tp_counts.get(g,0))

    micro_prec = tp_g/(tp_g+fp_g)
    micro_rec = tp_g/(tp_g+fn_g)
    micro_f1 = 2 * ((micro_prec*micro_rec)/(micro_prec+micro_rec))

    #print(micro_prec)
    #print(micro_rec)    

    macro_prec_list = []
    macro_rec_list = []
    macro_f1_list = []

    for g in genre_list:
        tc_g_mac = genre_true_counts.get(g,0)
        tp_g_mac = genre_tp_counts.get(g,0)
        fp_g_mac = genre_fp_counts.get(g,0)
        fn_g_mac = (genre_true_counts.get(g,0) - genre_tp_counts.get(g,0)) 

        macro_prec = tp_g_mac/(tp_g_mac+fp_g_mac)
        macro_prec_list.append(macro_prec)
        macro_rec = tp_g_mac/(tp_g_mac+fn_g_mac)
        macro_rec_list.append(macro_rec)
        macro_f1 = 2 * ((macro_prec*macro_rec)/(macro_prec+macro_rec))
        macro_f1_list.append(macro_f1)


    return micro_prec, micro_rec, micro_f1, macro_prec_list, macro_rec_list, macro_f1_list


    
def calculate_sklearn_metrics(model_pred_df, genre_list):
    '''
    Calculate metrics using sklearn's precision_recall_fscore_support.
    
    Args:
        model_pred_df (pd.DataFrame): DataFrame containing model predictions.
        genre_list (list): List of unique genres.
    
    Returns:
        tuple: Macro precision, recall, F1 score, and micro precision, recall, F1 score.
    
    Hint #1: You'll need these two lists
    pred_rows = []
    true_rows = []
    
    Hint #2: And a little later you'll need these two matrixes for sk-learn
    pred_matrix = pd.DataFrame(pred_rows)
    true_matrix = pd.DataFrame(true_rows)
    '''

    # Your code here
