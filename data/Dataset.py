import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_heart = pd.read_csv("heart.csv")
df_heart["target"] = df_heart["output"]

df_heart.drop(["output"],inplace=True ,axis=1)

df_heart.drop_duplicates(keep="first", inplace=True)

df_heart.to_csv("data/train_data.csv", index=False)
df_heart.to_csv("model/train_data.csv", index=False)
df_heart.to_csv("reports/train_data.csv", index=False)


