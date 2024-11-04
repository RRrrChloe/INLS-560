menu_option = ''
while menu_option != 'q':
    print('MENU:','a: pie chart', 'b: histogram', 'c: line chart', 'q: quit ')
    menu_option = input("Enter your choice: ")
    if menu_option == 'a':
        print('pie chart')
    elif menu_option == 'b':
        print('histogram')
    elif menu_option == 'c':
        print('line chart')
