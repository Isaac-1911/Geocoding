import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
import time
import os

# ========== Konfigurasi ==========
BATCH_SIZE = 500
BATCH_FOLDER = '../data/geocoded_batches'
INPUT_FILE = '../data/cleaned/bondowoso_cleaned.csv'
LOG_FOLDER = '../logs'

# ========== Setup Folder ==========
os.makedirs(BATCH_FOLDER, exist_ok=True)
os.makedirs(LOG_FOLDER, exist_ok=True)

# ========== Inisialisasi Geocoder ==========
geolocator = Nominatim(user_agent="bps-geocoding")

# ========== Fungsi Geocoding ==========
def geocode_location(lokasi, retries=3):
    for attempt in range(retries):
        try:
            location = geolocator.geocode(lokasi, timeout=10)
            if location:
                return location
        except (GeocoderTimedOut, GeocoderServiceError):
            print(f"Retry {attempt+1}/{retries} → {lokasi}")
            time.sleep(2)
    return None

# ========== Baca Data ==========
df = pd.read_csv(INPUT_FILE, on_bad_lines='skip')

# ========== Proses per Batch ==========
total_rows = len(df)
for start in range(0, total_rows, BATCH_SIZE):
    end = start + BATCH_SIZE
    batch_df = df.iloc[start:end].copy()
    
    batch_file = f"{BATCH_FOLDER}/batch_{start}_{end-1}.csv"
    if os.path.exists(batch_file):
        print(f"[⏩] Lewat: {batch_file} sudah ada")
        continue
      
    print(f"\n🚀 Mulai Batch {start}-{end-1}...")

    batch_df['Latitude'] = None
    batch_df['Longitude'] = None

    for idx, row in batch_df.iterrows():
        lokasi = str(row['Alamat_Usaha']).strip().title() + ", Bondowoso"
        location = geocode_location(lokasi)

        if location:
            batch_df.at[idx, 'Latitude'] = location.latitude
            batch_df.at[idx, 'Longitude'] = location.longitude
            print(f"[✅] {lokasi} → {location.latitude}, {location.longitude}")

            with open(f'{LOG_FOLDER}/success.log', 'a') as f:
                f.write(f"{lokasi} → {location.latitude}, {location.longitude}\n")
        else:
            print(f"[❌] Gagal: {lokasi}")
            with open(f'{LOG_FOLDER}/error.log', 'a') as f:
                f.write(f"{lokasi}\n")
        
        time.sleep(1)

    batch_df.to_csv(batch_file, index=False)
    print(f"💾 Disimpan: {batch_file}")

print("\n🎉 Semua batch selesai diproses!")
