row = int(input("Enter row"))
col = int(input("Enter col"))

array = []

for i in range(0,row):
    temp = []
    for j in range(0,col):
        val = i*j
        temp.append(val)
    array.append(temp)

print(array)
