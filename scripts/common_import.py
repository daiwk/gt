#!/usr/bin/env python
# -*- coding: gbk -*-
########################################################################
# 
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: common_import.py
Author: root(root@baidu.com)
Date: 2016/07/10 09:40:13
"""

import sys
import os
import ConfigParser

base_path = os.path.dirname(os.path.abspath(__file__)) + "/../"
os.sys.path.append(base_path)

from plugins.base_model.base_keras_model import BaseKerasModel
from plugins.base_model.base_keras_sklearn_model import BaseKerasSklearnModel
