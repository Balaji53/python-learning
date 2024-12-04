print("hello")

mnc = ['Google', 'Facebook', 'Microsoft', 'paypal']
service = ['Accenture', 'Infosys', 'IBM', 'TCS']
startups = ['Swiggy', 'zomato', 'Zepto', 'zerodha']

company = input("enter the company name to search :")

if company in mnc:
    print(f'{company} is an MNC')
elif company in service:
    print(f'{company} is an service')
elif company in startups:
    print(f'{company} is an startup')
else:
    print("not listed in company list")

print(f'{company} is MNC' if company in mnc else f'{company} is a service'
if company in service else f'{company} is a startup' if company in startups else f'company not listed in the list')
