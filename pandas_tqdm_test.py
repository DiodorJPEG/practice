import pandas as pd
import numpy as np
from tqdm import tqdm
import time

df = pd.DataFrame({'values': np.random.rand(1000)})

#Ну в общем тут прогресс бар подсчёта квадратов
squared = []
for val in tqdm(df['values'], desc="Прогресс рассчёта"):
    squared.append(val ** 2)
    time.sleep(0.002)

df['squared'] = squared
print(df.head())