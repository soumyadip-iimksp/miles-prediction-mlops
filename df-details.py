import pandas as pd
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the sting to be used")
parser.parse_args()

df = pd.read_csv("auto-mpg.csv")
print(df.head())
