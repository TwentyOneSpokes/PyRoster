import pandas as pd


class Controller:
    def __init__(self, name):
        self.name = name
        

L = Controller("Luke")

roster = [[0 for i in range(8)] for j in range(10)]

roster_df = pd.DataFrame(roster)
    
print(roster_df)
