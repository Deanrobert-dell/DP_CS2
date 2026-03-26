# shape classes

class Circle:
    def __init__(self, radius):
        self.radi = radius

    def area(self): #use same  functs for all to make easier to call/use
        return round(3.14 * self.radi * self.radi, 2) #calculations 

    def circumference(self):
        return round(2 * 3.14 * self.radi, 2) #makes circumfrence
    
    def display(self):
        print(f"circle (r={self.radi})")
        print(f"Areas: {self.area()}")
        print(f"Perimeter: {self.circumference()}") 

    def big_area(self, other): #literaly justcompares are
        return self.area() > other.area()


    def longer_perim(self, other):
        return self.circumference() > other.perimeter()

    
    def formula(self):
        print("Ccircle: area = pi*r^2, perimeter = 2*pi*r")


class Triangle:
    def __init__(self, base, height, side1, side2, side3): #inputs for triangle
        self.base = base
        self.height = height
        self.s1 = side1
        self.s2 = side2
        self.s3 = side3


    def area(self):
        return round(0.5 * self.base * self.height, 2)

    def perimeter(self):
        return round(self.s1 + self.s2 + self.s3, 2)

    def display(self):
        print(f"Triangle (base={self.base})")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")

    def bigarea(self, other):
        return self.area() > other.area()

    def longer_perim(self, other):
        return self.perimeter() > other.perimeter()

    

    def formula(self):
        print("triangle: area = 1/2 * base * height")




class Rectangle:
    def __init__(self, width, height):
        self.width = width
        
        self.height = height



    def area(self):
        return round(self.width * self.height, 2)


    def perimeter(self):
        return round(2 * (self.width + self.height), 2)

    def display(self):
        print(f"Rectangle ({self.width} x {self.height})")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")

    def big_area(self, other):
        return self.area() > other.area()

    def longer_perim(self, other):
        return self.perimeter() > other.perimeter()

    

    def formula(self):
        print("rectangle: area = w*h, Perimeter = 2(w+h)")




class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return round(self.side * self.side, 2)

    def perimeter(self):
        return round(4 * self.side, 2)

    def display(self):
        print(f"Square (side={self.side})")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")

    def big_area(self, other):
        return self.area() > other.area()

    def longer_perim(self, other):
        return self.perimeter() > other.perimeter()


    def formula(self):
        print("Square: Area = s^2, Perimeter = 4s") # more equations



# helper functions

def view_shapes(shapes):
    if len(shapes) == 0:
        print("No shapes.")
    else:
        for i, s in enumerate(shapes): #get shape/indexes
            print(f"Shape #{i+1}")
            s.display()


def select_shape(shapes):
    try:
        i = int(input("Select shape #: ")) - 1
        shapes[i].display()
    except:
        print("Invalid selection.")



def compare_shapes(shapes):
    try:
        a = int(input("first shape #")) - 1 #asks for shape number minus for list index
        b = int(input("aecond shape #: ")) - 1

        if shapes[a].big_area(shapes[b]):
            print("Shape num 1 has larger area")
        else:
            print("Shape 2 has larger area")

    except:
        print("WQRONG")


def sort_shapes(shapes):
    choice = input("Sort by area(1) or perimeter(2): ")

    if choice == "1":
        shapes.sort(key=lambda x: x.area()) # sort by area
    elif choice == "2":
        shapes.sort(key=lambda x: x.perimeter())

    print("sorted i think")


def show_formulas():
    Circle.formula()
    Rectangle.formula()
    Square.formula()
    Triangle.formula()