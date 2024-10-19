import pandas as pd

# Pengaturan tampilan Pandas
pd.set_option('display.max_rows', None)       # Menampilkan semua baris
pd.set_option('display.max_columns', None)    # Menampilkan semua kolom
pd.set_option('display.width', 1000)          # Mengatur lebar tampilan
pd.set_option('display.max_colwidth', None)   # Mengatur lebar maksimum kolom

# Baca dataset
df = pd.read_csv('songs_normalize.csv')

# Tampilkan DataFrame
print(df)
