import pandas as pd
from os import listdir
from os.path import isfile, join

mypath = "tmp_csvs/"

# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

def merge(file1, file2, output_name):
    """Read two CSV as dataframe"""
    a = pd.read_csv(file1)
    b = pd.read_csv(file2)

    """Join the DataFrame"""
    new_file = a.join(b, lsuffix="_left", rsuffix="_right")

    """Save the Pandas Dataframe to a CSV file"""
    new_file.to_csv(output_name, index=False)





