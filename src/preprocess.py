import pandas as pd
import numpy as np
import skimage.io as io
from skimage.transform import resize, rescale, rotate

def pixel_dimensions(df, dimension):
    '''
    Returns list of pixel dimensions for a collection of images
    '''
    
    if dimension == 'width':
        dim = 0
    elif dimension == 'height':
        dim = 1
    else:
        raise ValueError('Dimension must be either height or width')
    
    size_dim = [img.shape[dim] for img in df]
    
    return(size_dim)

def frequency_table(width_list, height_list):
    '''
    Returns frequency table of image dimensions
    '''
    
    image_sizes = pd.DataFrame({'width': width_list,
                                'height': height_list})\
                    .groupby(['width', 'height'])\
                    .value_counts()\
                    .reset_index()\
                    .sort_values(0, ascending = False)\
                    .rename(columns = {0: 'freq'})
    
    return(image_sizes)

def resize_greyscale(path):
    '''
    Loads in image data in greyscale and rescales and resizes them consistently
    '''
    
    # Load data
    df = io.ImageCollection(path, as_gray = True)
    
    # Prepare empty dictionary
    pp_data= dict()
    
    # Rescale images
    rescale_df = [rescale(img, 0.2) for img in df]
    
    # Resize images and convert into numpy array
    # 92x92 based on exploratory data analysis
    pp_data['data_pp'] = np.array([resize(img, (92, 92)).reshape(-1) for img in rescale_df])
    pp_data['img_name'] = np.array([name for name in df._files])
    
    return(pp_data)