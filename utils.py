import numpy as np
import matplotlib.pyplot as plt
import xml
import xml.etree.ElementTree as ET
import matplotlib.path as mpltPath

def reshape_img_masks(list_img,list_masks):
    """
    Reshape every img and mask according to the smallest dimensions present in the list.
    """
     
    min_x = min([img.shape[1] for img in list_img])
    min_y = min([img.shape[0] for img in list_img])
    
    output_img_list = [img[:min_y,:min_x,0] for img in list_img]
    output_mask_list = [mask[:min_y,:min_x]*1 for mask in list_masks]
    
    return output_img_list, output_mask_list
