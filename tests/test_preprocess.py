import os
import sys
sys.path.append('/classifier')

import skimage.io as io
from skimage import data_dir
import src.preprocess as pp
import pandas as pd


def test_ioImageCollectio():
    '''
    Greyscale image 
    '''
    ceviche = io.ImageCollection('data/ceviche/393751.jpg', as_gray = True)
    dimensions = [len(dim.shape) for dim in ceviche]
    
    assert max(dimensions) == 2, "Image has more than 2 dimensions, not greyscale"

def test_pixel_dimensions():
    test_data = io.ImageCollection(data_dir + '/r*.jpg')
    cols = pp.pixel_dimensions(test_data, dimension = 'width')
    
    assert cols == [1411, 427]
    
def test_frequency_table():
    widths = [500,500,500,400,400,400]
    heights = [500,500,500,300,300,100]
    
    table = pp.frequency_table(width_list = widths,
                               height_list = heights)
    
    assert type(table) == pd.DataFrame

def test_resize_greyscale():
    img='/classifier/data/ceviche/904.jpg'
    preprocessed = pp.resize_greyscale(path = img)
    
    assert preprocessed['data_pp'][0].shape[0] == 8464