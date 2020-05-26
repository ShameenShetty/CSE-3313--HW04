"""
Name: Shameen Shetty
ID	: 1001429743
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import ndimage


'''
	Function: imageProcessingFunction
	Parameters:
		1) imgName: This is the name of the image that we are reading from
		
		2) originalImgTitle: This means that we when plot the image and title it as
		"Original Image of Boat/Tank/Man" we write it to this parameter - originalImgTitle

		3) lowPass_ImgTitle: The title of the plot for the lowPass filtered image

		4) highPass_ImgTitle: The title of the plot for the highPass filtered image
	Returns: None
	Description: Reads in the name of the original image into a param called imgName, then
	reads the img using mpimg.imread(), we convert it to greyscale, then create a lowPass filter
	and a highPass filter and convolve each row of the original img with those respective filters
	and finally plot the original image, then the lowPass filtered img, and the highPass filtered
	img all in one plot.
'''
def imageProcessingFunction(imgName, originalImgTitle, lowPass_ImgTitle, highPass_ImgTitle):
	'''
	We want all the images (the original, the lowPass filtered img, and the highPass filtered img)
	to be on the same plot, hence we use subplots(3)
	'''
	fig, axs = plt.subplots(3)

	img = mpimg.imread(imgName)

	'''Using cmap=plt.cm.gray so that instead of getting a yellow-green in the 
	original img, we convert it to greyscale instead'''
	imgplot = axs[0].imshow(img, cmap=plt.cm.gray)
	axs[0].set_title(originalImgTitle)

	'''	Create a low pass filter which is a 10 point moving avg, that
	is h[n] has 10 values of 0.1 '''
	lowPassFilter = 0.1 * np.ones(10)

	height, width = img.shape


	''' Our lowPass filter, we will convolve each row of the image using img[n],
	and then append that result into a list called convolvedOutput_low'''
	convolvedOutput_low = []
	for n in range(height):
		result = np.convolve(lowPassFilter, img[n])
		convolvedOutput_low.append(result)
		
	lowpass_imgPlot = axs[1].imshow(convolvedOutput_low, cmap=plt.cm.gray)
	axs[1].set_title(lowPass_ImgTitle)

	''' Our highPass filter, we wil convolve it with each row of the original image
	and append the result into our convolvedOutput_high list'''
	highPassFilter = [-1, 1]
	convolvedOutput_high = []
	for n in range(height):
		result = np.convolve(highPassFilter, img[n])
		convolvedOutput_high.append(result)
		
	highPass_imgplot = axs[2].imshow(convolvedOutput_high, cmap=plt.cm.gray)
	axs[2].set_title(highPass_ImgTitle)
	
	fig.tight_layout() # So that the multiple subplots arent too close to each other



''' Main Function '''
if __name__ == "__main__":
#   Getting the names of all the pictures we are using, including their format
	boatPicture_Name = "boat.512.tiff"
	clockPicture_Name = "clock-5.1.12.tiff"
	manPicture_Name = "man-5.3.01.tiff"
	tankPicture_Name = "tank-7.1.07.tiff"
	darianGrayPicture_Name = "darinGrayNoise.jpg"
	
	
	''' Solving for boat'''
	imageProcessingFunction(boatPicture_Name, "Original Image of Boat", "Blurred Image of Boat", "Edge Detection for boat")	
	
	''' Solving for clock'''
	imageProcessingFunction(clockPicture_Name, "Original Image of Clock", "Blurring Clock Image", "Edge Detection for Clock")	
	
	''' Solving for man'''
	imageProcessingFunction(manPicture_Name, "Original Image for picture of Man", "Blurring Man Image", "Edge Detection for Man")
	
	''' Solving for tank'''
	imageProcessingFunction(tankPicture_Name, "Original Image for picture of Tank", "Blurring Tank Image", "Edge Detection for Tank")


	
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
