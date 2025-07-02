
🗺️ BPS Geocoding Project

Proyek ini dibuat sebagai bagian dari kegiatan magang di **Badan Pusat Statistik (BPS)**. Tujuannya adalah untuk melakukan _geocoding_ terhadap ribuan data alamat lokasi usaha di Kabupaten Bondowoso — mengubah alamat menjadi koordinat (latitude & longitude) secara otomatis menggunakan API.


📌 Tujuan

- Melakukan parsing dan normalisasi alamat dari dataset mentah.
- Menggunakan API Geocoding (OpenStreetMap atau Google Maps) untuk mendapatkan koordinat.
- Menyimpan hasil ke dalam dataset yang siap digunakan untuk visualisasi atau analisis spasial.

 🗂 Struktur Folder

```
bps-geocoding-project/
│
├── data/
│   ├── raw/               # Data mentah (CSV/XLSX asli dari BPS)
│   ├── cleaned/           # Data yang telah dibersihkan
│   ├── geocoded/          # Hasil geocoding final
│   └── geocoded_batches/  # Hasil batch per 500 data
│
├── scripts/
│   ├── geocode.py         # Script utama (OpenStreetMap)
│   ├── geocode_google.py  # Script alternatif (Google Maps) ❌ Gitignored
│   ├── utils.py           # Script cleaning & formatting
│   └── config.py          # API Key (❌ Gitignored)
│
├── logs/                  # File log sukses dan error
├── reports/               # Laporan progres dan error manual
├── requirements.txt       # Dependency Python
└── README.md              # Dokumentasi proyek ini
```

---

⚙️ Cara Menjalankan

1. Install Dependency

```bash
pip install -r requirements.txt
```

2. Bersihkan Data

```bash
python scripts/utils.py
```

3. Jalankan Geocoding (OpenStreetMap)

```bash
python scripts/geocode.py
```

4. Alternatif: Jalankan Geocoding (Google Maps)

```bash
python scripts/geocode_google.py
```



 💾 Output

- `bondowoso_geocoded.csv`: Dataset final berisi alamat + koordinat
- `success.log`: Daftar alamat yang berhasil di-geocode
- `error.log`: Daftar alamat yang gagal (perlu pengecekan manual)



🛡️ Catatan Keamanan

> File `config.py` dan `geocode_google.py` tidak di-upload ke repo ini karena berisi **API Key pribadi** dan script alternatif khusus pengujian.


 📍 Contoh Hasil Geocoding

| Nama Usaha         | Alamat                         | Latitude   | Longitude   |
|--------------------|--------------------------------|------------|-------------|
| TAPE 82            | Jl. Brigjen Pol. Sudarlan 53   | -7.912345  | 113.717891  |
| PERTANIAN JAYA     | Jebung Kidul                   | -7.943210  | 113.756900  |



📬 Kontak

Dibuat oleh: **Muhammad Anwar Thoriq**  
Magang di: **Badan Pusat Statistik (BPS)**  
Project: Geocoding Kabupaten Bondowoso  
Email: _[masukin email lo kalau mau]_



> _“Transforming messy location data into clean geographic insights.”_ 🌍
