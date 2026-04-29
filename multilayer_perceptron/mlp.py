import matplotlib.pyplot as pl
import numpy as np
import warnings
import sys
import pandas as pd

def parse():
    options = ["--dataset", "--training", "--predict"]
    if len(sys.argv) < 2 or sys.argv[1] not in options:
        raise Exception("Error: Wrong usage, this program has three options:\n \
	1. \'--dataset\' -> It will take the second argument (.csv) and split in train.csv and test.csv.\n \
	2. \'--training\' -> It will train the model using trains.csv\n \
	3. \'--predict\' -> It will make predictions using test.csv by default or the third argument(.csv) and put all them in a results.csv file")


if __name__ == '__main__':
    try:
        parse()
    except Exception as e:
        print(e)