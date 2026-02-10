#DP 2nd movie
import csv

def search():
    print("these are the choices: \n, Genre(1) \nDirector(2) \nActor(3) \nLength (min/max) (4)")
    options = input("choose from that with number seperated by commas, (ex. 1,3 or 1,2,4)")

def main():
    print("this is th movei recomender, if you are looking for mives to watch use this!!")
    choice = input("do you want to search/get recommendations(1), print list of movies(2), or exit (3)  ")
    if choice == 1:
        search()
    elif choice == 2:
        print()
    elif choice == 3:
        break



