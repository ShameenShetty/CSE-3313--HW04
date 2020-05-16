# CSE-3313-HW04
This is the coding assignment for Homework 4 for CSE3313 (Introduction to Signal Processing).
There are 2 coding assignment questions for this hw, the first is **Design of Lowpass and Highpass FIR filters** and the second is **Image Processing** using these filters

## Purpose for first coding question: Design of Lowpass and Highpass FIR Filters
Learn how to produce the filter coefficients needed to construction lowpass and
highpass filters.

That is, a common signal processing task is to remove the components of a signal whose frequency
is outside a particular range. A lowpass filter removes the components whose frequency is
higher than a certain cut-off frequency while a highpass filter removes the components whose
frequency is below a certain cut-off frequency.

### Process for first coding question
* First we design a low-pass filter with the following specifications
  - A cut-frequency of f<sub>c</sub> = 50 Hz
  - Filter length of L = 21, and M = filter length - 1
  - 0 ≤ n < L
  
The filter weights w[n] are found using the formula:  

<a href="https://www.codecogs.com/eqnedit.php?latex=w[n]&space;=&space;\begin{Bmatrix}&space;\frac{sin[2\pi&space;f_t&space;(n-\frac{M}{2})))]]}{\pi(n-\frac{M}{2}))}&space;&&space;n&space;\neq&space;\frac{M}{2}&space;\\&space;2f_t&space;&&space;n&space;=&space;\frac{M}{2}&space;\end{Bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?w[n]&space;=&space;\begin{Bmatrix}&space;\frac{sin[2\pi&space;f_t&space;(n-\frac{M}{2})))]]}{\pi(n-\frac{M}{2}))}&space;&&space;n&space;\neq&space;\frac{M}{2}&space;\\&space;2f_t&space;&&space;n&space;=&space;\frac{M}{2}&space;\end{Bmatrix}" title="w[n] = \begin{Bmatrix} \frac{sin[2\pi f_t (n-\frac{M}{2})))]]}{\pi(n-\frac{M}{2}))} & n \neq \frac{M}{2} \\ 2f_t & n = \frac{M}{2} \end{Bmatrix}" /></a>  

Where f<sub>t</sub> = f<sub>c</sub> / f<sub>s</sub> is the normalized cut-off freq.

* Then we use `numpy.convolve()` function to apply the filter.
* For the highpass filter, we design a highpass filter with the following specifications:
  - A cut-off freq of f<sub>c</sub> = 280 Hz
  - Filter len of 21 and M = filter len - 1
  
The filter weights w[n] are found from:  

<a href="https://www.codecogs.com/eqnedit.php?latex=w[n]&space;=&space;\begin{Bmatrix}&space;-\frac{sin[2\pi&space;f_t&space;(n-\frac{M}{2})))]]}{\pi(n-\frac{M}{2}))}&space;&&space;n&space;\neq&space;\frac{M}{2}&space;\\&space;1&space;-&space;2f_t&space;&&space;n&space;=&space;\frac{M}{2}&space;\end{Bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?w[n]&space;=&space;\begin{Bmatrix}&space;-\frac{sin[2\pi&space;f_t&space;(n-\frac{M}{2})))]]}{\pi(n-\frac{M}{2}))}&space;&&space;n&space;\neq&space;\frac{M}{2}&space;\\&space;1&space;-&space;2f_t&space;&&space;n&space;=&space;\frac{M}{2}&space;\end{Bmatrix}" title="w[n] = \begin{Bmatrix} -\frac{sin[2\pi f_t (n-\frac{M}{2})))]]}{\pi(n-\frac{M}{2}))} & n \neq \frac{M}{2} \\ 1 - 2f_t & n = \frac{M}{2} \end{Bmatrix}" /></a>   


Where f<sub>t</sub> = f<sub>c</sub> / f<sub>s</sub> is the normalized cut-off freq.  

* Then once again, apply this highpass filter using `numpy.convolve()` to the original signal.

## Purpose for second coding question : Image Processing
 Learn to apply simple filters to images.

### Process for second coding question
* We display the original images from the tiff images given (boat, clock, man, and tank) in their own figure window
* We then **blur the images** using a *lowpass filter*
  - The lowpass filter is a 10-point moving average (that is, h[n] consists of 10 values of 0.1 each)
  - Apply this filter to each row of the image using the convolve function 
  - Display the processed image in its own figure window
  
* Then we perform **edge detection** using a *highpass filter*
  - For this filter, h[n] = {1, -1}
  - Apply this filter to each row of the original image
  - Display the processed image in its own figure window.
  
* We do these steps for each individual image given

* Finally for the image *darinGreyNoise.jpg* we do the following:
  - remove the noise  
    i. Display the original image in its own figure window. This image contains what is called “salt and pepper” noise.   
    ii. Remove the noise by averaging it out using a low-pass filter. So we apply the 10-point running average to each row of the image.   
    iii. Apply a *medin filter* (which is a nonlinear filter) to the original noisy image using `outputImage = ndimage.median filter(inputImage, 5)` where `imputImage` and `outputImage` are the names we choose. We use the import `from scipy import ndimage`

