import random
import time

def getrandomdate(s,e):
    randomgenerator = random.random()
    dateformat="%d/%m/%Y"
    sdate=time.mktime(time.strptime(s,dateformat))
    edate=time.mktime(time.strptime(e,dateformat))
    randomtime=sdate + randomgenerator * (edate - sdate)
    randomdate=time.strftime(dateformat,time.localtime(randomtime))
    return randomdate
print("Random date :",getrandomdate("01/01/2025","01/12/2026"))