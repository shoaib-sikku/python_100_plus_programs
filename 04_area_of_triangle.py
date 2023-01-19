print('****Calculate area of triangle****')

height = float(input('Enter the height of a Triangle: \n'))
base = float(input('Enter the base of a Triangle: \n'))

def AreaOfTri(base,height):
    return 0.5*base*height
print(f'Area of Triangle is : {AreaOfTri(base,height)}')