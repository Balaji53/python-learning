sales=[2342,3243,562,343243,3532,98032]
totalsales = 0
for sale in range(len(sales)):
    totalsales += sales[sale]
    print(f'month {sale+1}:',totalsales)

for i in sales:
    print(i)
    if i > 2000:
        print(f'Month {sales.index(i)+1} : {i}has more expense and exceeds the limit')
        #break
    else:
        print(f'Month {sales.index(i) + 1}: {i} has less expense and within the limit')



