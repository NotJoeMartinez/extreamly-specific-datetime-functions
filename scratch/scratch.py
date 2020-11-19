import pandas as pd

"""Read two CSV as dataframe"""
name = pd.read_csv('test_csvs/name.csv')
job = pd.read_csv('test_csvs/job.csv')

"""Join the DataFrame"""
new_file = name.join(job, lsuffix="_left", rsuffix="_right")

"""Save the Pandas Dataframe to a CSV file"""
new_file.to_csv('new_file.csv', index=False)


