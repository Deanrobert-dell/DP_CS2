# shape classes

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(3.14 * self.radius * self.radius, 2)

    def circumference(self):
        return round(2 * 3.14 * self.radius, 2)

    def display(self):
        print(f"Circle (r={self.radius})")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.circumference()}")

    def has_larger_area(self, other):
        return self.area() > other.area()

    def has_longer_perimeter(self, other):
        return self.circumference() > other.perimeter()

    
    def formula(self):
        print("Circle: Area = pi*r^2, Perimeter = 2*pi*r")


class Triangle:
    def __init__(self, base, height, side1, side2, side3):
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

    def has_larger_area(self, other):
        return self.area() > other.area()

    def has_longer_perimeter(self, other):
        return self.perimeter() > other.perimeter()

    
    def formula(self):
        print("Triangle: Area = 1/2 * base * height")


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

    def has_larger_area(self, other):
        return self.area() > other.area()

    def has_longer_perimeter(self, other):
        return self.perimeter() > other.perimeter()

    @staticmethod
    def formula():
        print("Rectangle: Area = w*h, Perimeter = 2(w+h)")


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

    def has_larger_area(self, other):
        return self.area() > other.area()

    def has_longer_perimeter(self, other):
        return self.perimeter() > other.perimeter()

    def formula(self):
        print("Square: Area = s^2, Perimeter = 4s")


# helper functions

def view_shapes(shapes):
    if len(shapes) == 0:
        print("No shapes.")
    else:
        for i, s in enumerate(shapes):
            print(f"\nShape #{i+1}")
            s.display()


def select_shape(shapes):
    try:
        i = int(input("Select shape #: ")) - 1
        shapes[i].display()
    except:
        print("Invalid selection.")


def compare_shapes(shapes):
    try:
        a = int(input("First shape #: ")) - 1
        b = int(input("Second shape #: ")) - 1

        if shapes[a].has_larger_area(shapes[b]):
            print("Shape 1 has larger area")
        else:
            print("Shape 2 has larger area")

    except:
        print("Error comparing.")


def sort_shapes(shapes):
    choice = input("Sort by area(1) or perimeter(2): ")

    if choice == "1":
        shapes.sort(key=lambda x: x.area())
    else:
        shapes.sort(key=lambda x: x.perimeter())

    print("Sorted!")


def show_formulas():
    Circle.formula()
    Rectangle.formula()
    Square.formula()
    Triangle.formula()