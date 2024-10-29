#  Построй диаграмму рассеяния для двух наборов случайных данных,
#  сгенерированных с помощью функции `numpy.random.rand`.
# import numpy as np
# random_array = np.random.rand(5) # массив из 5 случайных чисел
# print(random_array)


import numpy as np
import matplotlib.pyplot as plt

# Генерация двух массивов из 100 случайных чисел
x = np.random.rand(100)
y = np.random.rand(100)

# Построение диаграммы рассеяния
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', alpha=0.6)
plt.title('Диаграмма рассеяния случайно сгенерированных наборов данных')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.show()
