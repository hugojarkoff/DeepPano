import numpy as np
import matplotlib.pyplot as plt
import xml
import xml.etree.ElementTree as ET
import matplotlib.path as mpltPath



def create_mask(img_path, xml_path):
    """
    Create a mask from img_path and xml_path (xml file of polygons).
    Mask is an array of True/False in the same shape as img.
    
    inputs : 
        img_path (str) : (relative) path of the img
        xml_path (str) : (relative) path of the xml file containing the polygons of the mask
        
    outputs :
        mask (np.array) : array of True/False for each pixel of the img
    
    """
    
    img = plt.imread(img_path)
    img_shape = (img.shape[1], img.shape[0])
    
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    lx,ly = np.arange(img_shape[0]), np.arange(img_shape[1])
    coordinates = [[x,y] for x in lx for y in ly]
    
    mask = np.array([False]*img_shape[0]*img_shape[1])
    
    for object in root.findall('object'):
        polygon = [int(child.text) for child in object.findall('polygon')[0]]
        polygon = np.reshape(polygon, (int(len(polygon)/2),2))
        path = mpltPath.Path(polygon)
        mask_polygon = np.array(path.contains_points(coordinates))
        mask = mask | mask_polygon
    
    return mask.reshape(img_shape).T

def create_list_img(list_panos):
    """
    Create list of img from list of panos (str).
    Simple utility function, used to return a list of img from the list of names
    
    """
    list_img = []
    for pano in list_panos:
        img_path = './img/'+pano+'.png'
        list_img.append(plt.imread(img_path))
    return list_img

def create_list_masks(list_panos):
    """
    Create list of masks from list of panos (str)
    Applies successively the create_mask function to each and everyone of the img/xml files in the list of panoss
    """
    list_masks = []
    for pano in list_panos:
        img_path = './img/'+pano+'.png'
        xml_path = './annot/'+pano+'.xml'
        list_masks.append(create_mask(img_path, xml_path))
    return list_masks
