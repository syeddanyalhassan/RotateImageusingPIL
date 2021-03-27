# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 13:00:55 2021

@author: danyal.hassan
"""


# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 11:59:16 2021

@author: danyal.hassan
"""
""

""""For importing os and PIL"""
import os
from PIL import Image

"""For rotating and showing image """
sourcepath = os.path.dirname(__file__)
file=sourcepath+"\download.jfif"
im=Image.open(file);
im.rotate(90).show();

"""for resizing and saving image with new name"""
new_im = im.resize((640,480))
new_im.save(sourcepath+"\example_resized.jpg")




