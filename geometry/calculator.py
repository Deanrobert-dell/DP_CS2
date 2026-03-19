from helpers import *





def display_menu():
    #displays the main menu
    print("\n Gemotry calculator ")
    print("1 Create new chape") #options of shapes mand makes
    print("2 view all shapes") #prints shapes
    print("3 select shape") #views specific detailes
    print("4 compare shapes") #compare based on area or othre details
    print("5 sort the shapes") #sorted by area
    print("6 formula guide") #equaions for each shape
    print("7 QUIT") #leaves program


def main():
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            shape = input("rectangle(1) triangle(2) circle(3)")
            if shape == "1":
                print("You have created a rectangle.")
            elif shape == "2":
                print("You have created a triangle.")
            elif shape == "3":
                print("You have created a circle.")
            else:
                print("Invalid shape.")

        elif choice == "2":
            
                
        elif choice == "3":
            
                
        elif choice == "4":
            
                
        elif choice == "5":
            
                
        elif choice == "6":
            
                
        elif choice == "7":
            print("beebye")
            break
            
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


main()