menu_option = ''
while menu_option != 'q':
    print(f'''
Shop information FAQS:
a: pie chart
b: histogram
c: line chart
q: quit
''')
    
    menu_option = input("Enter your choice: ")
    if menu_option == 'a':
        print('pie chart')
    elif menu_option == 'b':
        print('histogram')
    elif menu_option == 'c':
        print('line chart')
        data = input('Is your data fit line chart? enter (y or n): ')
        if data == 'y':
            print("Awesome! This is a right track!")
        else:
            print("You need to choose other options!")
