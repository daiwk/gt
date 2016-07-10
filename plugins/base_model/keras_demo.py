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

import numpy
import logging

from keras.models import Sequential 
from keras.layers import Dense 
from keras.layers import Dropout
from keras.layers import Convolution2D

from keras.wrappers.scikit_learn import KerasClassifier

from keras.optimizers import SGD

from keras.callbacks import ModelCheckpoint
from keras.callbacks import Callback

model = Sequential()
#model.add(Convolution2D(7, 3, 3, border_mode='same', input_shape=(3, 256, 256), dim_ordering='th'))
model.add(Convolution2D(64, 3, 3, border_mode='same', input_shape=(3, 256, 256), dim_ordering='tf'))
print model.output_shape
