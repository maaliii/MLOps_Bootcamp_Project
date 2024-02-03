import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)


df_heart=pd.read_csv("train_data.csv")

x = df_heart.drop("target", axis=1)
y = df_heart["target"]

x_train, x_test, y_train, y_test = train_test_split(x,
                                                    y,
                                                    test_size=0.2,
                                                    random_state=42)

np.random.seed(42)
model_2 = RandomForestClassifier()
model_2.fit(x_train, y_train)
model_2.score(x_test, y_test)



y_pred = model_2.predict(x_test)
y_pred