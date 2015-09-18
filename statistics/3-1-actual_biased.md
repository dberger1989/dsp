[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>>In this example, we want to measure how many children under 18 live in each household. If you were to ask each of the children how big their family is, you would get an overrepresentation of the bigger families, and so you would ahve a biased pmf. This occurs because the probability, which is unbiased, is multiplied by the number of children observing the family size. 
Below we give a function that computes this, followed by a step chart showing the difference, and finally the actual and biased mean output. 

```
import thinkstats2
import chap01soln
import thinkplot
responses = chap01soln.ReadFemResp()
pmf = thinkstats2.Pmf(responses.numkdhh, label='actual')
def BiasPmf(pmf, label=''):
    new_pmf = pmf.Copy(label=label)
    for x, p in pmf.Items():
       new_pmf.Mult(x, x)
    new_pmf.Normalize()
    return new_pmf

biased_pmf = BiasPmf(pmf,label='biased')

thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf,biased_pmf])
thinkplot.Show(xlabel='Number children under age 18 in household',ylabel='PMF')

actual = pmf.Mean()
biased = biased_pmf.Mean()
```
<img src = "Downloads/figure_1.png">
>>The actual pmf mean was 1.02, and the biased pmf mean was 2.40. 

