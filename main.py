import pandas as pd


class Controller:
    def __init__(self, name):
        self.name = name
        

L = Controller("Luke")

roster = [[0 for i in range(8)] for j in range(10)]

for i in range(1):
    for j in range(len(roster[i])):
        roster[i][j] = L.name

roster_df = pd.DataFrame(roster)
roster_df = roster_df.transpose()
    
print(roster_df)
