import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
num_points = 50  # Количество точек
x = np.random.rand(num_points)  # Первый набор (ось X)
y = np.random.rand(num_points)  # Второй набор (ось Y)

# Создание диаграммы рассеяния
plt.figure(figsize=(10, 6))
plt.scatter(x, y, c='blue', alpha=0.6, edgecolors='w', s=80)

# Добавление заголовка и подписей осей
plt.title('Диаграмма рассеяния случайных данных', fontsize=14)
plt.xlabel('X значения', fontsize=12)
plt.ylabel('Y значения', fontsize=12)
plt.grid(True, alpha=0.3)

# Отображение графика
plt.show()
