from helpers import *


def display_menu():
    #displays the main menu
    print(" Gemotry calculator ")
    print("1 Create new chape") #options of shapes mand makes
    print("2 view all shapes") #prints shapes
    print("3 select shape") #views specific detailes
    print("4 compare shapes") #compare based on area or othre details
    print("5 sort the shapes") #sorted by area
    print("6 formula gsuide") #equaions for each shape
    print("7 QUIT") #leaves program

def show_formulas(shapes):
    if len(shapes) == 0:
        print("No shapes created yet.")
    else:
        for s in shapes:
            s.formula()



def main():
    shapes = []  # store shapes
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            shape = input("rectangle(1) triangle(2) circle(3) square(4): ")
            
            if shape == "1":
                try:
                    w = float(input("width: "))
                    h = float(input("height: "))
                    if w > 0 and h > 0:
                        shapes.append(Rectangle(w, h))
                        print("You have created a rectangle.")
                except:
                    print("Invalid input.")

            elif shape == "2":
                try:
                    b = float(input("base: "))
                    h = float(input("height: "))
                    s1 = float(input("side1: "))
                    s2 = float(input("side2: "))
                    if b > 0 and h > 0:
                        shapes.append(Triangle(b, h, s1, s2, b))
                        print("You have created a triangle.")
                except:
                    print("Invalid input.")

            elif shape == "3":
                try:
                    r = float(input("radius: "))
                    if r > 0:
                        shapes.append(Circle(r))
                        print("You have created a circle.")
                except:
                    print("Invalid input.")

            elif shape == "4":
                try:
                    s = float(input("side: "))
                    if s > 0:
                        shapes.append(Square(s))
                        print("You have created a square.")
                except:
                    print("Invalid input.")
            
            else:
                print("Invalid shape.")

        elif choice == "2":
            view_shapes(shapes)

        elif choice == "3":
            select_shape(shapes)

        elif choice == "4":
            compare_shapes(shapes)

        elif choice == "5":
            sort_shapes(shapes)

        elif choice == "6":
            show_formulas(shapes)

        elif choice == "7":
            print("beebye")
            break
            
        else:
            print("Invalid choice. Please select 1-7.")


main()