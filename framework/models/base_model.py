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

import sys
import os
import ConfigParser

base_path = os.path.dirname(os.path.abspath(__file__)) + "/../../"
os.sys.path.append(base_path)
DEFAULT_LOG_FILENAME = base_path + "/log/base_model"
config_path = base_path + '/conf/'

import logging

class BaseModel(object):
    """
    base keras model based on keras's model(without sklearn)
    """
    def __init__(self):
        """
        init
        """
        pass

    def load_data(self, data_file, delimiter, lst_x_keys, lst_y_keys):
        """
        load data
        """
        pass
    
    def create_model(self):
        """
        create model
        """
        pass
    
    def init_model(self):
        """
        init model
        """
        self.model = self.create_model()
    
    def train_model(self, ):
        """
        train model
        """
        pass
    
    def process(self):
        """
        process
        """
        self.init_model()
        self.train_model()


if "__main__" == __name__:
    data_file='../../data/pima-indians-diabetes.csv'
    lst_x_keys = list(xrange(0, 8))
    lst_y_keys = [8]
    delimiter = ','

    config_file = config_path + 'demo.conf'
    conf = ConfigParser.ConfigParser()
    conf.read(config_file)
    demo_log_file = base_path + "log/" + conf.get("log", "log_name")
    haha = BaseModel(data_file, delimiter, lst_x_keys, lst_y_keys, log_filename=demo_log_file)
    haha.process()
    exit(0)
