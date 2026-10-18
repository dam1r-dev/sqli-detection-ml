"""
Удаляет дубликаты SQL-запросов из датасета.
Использование: python src/dedupe.py data/raw.csv data/clean.csv
Ожидаются колонки: query, label
"""
import sys
import pandas as pd

src, dst = sys.argv[1], sys.argv[2]
df = pd.read_csv(src)
before = len(df)

# нормализация: регистр и лишние пробелы
df["_norm"] = df["query"].astype(str).str.lower().str.split().str.join(" ")
df = df.drop_duplicates(subset="_norm").drop(columns="_norm")

# запросы, попавшие в оба класса сразу, подозрительны
print(f"Было: {before}, стало: {len(df)}, удалено: {before - len(df)}")
print(df["label"].value_counts())
df.to_csv(dst, index=False)
