import pandas as pd

df = pd.read_csv('../data/raw/bondowoso.csv', header=None, skiprows=4)

df.columns = [
    'No', 'Nama', 'NIB', 'Tanggal_Terbit', 'Status_NIB',
    'Kekayaan_Bersih', 'Nama_Usaha', 'Sektor', 'KBLI',
    'Kegiatan_Usaha', 'Alamat_Usaha', 'Kec_Usaha', 'Telp',
    'Modal_Usaha', 'Hasil_Penjualan', 'Jumlah_Tenaga_Kerja'
]

# ambil kolom penting aja buat geocoding
df_cleaned = df[['Nama_Usaha', 'Alamat_Usaha', 'Kec_Usaha']]

# drop baris yang kosong kalau ada
df_cleaned.dropna(inplace=True)

# cek hasil cleaning sementara
print(df_cleaned.head())

# simpan hasil cleaning
df_cleaned.to_csv('../data/cleaned/bondowoso_cleaned.csv', index=False)
