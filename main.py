import pandas as pd

sep = '\n' + '_' * 100 + '\n'

# Создаем DataFrame с данными
data = {
    'Имя': ['Анна', 'Борис', 'Виктор', 'Галина', 'Дмитрий', 'Елена', 'Женя', 'Зоя', 'Иван', 'Ксения'],
    'Математика': [5, 4, 3, 5, 4, 5, 3, 4, 5, 4],
    'Русский язык': [4, 5, 4, 3, 5, 4, 5, 3, 4, 5],
    'Физика': [5, 3, 4, 4, 3, 5, 4, 3, 5, 4],
    'Химия': [4, 4, 5, 3, 4, 5, 3, 4, 4, 5],
    'История': [3, 5, 4, 5, 4, 3, 5, 4, 4, 3]
}

df = pd.DataFrame(data)

print(f'2.\n{df.head()}', end=sep)

print(f'3. Средняя оценка по предметам:\n{df.mean(numeric_only=True).to_string()}', end=sep)

print(f'4. Медианная оценка по предметам:\n{df.median(numeric_only=True).to_string()}', end=sep)

Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR = Q3_math - Q1_math
print(f'5.1 Q1_math - {Q1_math}\n'
      f'5.2 Q3_math - {Q3_math}\n'
      f'5.3 IQR - {IQR}', end=sep)

print(f"6. Стандартное отклонение:\n{df.std(numeric_only=True).to_string()}", end=sep)
