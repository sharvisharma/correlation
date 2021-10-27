import csv
import plotly.express as px
import numpy as np


    
def createGraph():
    with open("data1.csv", newline="") as f:
        df= csv.DictReader(f)
        fig= px.scatter(df, x="Coffee",y="sleep")
        fig.show()


def getDataSource():
    coffee=[]
    sleep=[]

    with open("data1.csv", newline="") as f:
        df=csv.DictReader(f)

        for row in df:
            coffee.append(float(row["Coffee"]))
            sleep.append(float(row["sleep"]))

    return{"x":coffee, "y":sleep}

def findcorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("the correlation between sleep and coffee is : ", correlation)

def main():
    data=getDataSource()
    findcorrelation(data)
   # createGraph()

main()