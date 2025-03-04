t=float(input("Enter the num:"))
print("the number is even" if t%2 == 0 else "the number is odd")

expenses = [2600,3200,5400,8700,"dosa"]
total = 0
for e in range(len(expenses)):
    ex = expenses[e]
    print(f"month{e+1}:expense{ex}")
    #total +=ex
print(total)

#enumerate functions

i=[(ins,exp) for ins,exp in enumerate(expenses)]
print(i)
print(type(i))

#break and zip function

sal = [68,98,23,55,30,58,36]
mon=['jan','feb','mar','apr','may']
target = 35

for  sal,mon in zip(sal,mon):
    if sal > 30 :
        print(f"{mon} target is achieved")
    else:
        print(f"{mon} target is not achieved")




