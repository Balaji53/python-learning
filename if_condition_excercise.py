height=float(input("Enter the height :"))
weight = float(input("Enter the weight :"))
BMI = (weight)/((height/100)**2)

#first excercise
if BMI >= 30:
    print("obesity")
    print(BMI)
elif BMI > 25 and BMI <= 29 :
    print('overweight')
    print(BMI)
elif BMI > 18.5 and BMI <= 25:
    print(BMI)
    print('Normal')
elif BMI <= 18.5:
    print('Underweight')
    print(BMI)

#second excecise

India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
USA = ["New York","Chicago","Las Vegas", "San Francisco"]
UK = ["London", "Manchester", "Liverpool", "Nottingham"]

city1 = input("Enter the name of the city")
city2 = input("Enter the name of the city")

if city1 in India and city2 in India:
    print(f'{city1} and {city2} is in India')
elif city1 in India and city2 in USA:
    print(f'{city1} and {city2} is in USA')
elif city1 in India and city2 in UK:
    print(f'{city1} and {city2} is in UK')
else:
    print(f"cities is not in the country")