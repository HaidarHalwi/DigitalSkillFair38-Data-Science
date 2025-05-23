# -*- coding: utf-8 -*-
"""Tugas_Day3_KapalTitanic.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LW_gLgbVHztrd24L3NZir5QTK9jUiShW
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

# import data
df = pd.read_excel('titanic.xlsx')
df.head()

"""# **Lihat head, tail, sample, dan info**"""

# Lihat 5 baris pertama
print("=== HEAD ===")
display(df.head())

# Lihat 5 baris terakhir
print("\n=== TAIL ===")
display(df.tail())

# Ambil sample acak
print("\n=== SAMPLE ===")
display(df.sample(5, random_state=42))

# Info lengkap
print("\n=== INFO ===")
df.info()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Agar grafik tampil lebih cantik
sns.set(style="whitegrid", palette="pastel")
plt.rcParams["figure.figsize"] = (8, 5)

# Import data
df = pd.read_excel('titanic.xlsx')

# Lihat 5 baris pertama
print("=== HEAD ===")
display(df.head())

# Lihat 5 baris terakhir
print("\n=== TAIL ===")
display(df.tail())

# Ambil sample acak
print("\n=== SAMPLE ===")
display(df.sample(5, random_state=42))

# Info lengkap
print("\n=== INFO ===")
df.info()

# Visualisasi 1: Perbandingan jumlah yang selamat vs tidak
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='survived')
plt.title("Jumlah Penumpang Selamat vs Tidak Selamat")
plt.xticks([0, 1], ['Tidak Selamat', 'Selamat'])
plt.ylabel("Jumlah Penumpang")
plt.xlabel("")
plt.tight_layout()
plt.show()

# Visualisasi 2: Distribusi umur
plt.figure(figsize=(6, 4))
sns.histplot(df['age'].dropna(), bins=20, kde=True)
plt.title("Distribusi Umur Penumpang Titanic")
plt.xlabel("Umur")
plt.ylabel("Jumlah")
plt.tight_layout()
plt.show()

# Visualisasi 3: Kelangsungan Hidup berdasarkan Jenis Kelamin
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='sex', hue='survived')
plt.title("Kelangsungan Hidup Berdasarkan Jenis Kelamin")
plt.xticks(rotation=0)
plt.legend(title='Survived', labels=['Tidak', 'Ya'])
plt.ylabel("Jumlah Penumpang")
plt.tight_layout()
plt.show()

"""# **Observasi awal dan Statistik Ringkasan**"""

# Statistik Ringkasan Data Numerik
print("\n=== STATISTICAL SUMMARY (NUMERIK) ===")
display(df.describe())

# Statistik Ringkasan Data Kategorik
print("\n=== STATISTICAL SUMMARY (KATEGORIK) ===")
display(df.describe(include='object'))

"""# **Cek duplikat dan menghapusnya jika ada**"""

# Cek jumlah duplikat
duplicates = df.duplicated().sum()
print(f"\nJumlah duplikat: {duplicates}")

# Jika ada, hapus duplikat
if duplicates > 0:
    df = df.drop_duplicates()
    print("Duplikat dihapus.")

"""#**Cek Missing Values & Persentasenya**"""

# Cek missing value per kolom
print("\n=== MISSING VALUE CHECK ===")
missing = df.isnull().sum()
percent_missing = (df.isnull().sum() / len(df)) * 100

missing_df = pd.DataFrame({
    'Total Missing': missing,
    'Persentase (%)': percent_missing
})
display(missing_df[missing_df['Total Missing'] > 0])

"""# **Penanganan Missing Value (contoh)**"""

# Contoh penanganan (silakan disesuaikan setelah kamu lihat datanya)
# Misal isi missing "Age" dengan median
if 'age' in df.columns:
    df['age'].fillna(df['age'].median(), inplace=True)

# Misal drop baris yang missing pada kolom 'Embarked'
if 'Embarked' in df.columns:
    df.dropna(subset=['Embarked'], inplace=True)

# Visualisasi distribusi umur
sns.histplot(df['age'], kde=True)
plt.title("Distribusi Umur Penumpang")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Menampilkan statistik deskriptif lengkap
print("=== DESCRIPTIVE STATISTICS ===")
display(df.describe(include='all'))

# Statistik spesifik kolom 'age'
mean_age = df['age'].mean()
min_age = df['age'].min()
max_age = df['age'].max()

print(f"\nUmur Rata-rata: {mean_age:.2f} tahun")
print(f"Umur Termuda: {min_age} tahun")
print(f"Umur Tertua: {max_age} tahun")

# Visualisasi 1: Distribusi Umur
plt.figure(figsize=(6, 4))
sns.histplot(df['age'].dropna(), bins=20, kde=True, color='skyblue')
plt.axvline(mean_age, color='red', linestyle='--', label=f'Rata-rata: {mean_age:.1f}')
plt.title("Distribusi Umur Penumpang Titanic")
plt.xlabel("Umur")
plt.ylabel("Jumlah")
plt.legend()
plt.tight_layout()
plt.show()

# Visualisasi 2: Distribusi Jenis Kelamin
plt.figure(figsize=(5, 4))
sns.countplot(data=df, x='sex', palette='Set2')
plt.title("Distribusi Penumpang Berdasarkan Jenis Kelamin")
plt.xlabel("Jenis Kelamin")
plt.ylabel("Jumlah")
plt.tight_layout()
plt.show()

# Visualisasi 3: Persentase Penumpang Selamat vs Tidak
plt.figure(figsize=(5, 4))
survived_counts = df['survived'].value_counts()
plt.pie(survived_counts, labels=['Tidak Selamat', 'Selamat'], autopct='%1.1f%%', colors=['#ff9999','#66b3ff'])
plt.title("Persentase Keselamatan Penumpang")
plt.tight_layout()
plt.show()

df.isnull().sum()
df.isnull().mean() * 100

import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
# Contoh imputasi dengan median
df['age'].fillna(df['age'].median(), inplace=True)

plt.title("Peta Missing Values")
plt.show()

