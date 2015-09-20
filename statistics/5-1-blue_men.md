[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> Given the mean height and standard deviation, I generated a random set of numbers that fit the shape of the model using the norm method, and giving it a mean of 178 and a std of 7.7. 
Then I found the difference between the cdf of the upper limit (convereted from inches to cm), and the cdf of the lower limit. this difference represents the chance that someone will be equal or below the upper limit, and equal or above the lower limit. 


>>The percent that a male fits in the range for the Blue Man Group is 0.34209468294595308

```
import scipy.stats
distribution = scipy.stats.norm(178, 7.7)
prob_blue = distribution.cdf(185.4) - distribution.cdf(177.8)
prob_blue
```
