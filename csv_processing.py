import pandas as pd
import matplotlib.pyplot as plt

# Анализ данных из CSV
df = pd.read_csv('divan_prices_20250628_224315.csv')

# Преобразование цен в числа (уже выполнено pandas)
# Просто удаляем строки с нечисловыми значениями
df = df[pd.to_numeric(df['Цена'], errors='coerce').notna()]

# Расчет средней цены
mean_price = df['Цена'].mean()
print(f'Средняя цена: {mean_price:.2f} руб.')

# Построение гистограммы
plt.figure(figsize=(12, 6))
plt.hist(df['Цена'], bins=20, color='skyblue', edgecolor='black')
plt.title('Распределение цен на диваны', fontsize=14)
plt.xlabel('Цена (руб.)', fontsize=12)
plt.ylabel('Количество', fontsize=12)
plt.grid(axis='y', alpha=0.3)
plt.axvline(mean_price, color='red', linestyle='--', label=f'Средняя: {mean_price:.0f} руб.')
plt.legend()
plt.show()
