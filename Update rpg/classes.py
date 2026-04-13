from faker import Faker
import random
import pandas as pd

import matplotlib.pyplot as plt

fake = Faker()

#change for commit
class DataVisualization:

    def __init__(self, stats_dict):
        # global stats
        self.df = pd.DataFrame.from_dict(stats_dict, orient='index')

    def show_bar_chart(self, character_name):
        if character_name not in self.df.index:

            print("Character si not found")
            return

        char = self.df.loc[character_name]
##
        # Only numeric stats
        numeric_stats = char.select_dtypes(include='number')

        numeric_stats.plot(kind='bar')
        plt.title(f"{character_name} Stats")

        plt.ylabel("Value")
        plt.show()

    def compare_characters(self, names):
        subset = self.df.loc[names]

        subset[["strength", "dexterity",  "intelligence", "wisdom"]].plot(kind='bar')
        plt.title("Character Comparison")

        plt.show()



class StatisticalAnalyzer:

    def __init__(self, stats_dict):
        self.df = pd.DataFrame.from_dict(stats_dict, orient='index')
#
    def basic_stats(self):
        print("BASE sTATS")
        print("mean:\n", self.df.mean(numeric_only = True))
        print("\nMax:\n", self.df.max(numeric_only=True))
        print("\nMin:\n", self.df.min(numeric_only=True))

    def strongest_character(self):
        if "strength" not in self.df.columns:
            print("No strengths stat found")
            return
        
        strongest = self.df["strength"].idxmax()
        print(f"Strongest characters: {strongest}")


    def sort_by_stat(self, stat):
        if stat not in self.df.columns:
            print("invalid stat")
            return
        
        print(self.df.sort_values(by=stat, ascending=False))



class RandomGenerator:

    def quest(self):
        actions = ["retrieve", "protect", "deliver", "investigate", "defeat"]
        objects = ["artifact", "message", "treasure", "weapon", "secret"]
        places = ["ancient ruins", "haunted forest", "lost city", "dungeon", "kingdom"]

        return f"your quest is to {random.choice(actions)} a {random.choice(objects)} from the {random.choice(places)}."

    def backstory(self):
        return f"{fake.name()} was born in {fake.city()} and worked as a {fake.job()}. Now seeks adventuress"

    def name(self):
        return fake.name()
