import sys

while True:
    fv = input('''
What file would you like to search for?:
    a) 60s-music file
    b) athletes file
    x) to exit

''')
    if fv == "a":
        fv = "60s_music.csv"
    elif fv == "b":
        fv = "athelets.csv"
    elif fv == "x":
        sys.exit()
    else:
        print("Invalid Option, enter a, b, or x.")
        continue
    
    sv = input(f'Enter the search term for {fv} file:')
    sv = sv.title()

    def find(fv,sv):
        with open(fv,'r') as f:
            c= f.read()
        if sv in c:
            print(f'Your search term {sv} exists in the {fv} file!')
            se = input('Would you like to see the entries? (y or n)?')
            if se.lower() == 'y':
                print()
                with open (fv,'r') as f:
                    for line in f:
                        if sv in line:
                            print(line.strip())
            elif se.lower() == 'n':
                print('Good Bye!')
                sys.exit()
            else:
                print("Invalid option enter y or n")
        else:
            print(f'{sv} does not exist in file {fv}')
    find(fv,sv)