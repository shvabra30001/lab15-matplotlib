import os
import matplotlib
matplotlib.rcParams["font.family"] = "DejaVu Sans"
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

os.makedirs("images", exist_ok=True)

# Задание 1. Первый линейный график
plt.figure()
days = list(("Пн", "Вт", "Ср", "Чт", "Пт"))
work = list((2, 3.5, 7, 5, 9))
plt.plot(days, work, "o-", color="steelblue", label="Сложность задач")
plt.xlabel("День недели")
plt.ylabel("Сложность")
plt.title("Сложность задач по дням")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("images/plot1.png", dpi=150)
plt.close()

# Задание 2. Точечная диаграмма: донаты и уровень
plt.figure()
np.random.seed(42)
level = np.random.randint(1, 100, 60)
donates = level * 15 + np.random.normal(0, 200, 60)
plt.scatter(level, donates, alpha=0.6, color="seagreen")
plt.xlabel("Уровень игрока")
plt.ylabel("Сумма донатов, руб.")
plt.title("Зависимость донатов от уровня")
plt.grid(True, alpha=0.3)
plt.savefig("images/scatter_donates.png", dpi=150)
plt.close()

# Задание 3. Столбчатая диаграмма: игроки по классам
plt.figure()
classes = list(("Воин", "Маг", "Стрелок", "Паладин"))
counts = list((14, 9, 11, 6))
plt.bar(classes, counts, color=list(("#4C72B0", "#DD8452", "#55A868", "#C44E52")))
plt.xlabel("Класс персонажа")
plt.ylabel("Количество игроков")
plt.title("Распределение игроков по классам")
plt.savefig("images/bar_classes.png", dpi=150)
plt.close()

# Задание 4. Гистограмма: распределение случайных чисел
plt.figure()
np.random.seed(7)
times = np.random.normal(loc=120, scale=25, size=500)
plt.hist(times, bins=30, color="steelblue", edgecolor="black")
plt.xlabel("Время выполнения, мс")
plt.ylabel("Количество задач")
plt.title("Распределение времени выполнения задач")
plt.savefig("images/hist_times.png", dpi=150)
plt.close()
print("Среднее:", times.mean().round(1))
print("Минимум:", times.min().round(1))
print("Максимум:", times.max().round(1))

# Задание 5. Несколько графиков: subplots
np.random.seed(42)
x = np.arange(1, 21)
y = x * 3 + np.random.normal(0, 10, 20)
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
ax1, ax2 = axes
ax1.plot(x, y, "o-")
ax1.set_title("Линейный график")
ax1.set_xlabel("Время")
ax1.set_ylabel("Значение")
ax2.scatter(x, y, color="crimson")
ax2.set_title("Точечная диаграмма")
ax2.set_xlabel("Время")
ax2.set_ylabel("Значение")
plt.tight_layout()
plt.savefig("images/subplots.png", dpi=150)
plt.close()

# Задание 7 (Бонус). График из Pandas
if os.path.exists("dataset.csv"):
    plt.figure()
    df = pd.read_csv("dataset.csv")
    class_counts = df["klass"].value_counts()
    plt.bar(class_counts.index, class_counts.values, color="slateblue")
    plt.xlabel("Класс")
    plt.ylabel("Количество")
    plt.title("Игроки по классам (из Pandas)")
    plt.savefig("images/pandas_bar.png", dpi=150)
    plt.close()
