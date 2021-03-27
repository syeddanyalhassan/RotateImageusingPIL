# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 11:59:16 2021

@author: danyal.hassan
"""

import os
from PIL import Image
sourcepath = os.path.dirname(__file__)
file=sourcepath+"\Desktop\Screenshot_1.jpg"
im=Image.open(file);
im.rotate(90).show();



