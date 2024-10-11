import datetime


myhour = datetime.date.today().ctime()
mytime = datetime.date.today()
# print(str(myhour) + " " + str(mytime))
print(myhour)
now = datetime.datetime.now()

print("The current time is:", now.time())
