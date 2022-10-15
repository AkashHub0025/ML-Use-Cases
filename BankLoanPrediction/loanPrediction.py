from imp import load_dynamic
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

# x = [1,2,3]
# y = [3,4,5]
# plt.plot(x,y)
# plt.show()

#Data preprocessing
loan_dataset = pd.read_csv("loan_dataset.csv")
print(loan_dataset.head())
print(loan_dataset.shape)
print(loan_dataset.describe())