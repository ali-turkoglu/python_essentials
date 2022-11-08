# there are some classes like date, time, datetime

import datetime
from datetime import datetime
# from datetime import date
# from datetime import time


# result1=dir(datetime)
# result2=dir(datetime.datetime)
# result3=dir(datetime.date)
# result4=dir(datetime.time)

# print(result1,"\n###################")
# print(result2,"\n###################")
# print(result3,"\n###################")
# print(result4,"\n###################")

simdi = datetime.now()
result=simdi.year 
result=simdi.month 
result=simdi.day
result=simdi.hour 
result=simdi.minute
result=simdi.second

print(datetime.ctime(simdi))

########################################################

result=datetime.strftime(simdi,"%Y")
result=datetime.strftime(simdi,"%X")
result=datetime.strftime(simdi,"%D")
result=datetime.strftime(simdi,"%A")
result=datetime.strftime(simdi,"%B")
result=datetime.strftime(simdi,"%Y %B %A")

###################################################

t="23 April 2002"
gun, ay, yil=t.split(" ")
print(gun)
print(ay)
print(yil)

t = "13 june 1999 hour 22:33:21"
dt = datetime.strptime(t,'%d %B %Y hour %H:%M:%S')
print(dt)


