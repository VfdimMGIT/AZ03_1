import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных данных
data = np.random.normal(mean, std_dev, num_samples)

# Создание гистограммы
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, edgecolor='black', alpha=0.7, density=True)

# Добавление линии плотности нормального распределения (опционально)
from scipy.stats import norm
x = np.linspace(min(data), max(data), 100)
plt.plot(x, norm.pdf(x, mean, std_dev), 'r-', linewidth=2)

# Настройка оформления
plt.title('Гистограмма нормального распределения', fontsize=14)
plt.xlabel('Значения', fontsize=12)
plt.ylabel('Плотность вероятности', fontsize=12)
plt.grid(True, alpha=0.3)

# Отображение графика
plt.show()
