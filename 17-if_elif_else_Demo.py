import datetime

tarih=input("When was your car on the road (2020/8/22): ")
tarih=tarih.split("/")

currentDate=datetime.datetime.now()
dateOfOnRoad=datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))

days=currentDate-dateOfOnRoad
print(days)


days=days.days

if days<=365:
    print("1. service term")
elif days>365 and days<365*2:
    print("2. service term")
elif days>365*2 and days<365*3:
    print("3. service term")
else:
    print("wrong date")    