[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

>>In the code below, we first read the data from hinc.py. Then we use the InterpolateSample which makes a sample out of the data with an upper limit of log 6, or $1,000,000, and a lower limit of log 3. 

>>The data is in log form, so to convert it we take 10 to each income entry. Now we have our sample ready for analysis and we find the mean is 74278.707531187203, the median is 51226.454478940461, and the standard deviation is 93946.92996347824. The mean is much higher than the median, telling is there is a significant positive skew. The skewness confirms this, and the pearson median coefficient is 0.7361258019141782. After caclculating the cdf, we see that about 66% of all the incomes fall below the mean, which tells us the incomes at the top are making the mean a poor calculator of average, and are not distributed normally. 

>>If we were to make the upper limit even larger, we would expect the same thing, with more incomes at the top skewing the data upward, and making the difference between median and mean even larger. 

```python

>>> import thinkstats2
>>> import hinc
>>> import hinc2
>>> import numpy as np
>>> df = hinc.ReadData()
>>> 
>>> def InterpolateSample(df, log_upper=6.0):
...     df['log_upper'] = np.log10(df.income)
...     df['log_lower'] = df.log_upper.shift(1)
...     df.log_lower[0] = 3.0
...     df.log_upper[41] = log_upper
...     arrays = []
...     for _, row in df.iterrows():
...         vals = np.linspace(row.log_lower, row.log_upper, row.freq)
...         arrays.append(vals)
...     log_sample = np.concatenate(arrays)
...     return log_sample
... 
>>> log_sample = InterpolateSample(df, log_upper=6.0)
>>> 
>>> sample = [10**i for i in log_sample]
>>> thinkstats2.Mean(sample)
74278.707531187203
>>> thinkstats2.Std(sample)
93946.92996347824
>>> thinkstats2.Median(sample)
51226.454478940461
>>> 
>>> thinkstats2.Skewness(sample)
4.9499202444295829
>>> thinkstats2.PearsonMedianSkewness(sample)
0.7361258019141782
>>> 
>>> cdfsample = thinkstats2.Cdf(sample)
>>> cdfsample[thinkstats2.Mean(sample)]
0.66000587956687196
>>> 
```
