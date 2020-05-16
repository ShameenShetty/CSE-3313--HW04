# CSE-3313-HW04
This is the coding assignment for Homework 4 for CSE3313 (Introduction to Signal Processing).
There are 2 coding assignment questions for this hw, the first is **Design of Lowpass and Highpass FIR filters** and the second is **Image Processing** using these filters

## Purpose for first coding question
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

## Purpose for second coding question


### Process for second coding question
