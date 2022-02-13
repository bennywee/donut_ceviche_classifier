import skimage.io as io

def test_ioImageCollection():
    '''
    Greyscale image 
    '''
    ceviche = io.ImageCollection('data/ceviche/393751.jpg', as_gray = True)
    dimensions = [len(dim.shape) for dim in ceviche]
    
    assert max(dimensions) == 2, "Image has more than 2 dimensions, not greyscale"
    
    