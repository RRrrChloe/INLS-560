MAX_Years_Sales = 10
MAX_price =30

years_sales = int(input("Enter your hourse sales years: "))
price = int(input('Enter your hourse price:  '))

if years_sales < MAX_Years_Sales and price < MAX_price:
    print('The hourse is valued.')
else:
    print(f'''
    With the year used of
    {MAX_Years_Sales} and the max price of {MAX_price}
s
''')