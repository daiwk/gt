#!/usr/bin/env python
# -*- coding: gbk -*-
########################################################################
# 
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: keras_demo.py
Author: daiwenkai(daiwenkai@baidu.com)
    Date: 2016/07/10 13:04:28
"""

import os
import ConfigParser
import logging

from keras.models import Sequential 
from keras.layers import Dense 
from keras.layers import Dropout

from keras.optimizers import SGD

from common_import import BaseKerasSklearnModel as BaseKerasSklearnModel
from common_import import BaseKerasModel as BaseKerasModel

base_path = os.path.dirname(os.path.abspath(__file__)) + "/../"
os.sys.path.append(base_path)
DEFAULT_LOG_FILENAME = base_path + "/log/base_keras_model"
config_path = base_path + '/conf/'
data_path = base_path + '/data/'

def create_model():
    """
    create model
    """
    # Define and Compile 
    model = Sequential()
    model.add(Dense(12, input_dim=8, init='uniform', activation='relu')) 
    model.add(Dense(8, init='uniform', activation='relu'))
    model.add(Dense(1, init='uniform', activation='sigmoid'))
    model.add(Dropout(0.2))

    sgd = SGD(lr=0.1, momentum=0.9, decay=0.0001, nesterov=True) # learning rate schedule
    model.compile(loss='binary_crossentropy', optimizer=sgd, metrics=['accuracy']) # Fit the model
    #model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy']) # Fit the model
    return model
 


if "__main__" == __name__:

    data_file = data_path + 'pima-indians-diabetes.csv'
    lst_x_keys = list(xrange(0, 8))
    lst_y_keys = 8
    delimiter = ','

    ### base
    config_file = config_path + 'demo_base.conf'
    conf = ConfigParser.ConfigParser()
    conf.read(config_file)
    demo_log_file = base_path + "log/" + conf.get("log", "log_name")
    demo_model_path = base_path + "model/" + conf.get("model", "model_path")

    base_inst = BaseKerasModel(data_file, delimiter, lst_x_keys, lst_y_keys, \
            log_filename=demo_log_file, model_path=demo_model_path)
    base_inst.process()

    ## sklearn
    config_file = config_path + 'demo_base_sklearn.conf'
    conf = ConfigParser.ConfigParser()
    conf.read(config_file)
    demo_log_file = base_path + "log/" + conf.get("log", "log_name")
    demo_model_path = base_path + "model/" + conf.get("model", "model_path")

    base_sklearn_inst = BaseKerasSklearnModel(data_file, delimiter, lst_x_keys, lst_y_keys, \
            log_filename=demo_log_file, model_path=demo_model_path, \
            create_model_func=create_model)
    base_sklearn_inst.process()
    exit(0)
