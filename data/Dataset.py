import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import shutil

df_heart = pd.read_csv("heart.csv")
df_heart["target"] = df_heart["output"]

df_heart.drop(["output"],inplace=True ,axis=1)

df_heart.drop_duplicates(keep="first", inplace=True)

csv_filename = "train_data.csv"
df_heart.to_csv(csv_filename, index=False)

model_dir = "../models"
data_dir = "data"

if not os.path.exists(model_dir):
    os.makedirs(model_dir)

if not os.path.exists(data_dir):
    os.makedirs(data_dir)

shutil.copy(csv_filename, os.path.join(model_dir, csv_filename))

print("Train dataseti CSV olarak kaydedildi ve model/data klasörlerine kopyalandı.")

