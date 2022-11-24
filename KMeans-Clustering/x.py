import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

siswa = pd.read_csv("../data_nilai_without_name.csv");
after_remove = siswa.drop(['Nama'],axis=1)
