"""
Name: Shameen Shetty
ID	: 1001429743
"""

import numpy as np
import matplotlib.pyplot as plt

''' Main Function '''
if __name__ == "__main__" :
    fileName = "data-filtering.csv"
    csvData = np.genfromtxt(fileName, dtype=None, delimiter=",")
    f_s = 2000 # sampling rate
    
    ''' setting up the low-pass filter '''
    filterLen = 21
    M = filterLen - 1
    f_c = 50 # cut off frequency, 50Hz
    f_t = f_c / f_s # normalized cut-off frequency
    lowPassFilter = []
    
    '''For the below for-loop we are setting up a low pass filter'''
    for n in range(filterLen):
        if (n != M/2):
            numerator = np.sin(2* np.pi * f_t * (n - (M/2)))
            denominator = np.pi * (n - (M/2))
            
            lowPassFilter.append(numerator / denominator)
        if (n == M/2):
            lowPassFilter.append(2 * f_t)
    
    
    ''' Convolving original signal with a lowpass filter '''
    low_ConvolvedSignal = np.convolve(csvData, lowPassFilter)
    
    fig, axs = plt.subplots(3)
    fig.suptitle('Figure 1: Lowpass filter', fontweight='bold', x=0.5, y=1.1)
    axs[0].plot(csvData)
    axs[0].set_title("Original Signal")
    
    
    ''' Plotting a 4Hz signal, using formula Asiw(ωt) where ω is the 2*pi*f
    so a 4Hz signal = 2 * pi * 4. The 0.0125 is to make sure we get the x-ticks
    going from 0  to 2000 '''
    axs[1].plot(np.cos(np.arange(0, 2 * 4 * np.pi, 0.0125)))
    axs[1].set_title("4 Hz signal")
    
    axs[2].plot(low_ConvolvedSignal)
    axs[2].set_title("application of lowpass filter")

    fig.tight_layout() #So that the multiple subplots arent too close to each other
    
    
    ''' setting up the high-pass filter'''
    filterLen = 21
    M = filterLen - 1
    f_c = 280 # cutOff freq for highPass filter, 280Hz
    f_t = f_c / f_s # normalized cut-off frequency
    highPassFilter = []
    
    '''For the below for-loop we are setting up a high pass filter'''
    for n in range(filterLen):
        if (n != M/2):
            numerator = -1 * np.sin(2* np.pi * f_t * (n - (M/2)))
            denominator = np.pi * (n - (M/2))
            highPassFilter.append(numerator / denominator)
            
        if (n == M/2):
            highPassFilter.append(1 - (2 * f_t))
    
    ''' Convolving original signal with a highpass filter '''
    high_ConvolvedSignal = np.convolve(csvData, highPassFilter)
    
    fig2, axs2 = plt.subplots(3)
    fig2.suptitle('Figure 2: Highpass filter', fontweight='bold', x=0.5, y=1.1)
    '''[0:100] so that we get the first 100 values only instead of the original
    2000 values for csvData'''
    axs2[0].plot(csvData[0:100])
    axs2[0].set_title("Original Signal")
    
    ''' Plotting a 330Hz signal, using formula Asiw(ωt) where ω is the 2*pi*f
    so a 4Hz signal = 2 * pi * 330. The 20 is to make sure we get the x-ticks
    going from 0  to 100 '''
    axs2[1].plot(np.cos(np.arange(0, 2 * 330 * np.pi, 20)))
    axs2[1].set_title("330 Hz signal")
    
    '''
    Getting the first 100 values for the high_convolvedSignal
    '''
    axs2[2].plot(high_ConvolvedSignal[0:100])
    axs2[2].set_title("application of highpass filter")
    
    '''   To prevent the subplots from being too close to each other   '''
    fig2.tight_layout()
    
    plt.show()