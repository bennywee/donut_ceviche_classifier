import os
import sys
sys.path.append('/classifier')

import skimage.io as io
from skimage import data_dir
import src.preprocess as pp


def test_ioImageCollectio():
    '''
    Greyscale image 
    '''
    ceviche = io.ImageCollection('data/ceviche/393751.jpg', as_gray = True)
    dimensions = [len(dim.shape) for dim in ceviche]
    
    assert max(dimensions) == 2, "Image has more than 2 dimensions, not greyscale"

def test_pixel_dimensions():
    test_data = io.ImageCollection(data_dir + '/r*.jpg')
    cols = pp.pixel_dimensions(test_data, dim = 0)
    
    assert cols == [1411, 427]