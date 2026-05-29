import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Стиль
sns.set_style("whitegrid")

# 1. Линейный график (Matplotlib)
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.figure(figsize=(8,4))
plt.plot(x, y, label='sin(x)', color='blue', linewidth=2)
plt.title('Пример синусоиды')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()
plt.show()

# 2. Гистограмма и KDE (Seaborn)
data = np.random.normal(0, 1, 500)
sns.histplot(data, bins=30, kde=True, color='green')
plt.title('Гистограмма нормального распределения')
plt.show()

# 3. Scatter plot с регрессией
df = pd.DataFrame({'x': np.random.rand(50)*10, 'y': np.random.rand(50)*10 + np.random.randn(50)*2})
sns.lmplot(data=df, x='x', y='y', height=4, aspect=1.5)
plt.title('Диаграмма рассеяния с линейной регрессией')
plt.show()