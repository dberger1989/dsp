# Hint:  use Google to find python function

####a) 
```
import datetime
from datetime import date 

date_start = '01-02-2013'  
date_stop = '07-28-2015'

date_start = date(2013, 01, 02)
date_stop = date(2015, 07, 28)
datediff = date_stop - date_start
print datediff
```

####b)  
date_start = '12312013'  
date_stop = '05282015' 

```
import datetime
from datetime import date 
date_start = '12312013'
date_stop = '05282015' 

def dateformat(date_start1):
    li = []
    i = 0
    li.append(int(date_start1[4:8]))
    li.append(int(date_start1[0:2]))
    li.append(int(date_start1[2:4]))
    print li
    return li

startlist = dateformat(date_start)
stoplist = dateformat(date_stop)

dstart_formatted = dstopformatted = date(startlist[0], startlist[1],startlist[2])
dstop_formatted = date(stoplist[0], stoplist[1],stoplist[2])
difference_between_dates = dstop_formatted- dstart_formatted
print difference_between_dates
```

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015' 

```
import datetime
from datetime import *

date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'

dstart_formatted = datetime.strptime(date_start, '%d-%b-%Y').date()
dstop_formatted = datetime.strptime(date_stop, '%d-%b-%Y').date()

print dstop_formatted - dstart_formatted
```
