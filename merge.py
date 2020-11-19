import pandas as pd

def f_1_20():
    """Read two CSV as dataframe"""
    data_1_10= pd.read_csv('csvs/full/full_1_10.csv')
    data_11_20 = pd.read_csv('csvs/full/full_11_20.csv')

    """Join the DataFrame"""
    new_file = data_1_10.join(data_11_20, lsuffix="_left", rsuffix="_right")

    """Save the Pandas Dataframe to a CSV file"""
    new_file.to_csv('1_20.csv', index=False)


def f_21_40():
    data_21_30= pd.read_csv('csvs/full/full_21_30.csv')
    data_31_40 = pd.read_csv('csvs/full/full_31_40.csv')

    """Join the DataFrame"""
    new_file = data_21_30.join(data_31_40, lsuffix="_left", rsuffix="_right")

    """Save the Pandas Dataframe to a CSV file"""
    new_file.to_csv('21_40.csv', index=False)



def f_all():
    data_1_20 = pd.read_csv('1_20.csv')
    data_21_40 = pd.read_csv('21_40.csv')
    new_file = data_1_20.join(data_21_40, lsuffix="_left", rsuffix="_right")
    new_file.to_csv('full_1_40.csv', index=False)


f_1_20()
f_21_40()
f_all()