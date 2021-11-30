# PUTF21 Final Project - Rebecca Bang

from time import sleep
import pandas as pd
import os

path2 = os.path.dirname(os.path.realpath(__file__))
df = pd.read_csv(path2 + '/data/wines.csv' , encoding='utf8')

class WineList(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(
                WineList, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def pick_wine(self, wine_type):
        return Wine.pick_wine(wine_type)

class Wine(object):
    def __init__(self, num):
        self.num = num

    def name1(self):
        col = df['name1'].fillna('Unavailable')
        return col[self.num]

    def name2(self):
        col = df['name2'].fillna('Unavailable')
        return col[self.num]

    def country(self):
        col = df['country'].fillna('Unavailable')
        return col[self.num]

    def region(self):
        col = df['region'].fillna('Unavailable')
        return col[self.num]

    def year(self):
        col = df['year'].fillna('Unavailable')
        return col[self.num]

    def price(self):
        col = df['price'].fillna('Unavailable')
        return col[self.num]

    def currency(self):
        col = df['currency']
        return col[self.num]

    def desc(self):
        print(f"{__class__.name1(self):<20}{__class__.name2(self)}")
        sleep(0.5)
        print(f"{'Country/Region':<20}{__class__.country(self)}{' / '}{__class__.region(self)}")
        sleep(0.5)
        print(f"{'Year':<20}{__class__.year(self)}")
        sleep(0.5)
        print(f"{'Price':<20}{__class__.price(self)} {__class__.currency(self)}\n")
        sleep(0.5)

    @staticmethod
    def pick_wine(option):
        while True:
            print(f"{'=' * 50}\n"+"-- List of wines --\n")
            df2 = df[['id','name1']]
            print(df2.to_string(index=False, header=None))
            inp = input("\n(Press 'q' to quit)\nEnter your selection: ")
            if inp == 'q':
                break
            else:
                print(f"{'=' * 50}\n")
                selection = int(inp)-1
                result = Wine(selection)
                result.desc()

def main():
    while True:
        print(f"{'=' * 50}\n"+"-- List of wines --\n")
        df2 = df[['id','name1']]
        print(df2.to_string(index=False, header=None))
        inp = input("\n(Press 'q' to quit)\nEnter your selection: ")
        if inp == 'q':
            break
        else:
            print(f"{'=' * 50}\n")
            selection = int(inp)-1
            result = Wine(selection)
            result.desc()

if __name__ == "__main__":
    main()
