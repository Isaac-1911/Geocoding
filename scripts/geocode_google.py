import pandas as pd
import googlemaps
import time
import os
from config import API_KEY

# ========== Konfigurasi ==========
INPUT_FILE = '../data/cleaned/bondowoso_cleaned.csv'
OUTPUT_FILE = '../data/geocoded/bondowoso_google_200.csv'
LOG_FOLDER = '../logs'

# ========== Setup ==========
os.makedirs('../data/geocoded', exist_ok=True)
os.makedirs(LOG_FOLDER, exist_ok=True)

# Inisialisasi Google Maps API
gmaps = googlemaps.Client(key=API_KEY)

# Baca 200 data pertama
df = pd.read_csv(INPUT_FILE, on_bad_lines='skip').head(200)

# Tambah kolom kosong
df['Latitude'] = None
df['Longitude'] = None

# Proses satu per satu
for idx, row in df.iterrows():
    alamat = str(row['Alamat_Usaha']).strip().title() + ", Bondowoso"
    
    try:
        result = gmaps.geocode(alamat)
        if result:
            lokasi = result[0]['geometry']['location']
            df.at[idx, 'Latitude'] = lokasi['lat']
            df.at[idx, 'Longitude'] = lokasi['lng']
            print(f"[✅] {alamat} → {lokasi['lat']}, {lokasi['lng']}")

            with open(f'{LOG_FOLDER}/success_google.log', 'a') as f:
                f.write(f"{alamat} → {lokasi['lat']}, {lokasi['lng']}\n")
        else:
            print(f"[❌] Gagal: {alamat}")
            with open(f'{LOG_FOLDER}/error_google.log', 'a') as f:
                f.write(f"{alamat}\n")

    except Exception as e:
        print(f"[💥] Error pada {alamat}: {e}")
        with open(f'{LOG_FOLDER}/error_google.log', 'a') as f:
            f.write(f"{alamat} → ERROR: {e}\n")

    time.sleep(0.5)  # jeda biar gak ke-rate-limit

# Simpan hasil
df.to_csv(OUTPUT_FILE, index=False)
print("✅ Parsing 200 data selesai dan disimpan.")
