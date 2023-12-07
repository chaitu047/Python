from datetime import date

print("Enter date in yyyy/MM/dd format")

startDateStr = input("Enter start date")
datelist = startDateStr.split("/")
year = int(datelist[0])
month = int(datelist[1])
day = int(datelist[2])
startDate = date(year,month,day)


endDateStr = input("Enter end date")
datelist = endDateStr.split("/")
year = int(datelist[0])
month = int(datelist[1])
day = int(datelist[2])
endDate = date(year,month,day)

datediff = endDate - startDate

print(datediff.days)