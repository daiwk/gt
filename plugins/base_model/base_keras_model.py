#!/usr/bin/env python
# -*- coding: gbk -*-
########################################################################
# 
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: base_keras_model.py
Author: daiwenkai(daiwenkai@baidu.com)
    Date: 2016/07/10 13:04:28
"""

import numpy
import logging

from keras.models import Sequential 
from keras.layers import Dense 
from keras.layers import Dropout

from keras.wrappers.scikit_learn import KerasClassifier

from keras.optimizers import SGD

from keras.callbacks import ModelCheckpoint
from keras.callbacks import Callback

import sklearn
from sklearn.cross_validation import StratifiedKFold
from sklearn.cross_validation import cross_val_score

class LossHistory(Callback):
    def on_train_begin(self, logs={}):
        self.losses = []

    def on_batch_end(self, batch, logs={}):
        self.losses.append(logs.get('loss'))


class BaseKerasModel(object):
    """
    base keras model based on keras's model(without sklearn)
    """
    def __init__(self, data_file, delimiter, lst_x_keys, lst_y_keys):
        """
        init
        """
        self.load_data(data_file, delimiter, lst_x_keys, lst_y_keys)

    def load_data(self, data_file, delimiter, lst_x_keys, lst_y_keys):
        # Load the dataset
        self.dataset = numpy.loadtxt(data_file, delimiter=",") 
        self.X = self.dataset[:, lst_x_keys] 
        self.Y = self.dataset[:, lst_y_keys]
    
    def create_model(self):
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
    
    def init_model(self):
        self.model = self.create_model()
    
    def train_model(self, ):
        ## fit once:
        X = self.X
        Y = self.Y
        checkpoint_callback = ModelCheckpoint('weights.{epoch:02d}-{acc:.2f}.hdf5', monitor='acc', save_best_only=False)
        history_callback = LossHistory()
        callbacks_list = [checkpoint_callback, history_callback]
        history = self.model.fit(X, Y, nb_epoch=10, batch_size=10, callbacks=callbacks_list) # Evaluate the model
        scores = self.model.evaluate(X, Y)
        print history_callback.losses
        print "final %s: %.2f%%" % (self.model.metrics_names[1], scores[1] * 100)
        print history.history
    
    def process(self):
        self.init_model()
        self.train_model()

    
def process_from_checkpoint():
    init_model()
    train_model()


if "__main__" == __name__:
    data_file='../../data/pima-indians-diabetes.csv'
    lst_x_keys = list(xrange(0, 8))
    lst_y_keys = [8]
    delimiter = ','
    haha = BaseKerasModel(data_file, delimiter, lst_x_keys, lst_y_keys)
    haha.process()
    exit(0)
