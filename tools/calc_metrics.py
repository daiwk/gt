#!/usr/bin/env python
# -*- coding: gbk -*-
########################################################################
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: calc_metrics.py
Author: daiwenkai(daiwenkai@baidu.com)
Date: 2017/07/06 23:36:22
"""

import numpy as np
from sklearn.metrics import roc_curve
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import auc


def generate_demo_data(class_num=2):
    """
    given class_num, generate demo data in np.array format
    """
    if class_num == 2:
        g_threshold = 0.34 # just test
        labels_true = np.array([1, 1, 2, 2])
        labels_pred_prob = np.array([0.1, 0.4, 0.35, 0.8])

        labels_pred = np.array([1 if i > g_threshold else 2 for i in labels_pred_prob])
    else:
        labels_true = np.array([1, 1, 2, 3, 2, 3])
        labels_pred_prob = np.array([0.1, 0.4, 0.35, 0.8, 0.7, 0.33])

        labels_pred = np.array([1, 2, 3, 2, 2, 1])
        
    return labels_true, labels_pred_prob, labels_pred


def get_auc(labels_true, labels_pred_prob, pos_label):
    """
    Args:
        labels_true
        labels_pred_prob
        pos_label: Label considered as positive and others are considered negative.
    Returns:
        auc

    """
    fpr, tpr, thresholds = roc_curve(labels_true, labels_pred_prob, pos_label=pos_label)
    print "fpr", fpr
    print "tpr", tpr
    print "thresholds", thresholds

    return auc(fpr, tpr)


def get_recall(labels_true, labels_pred, average_type):
    """
    Args:
        labels_true
        labels_pred
        average_type:
            + micro: Calculate metrics globally by counting the total true positives, false negatives and false positives.
            + macro: Calculate metrics for each label, and find their unweighted mean. This does not take label imbalance into account.
            + weighted: Calculate metrics for each label, and find their average, weighted by support (the number of true instances for each label). This alters 'macro' to account for label imbalance; it can result in an F-score that is not between precision and recall.
            + samples: Calculate metrics for each instance, and find their average (only meaningful for multilabel classification where this differs from accuracy_score).
            + None: the scores for each class are returned. 
    Returns:
        recall
    """
    return recall_score(labels_true, labels_pred, average=average_type)


def get_precision(labels_true, labels_pred, average_type):
    """
    Args:
        labels_true
        labels_pred
        average_type:
            + micro: Calculate metrics globally by counting the total true positives, false negatives and false positives.
            + macro: Calculate metrics for each label, and find their unweighted mean. This does not take label imbalance into account.
            + weighted: Calculate metrics for each label, and find their average, weighted by support (the number of true instances for each label). This alters 'macro' to account for label imbalance; it can result in an F-score that is not between precision and precision.
            + samples: Calculate metrics for each instance, and find their average (only meaningful for multilabel classification where this differs from accuracy_score).
            + None: the scores for each class are returned. 
    Returns:
        precision
    """
    return precision_score(labels_true, labels_pred, average=average_type)


if __name__ == "__main__":
    class_num = 3
    labels_true, labels_pred_prob, labels_pred = generate_demo_data(class_num) 
    average_type = "micro"
    print get_recall(labels_true, labels_pred, average_type)
    print get_precision(labels_true, labels_pred, average_type)

    average_type = None
    print get_recall(labels_true, labels_pred, average_type)
    print get_precision(labels_true, labels_pred, average_type)

    pos_label=1
    print get_auc(labels_true, labels_pred_prob, pos_label)
