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

from keras.datasets import mnist
from keras.utils import np_utils

from keras.models import Sequential 
from keras.layers import Dense 
from keras.layers import Dropout

from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten

from keras.optimizers import SGD

from common_import import BaseKerasSklearnModel as BaseKerasSklearnModel
from common_import import BaseKerasModel as BaseKerasModel

base_path = os.path.dirname(os.path.abspath(__file__)) + "/../"
os.sys.path.append(base_path)
config_path = base_path + '/conf/'
data_path = base_path + '/data/'

def create_cnn_model(num_classes):
    """
    create a cnn model
    """
    # Define and Compile 
    model = Sequential()
    model.add(Convolution2D(32, 3, 3, border_mode='valid', input_shape=(1, 28, 28), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))

    sgd = SGD(lr=0.1, momentum=0.9, decay=0.0001, nesterov=True) # learning rate schedule
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy']) # Fit the model
    #model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy']) # Fit the model
    return model
 


if "__main__" == __name__:

    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    X_train = X_train.reshape(X_train.shape[0], 1, 28, 28) 
    X_test = X_test.reshape(X_test.shape[0], 1, 28, 28)
    classes = set()
    for i in y_train:
        classes.add(i)
    y_train = np_utils.to_categorical(y_train)
    
    y_test = np_utils.to_categorical(y_test)
    
    num_classes = len(classes)
    aa = create_cnn_model(num_classes=num_classes)
    print aa
    
    

    exit(0)

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
