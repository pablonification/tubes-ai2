# Penjelasan Dataset Tubes DAI

## Deskripsi Kolom

| Nama Kolom | Penjelasan |
|------------|------------|
| **ID** | Indeks baris (integer) yang unik untuk setiap data, dibuat di akhir proses generasi data. |
| **transaction_id** | ID unik untuk setiap transaksi (format string seperti T0001234). |
| **user_id** | ID pengguna yang melakukan transaksi. Menghubungkan beberapa transaksi dari pengguna yang sama. |
| **age** | Umur pengguna dalam tahun. |
| **gender** | Jenis kelamin pengguna: M (male/laki-laki) atau F (female/perempuan). |
| **country** | Negara tempat transaksi dilakukan (misalnya: US, UK, ID). |
| **device_type** | Jenis perangkat yang digunakan: mobile, desktop, atau tablet. |
| **device_os** | Sistem operasi perangkat yang digunakan (misalnya: Android, iOS, Windows, Linux, MacOS). |
| **transaction_amount** | Jumlah uang pada transaksi tersebut. |
| **transaction_type** | Jenis transaksi: purchase, transfer, topup, atau withdrawal. |
| **merchant_category** | Kategori merchant/toko tempat transaksi terjadi (misalnya electronics, groceries, gas). |
| **time_of_day** | Jam transaksi dilakukan dalam format 0-23. |
| **day_of_week** | Hari dalam seminggu (0= Senin, 6= Minggu). |
| **transaction_duration** | Lama waktu proses transaksi (dalam detik), dihasilkan dengan distribusi eksponensial. |
| **num_prev_transactions** | Jumlah transaksi sebelumnya yang pernah dilakukan oleh pengguna. |
| **avg_transaction_amount** | Rata-rata jumlah transaksi historis pengguna. |
| **std_transaction_amount** | Standar deviasi (simpangan baku) dari jumlah transaksi historis pengguna. |
| **transactions_last_24h** | Jumlah transaksi yang dilakukan pengguna dalam 24 jam terakhir. |
| **transactions_last_1h** | Jumlah transaksi yang dilakukan pengguna dalam 1 jam terakhir. |
| **failed_login_attempts** | Jumlah percobaan login yang gagal sebelum transaksi ini terjadi. |
| **ip_risk_score** | Skor risiko (0−1) berdasarkan IP address pengguna. Semakin tinggi semakin berisiko. |
| **device_trust_score** | Skor kepercayaan perangkat (0−1). Semakin tinggi semakin aman. |
| **shared_ip_users** | Jumlah pengguna lain yang berbagi alamat IP yang sama. |
| **shared_device_users** | Jumlah akun pengguna lain yang pernah menggunakan perangkat fisik yang sama. |
| **account_age_days** | Lama umur akun dalam hari. Nilai kecil berarti akun masih baru. |
| **has_chargeback_history** | Apakah pengguna pernah memiliki riwayat chargeback (0= tidak, 1=ya). |
| **merchant_risk** | Skor risiko spesifik berdasarkan kategori merchant (misal: financial lebih tinggi dari groceries). |
| **country_risk** | Skor risiko spesifik berdasarkan negara asal transaksi. |
| **distance_from_home** | Jarak lokasi transaksi dari rumah pengguna (satuan jarak tertentu). |
| **is_new_country** | Penanda apakah ini kali pertama pengguna bertransaksi di negara tersebut (1= ya, 0= tidak). |
| **is_fraud** | Label fraud (0= normal, 1= fraud). |

---

## Kategori Fitur

### Informasi Pengguna
- age, gender, user_id, account_age_days

### Informasi Perangkat
- device_type, device_os, device_trust_score, shared_device_users

### Informasi Transaksi
- transaction_id, transaction_amount, transaction_type, merchant_category, transaction_duration

### Informasi Waktu
- time_of_day, day_of_week

### Informasi Lokasi
- country, distance_from_home, is_new_country, country_risk

### Riwayat & Perilaku
- num_prev_transactions, avg_transaction_amount, std_transaction_amount
- transactions_last_24h, transactions_last_1h
- has_chargeback_history

### Indikator Risiko
- ip_risk_score, shared_ip_users, failed_login_attempts, merchant_risk

### Target
- is_fraud (Label untuk klasifikasi)