import pandas as pd
import os

dir_files = os.listdir('.')
user_files = [file for file in dir_files if str('jerwin') in file]

df = pd.read_csv(user_files[2])
time = df['Time']
value = df['Value']
