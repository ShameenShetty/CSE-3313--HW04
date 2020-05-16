"""
Name: Shameen Shetty
ID	: 1001429743
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import ndimage

''' Main Function '''
if __name__ == "__main__":
#   Getting the names of all the pictures we are using, including their format
    boatPicture_Name = "boat.512.tiff"
    clockPicture_Name = "clock-5.1.12.tiff"
    manPicture_Name = "man-5.3.01.tiff"
    tankPicture_Name = "tank-7.1.07.tiff"
    darianGrayPicture_Name = "darinGrayNoise.jpg"
    
    
    ''' Solving for boat'''
    
    fig1, axs1 = plt.subplots(3)
    
    
    img = mpimg.imread(boatPicture_Name)
    '''    cmap=plt.cm.gray so that instead of getting a yellow-green in the 
    original img, we convert it to greyscale instead    '''
    imgplot1 = axs1[0].imshow(img, cmap=plt.cm.gray)
    axs1[0].set_title("Original Image of Boat")
    
    '''
    Create a low pass filter which is a 10 point moving avg, that
    is h[n] has 10 values of 0.1
    '''
    lowPassFilter = 0.1 * np.ones(10)
    
    height, width = img.shape
    convolvedOutput_low = []
    for n in range(height):
        result = np.convolve(lowPassFilter, img[n])
        convolvedOutput_low.append(result)
        
    
    imgplot2 = axs1[1].imshow(convolvedOutput_low, cmap=plt.cm.gray)
    axs1[1].set_title("Blurred Image of boat")
    
    highPassFilter = [-1, 1]
    convolvedOutput_high = []
    for n in range(height):
        result = np.convolve(highPassFilter, img[n])
        convolvedOutput_high.append(result)
        
    imgplot3 = axs1[2].imshow(convolvedOutput_high, cmap=plt.cm.gray)
    axs1[2].set_title("Edge Detection for boat")
    
    fig1.tight_layout() #So that the multiple subplots arent too close to each other
    
    
    
    
    ''' Solving for clock'''
    
    fig2, axs2 = plt.subplots(3)
    
    
    img = mpimg.imread(clockPicture_Name)
    '''    cmap=plt.cm.gray so that instead of getting a yellow-green in the 
    original img, we convert it to greyscale instead    '''
    imgplot1 = axs2[0].imshow(img, cmap=plt.cm.gray)
    axs2[0].set_title("Original Image of Clock")
    
    '''
    Create a low pass filter which is a 10 point moving avg, that
    is h[n] has 10 values of 0.1
    '''
    lowPassFilter = 0.1 * np.ones(10)
    
    height, width = img.shape
    convolvedOutput_low = []
    for n in range(height):
        result = np.convolve(lowPassFilter, img[n])
        convolvedOutput_low.append(result)
        
    
    imgplot2 = axs2[1].imshow(convolvedOutput_low, cmap=plt.cm.gray)
    axs2[1].set_title("Blurring Clock Image")
    
    highPassFilter = [-1, 1]
    convolvedOutput_high = []
    for n in range(height):
        result = np.convolve(highPassFilter, img[n])
        convolvedOutput_high.append(result)
        
    imgplot3 = axs2[2].imshow(convolvedOutput_high, cmap=plt.cm.gray)
    axs2[2].set_title("Edge Detection for Clock")
    
    fig2.tight_layout() #So that the multiple subplots arent too close to each other
    
    
    ''' Solving for man'''
    
    fig3, axs3 = plt.subplots(3)
    
    
    img = mpimg.imread(manPicture_Name)
    '''    cmap=plt.cm.gray so that instead of getting a yellow-green in the 
    original img, we convert it to greyscale instead    '''
    imgplot1 = axs3[0].imshow(img, cmap=plt.cm.gray)
    axs3[0].set_title("Original Image for picture of Man")
    
    '''
    Create a low pass filter which is a 10 point moving avg, that
    is h[n] has 10 values of 0.1
    '''
    lowPassFilter = 0.1 * np.ones(10)
    
    height, width = img.shape
    convolvedOutput_low = []
    for n in range(height):
        result = np.convolve(lowPassFilter, img[n])
        convolvedOutput_low.append(result)
        
    
    imgplot2 = axs3[1].imshow(convolvedOutput_low, cmap=plt.cm.gray)
    axs3[1].set_title("Blurring Man Image")
    
    highPassFilter = [-1, 1]
    convolvedOutput_high = []
    for n in range(height):
        result = np.convolve(highPassFilter, img[n])
        convolvedOutput_high.append(result)
        
    imgplot3 = axs3[2].imshow(convolvedOutput_high, cmap=plt.cm.gray)
    axs3[2].set_title("Edge Detection for Man")
    
    fig3.tight_layout() #So that the multiple subplots arent too close to each other
    
    
    ''' Solving for tank'''
    
    fig4, axs4 = plt.subplots(3)
    
    
    img = mpimg.imread(tankPicture_Name)
    '''    cmap=plt.cm.gray so that instead of getting a yellow-green in the 
    original img, we convert it to greyscale instead    '''
    imgplot1 = axs4[0].imshow(img, cmap=plt.cm.gray)
    axs4[0].set_title("Original Image for picture of Tank")
    
    '''
    Create a low pass filter which is a 10 point moving avg, that
    is h[n] has 10 values of 0.1
    '''
    lowPassFilter = 0.1 * np.ones(10)
    
    height, width = img.shape
    convolvedOutput_low = []
    for n in range(height):
        result = np.convolve(lowPassFilter, img[n])
        convolvedOutput_low.append(result)
        
    
    imgplot2 = axs4[1].imshow(convolvedOutput_low, cmap=plt.cm.gray)
    axs4[1].set_title("Blurring Tank Image")
    
    highPassFilter = [-1, 1]
    convolvedOutput_high = []
    for n in range(height):
        result = np.convolve(highPassFilter, img[n])
        convolvedOutput_high.append(result)
        
    imgplot3 = axs4[2].imshow(convolvedOutput_high, cmap=plt.cm.gray)
    axs4[2].set_title("Edge Detection for Tank")
    
    fig4.tight_layout() #So that the multiple subplots arent too close to each other
    
    
    ''' Solving for Darian Gray'''
    
    fig5, axs5 = plt.subplots(3)
    
    
    img = mpimg.imread(darianGrayPicture_Name)
    '''    cmap=plt.cm.gray so that instead of getting a yellow-green in the 
    original img, we convert it to greyscale instead    '''
    imgplot1 = axs5[0].imshow(img, cmap=plt.cm.gray)
    axs5[0].set_title("Original Image with salt and pepper noise")
    
    '''
    Create a low pass filter which is a 10 point moving avg, that
    is h[n] has 10 values of 0.1
    '''
    lowPassFilter = 0.1 * np.ones(10)
    
    height, width = img.shape
    convolvedOutput_low = []
    for n in range(height):
        result = np.convolve(lowPassFilter, img[n])
        convolvedOutput_low.append(result)
        
    
    imgplot2 = axs5[1].imshow(convolvedOutput_low, cmap=plt.cm.gray)
    axs5[1].set_title("Removing noise  with lowPass filter")
    
    outputImage = ndimage.median_filter(img, 5)
        
    imgplot3 = axs5[2].imshow(outputImage, cmap=plt.cm.gray)
    axs5[2].set_title("Applying median filter to original image")
    
    fig5.tight_layout() #So that the multiple subplots arent too close to each other
    plt.show()