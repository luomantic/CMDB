#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys

BASE_DIR = os.path.dirname(os.getcwd())
print('base_dir:'+ BASE_DIR)
# 设置工作目录，使得包和模块能够正常导入
sys.path.append(BASE_DIR)

from Client.core import handler

if __name__ == '__main__':
    handler.ArgvHandler(sys.argv)
