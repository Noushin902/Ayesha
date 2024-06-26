def Rectangle_Perimeter(l,w): return 2*(l+w)
def Rectangle_Area(l,w): return (l*w)

def Circle_Perimeter(r): return (2*3.1416*r)
def Circle_Area(r): return 3.1416*r**2

def Parallelogram_Perimeter(h,b): return 2*(h+b)
def Parallelogram_Area(h,b): return (h*b)

def Trapezoid_Perimeter(a,b,c,d): return a+b+c+d
def Trapezoid_Area(a,b,h): return 0.5*(a+b)*h

def Triangle_Perimeter(a,b,c): return a+b+c 
def Triangle_Area(b,h): return (b*h)/2

def Cylinder_Area(r,h): return (3.1416*r + 2*3.1416*r*h)
def Cylinder_Volume(r,h): return 3.1416*r*h

def Cone_Area(r,s): return (3.1416*r**2 + 3.1416*r*s)
def Cone_Volume(r,h): return (3.1416*r**2*h)/3


s = int(input("Enter\n1 for Rectangle\n2 for Circle\n3 for Parallelogram\n4 for Trapezoid\n5 for Triangle\n6 for Cylinder\n7 for Cone\n"))
if(s==1): 
    l,w = map(int, input("Enter length and width : ").split())
    print(f"Perimeter of rectangle : {Rectangle_Perimeter(l,w)}")
    print(f"Area of rectangle : {Rectangle_Area(l,w)}")
elif(s==2): 
    r = int(input("Enter radius : "))
    print(f"Perimeter of circle : {Circle_Perimeter(r)}")
    print(f"Area of circle : {Circle_Area(r)}")
elif(s==3): 
    h,b = map(int, input("Enter height and base : ").split())
    print(f"Perimeter of parallelogram : {Parallelogram_Perimeter(h,b)}")
    print(f"Area of parallelogram : {Parallelogram_Area(h,b)}")
elif(s==4): 
    a,b,c,d = map(int, input("Enter 4 side lengths").split())
    print(f"Perimeter of trapezoid : {Trapezoid_Perimeter(a,b,c,d)}")
    print(f"Area of trapezoid : {Trapezoid_Area(a,b,c,d)}")
elif(s==5):
    a,b,c = map(int, input("Enter 3 side lengths : ").split())
    print(f"Perimeter of triangle : {Triangle_Perimeter(a,b,c)}")
    print(f"Area of triangle : {Triangle_Area(a,b,c)}")
elif(s==6): 
    r,h = map(int, input("Enter radius and hight : ").split())
    print(f"Area of cylinder : {Cylinder_Area(r,h)}")
    print(f"Volume of cylinder : {Cylinder_Volume(r,h)}")
else:
    r,s = map(int, input("Enter radius and side : ").split())
    r,h = map(int, input("Enter radius and hight : ").split())
    print(f"Area of cone : {Cone_Area(r,s)}")
    print(f"Volume of cone : {Cone_Volume(r,h)}")