csvString = input("Enter csv string")

csvList = csvString.split(",")

csvTuple = tuple(csvList)

print(csvList,csvTuple)