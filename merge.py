"""
 Python Script:
  Combine/Merge multiple CSV files using the Pandas library
"""
import os
from glob import glob
import pandas as pdlib

# Produce a single CSV after combining all files
def produceOneCSV(list_of_files, file_out):
   # Consolidate all CSV files into one object
   result_obj = pdlib.concat([pdlib.read_csv(file) for file in list_of_files])
   # Convert the above object into a csv file and export
   result_obj.to_csv(file_out, index=False, encoding="utf-8")

# Move to the path that holds our CSV files
# csv_file_path = 'csvs/full/'
path = "csvs/full/{}.csv"
foo = ["csvs/full/full_1_10.csv","csvs/full/full_11_20.csv"] 
# os.chdir(csv_file_path)

# List all CSV files in the working dir
# file_pattern = ".csv"
# list_of_files = [file for file in glob('*.{}'.format(file_pattern))]
# print(list_of_files)

file_out = "merged.csv"

produceOneCSV(foo, file_out)