import pandas
import os

dir_path = os.path.realpath("challengeCSV/Appeals_Filed_In_2017.csv")
data = pandas.read_csv(dir_path)

def getColumnNames():
    '''
    Get the names of each column values
    Also sort them in alphabetical order
    '''
    return sorted(data.columns.values.tolist())

def getRowAmount():
    '''
    Get the total number of rows in the CSV
    '''
    return len(data.index)

def addition():
    '''
    Add a new column to the CSV computed from two other column values
    For this CSV it is Acronym-Exam No. in that format
    '''
    data["Acronym-Appeal Type"] = data["Acronym"] + "-" + data["Appeal Type"]
    data.to_csv("challenge1.csv", index=False)

def challenge():
    print(getColumnNames())
    print(getRowAmount())
    addition()