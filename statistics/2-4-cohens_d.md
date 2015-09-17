[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>>In the code below, I find the means of all live first births and all live births that are not 'firsts'. I use Cohen's d to find how great of a difference there is between these two means. To do this we take the difference in means and divide it by the pooled standard deviation, and this gives us a d of -0.0886729270726. This means that first births are lighter than others by -0.0886729270726 standard deviations, which is less than 10 percent of a standard deviation. This tells us that the difference in mean weight between the of first-borns and non-firstborns is less than 10% the difference we would expect to see between individual babies within these 2 groups themselves. 
>>
```
live = preg[preg.outcome == 1]
other = preg[preg.outcome != 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]
firstsmean = firsts.totalwgt_lb.mean()
othersmean = others.totalwgt_lb.mean()
meandiff = firstsmean - othersmean
s1 = (firsts.totalwgt_lb.var() * len(firsts))
s2 = (others.totalwgt_lb.var() * len(others)) 
nu= (len(firsts) + len(others))
pooled_var = (s1 + s2)/nu
d = meandiff/ math.sqrt(pooled_var)
print d
```


