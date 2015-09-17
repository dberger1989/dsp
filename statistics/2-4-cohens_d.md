[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> ```

live = preg[preg.outcome == 1]

>>other = preg[preg.outcome != 1]
>>firsts = live[live.birthord == 1]
>>others = live[live.birthord != 1]
>>firstsmean = firsts.totalwgt_lb.mean()
>>othersmean = others.totalwgt_lb.mean()

>>meandiff = firstsmean - othersmean

>>s1 = (firsts.totalwgt_lb.var() * len(firsts))
s2 = (others.totalwgt_lb.var() * len(others)) 
nu= (len(firsts) + len(others))
pooled_var = (s1 + s2)/nu
d = meandiff/ math.sqrt(pooled_var)
print d
```


