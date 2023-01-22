print('****Convert Kilo to Miles Program****')

con = int(input('press 1 for kilometer to miles conversion \npress  2 for miles to kilometer conversion: \n'))

if con==1:
    kilo = float(input('enter the kilometer: \n'))
    print(f'{kilo * 0.62137119} miles')
elif con==2:
    miles = float(input('enter the miles: \n'))
    print(f'{miles * 1.60934} kilometer')
else:
    print('you enter wrong input')