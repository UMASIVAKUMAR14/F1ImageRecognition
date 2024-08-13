import numpy as np
import cv2
import pywt

#img is the input image, mode is the default wavelet type, level is the level of decomposition
def w2d(img, mode='haar' , level=1):
    imArray = img
    # DATATYPE CONVERSIONS
        # convert from RGB to grayscale
    imArray = cv2.cvtColor(imArray, cv2.COLOR_RGB2GRAY)
        # convert each pixel to 32-bit floating point
    imArray = np.float32(imArray)
        # normalize the pixel values by dividing by 255, scaling values to the range [0, 1]
    imArray/= 255;
        # compute 2D discrete wavelet transform [DWT] of image. 
            # cfs[0] is the approx coeffs (low-frequency components) in a 2D numpy array. cfs[1], cfs[2], 
            # & so on are tuples, each with 3 2D numpy arrays of detail coefficients (high-frequency components) 
            # in horizontal, vertical, and diagonal directions at each level of decomposition
    cfs = pywt.wavedec2(imArray, mode, level=level)
    
    # PROCESS COEFFICIENTS
        # converts cfs to a modifiable list
    cfs_h = list(cfs)
        # set approx coeffs to 0 to focus the reconstruction on details
    cfs_h[0] *= 0;
    
    # RECONSTRUCTION
        # reconstructs the image with the modified wavelet transformations
    imArray_h = pywt.waverec2(cfs_h, mode);
        # scales the reconstructed image back to [0, 255]
    imArray_h *= 255;
        # converts image back to standard 8-bit unsigned integer format
    imArray_h = np.uint8(imArray_h)
    
    return imArray_h