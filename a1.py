from datetime import datetime,date,time
I= date.today()
print("Todays date is: ", I)
print("Date components are: ", str(I.day)+"-"+str(I.month)+"-"+str(I.year))
now= datetime.now()
print("Current date and time is: ", now)