# Tubes 2 - Dasar Inteligensi Artificial (IF3070)

## Deskripsi Repository

Repository ini adalah hasil Tugas Besar 2 mata kuliah **Dasar Inteligensi Artificial (IF3070)**. Proyek ini fokus pada implementasi dan analisis tiga algoritma machine learning klasik:

1. **Decision Tree Learning (DTL)** - Algoritma pembelajaran berbasis pohon untuk klasifikasi
2. **K-Nearest Neighbors (KNN)** - Algoritma pembelajaran berbasis kemiripan jarak
3. **Logistic Regression** - Algoritma pembelajaran untuk klasifikasi biner/multikelas

Setiap algoritma diimplementasikan dari scratch dan menggunakan library Scikit-Learn, kemudian dianalisis performa dan karakteristiknya pada dataset yang sama.

---

## Setup dan Cara Menjalankan Program

### Prerequisites
- Python 3.8 atau lebih tinggi
- pip (package manager untuk Python)

### Instalasi Dependencies

```bash
pip install -r requirements.txt
```

Atau jika file requirements belum ada, install package berikut:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn jupyter
```

### Menjalankan Notebook

Untuk menjalankan dan melihat hasil implementasi algoritma:

```bash
jupyter notebook src/IF3070_Dasar_Artificial_Intelligence_Tugas_Besar_2_Notebook.ipynb
```

Atau jika menggunakan JupyterLab:

```bash
jupyter lab src/IF3070_Dasar_Artificial_Intelligence_Tugas_Besar_2_Notebook.ipynb
```

### Struktur File

```
tubes-ai2/
├── README.md                          
├── requirements.txt                   
├── data/
│   ├── train.csv                     
│   ├── test.csv                      
│   └── sample_submission.csv         
├── src/
│   └── IF3070_Dasar_Artificial_Intelligence_Tugas_Besar_2_Notebook.ipynb
│                                      
├── doc/
│   ├── Penjelasan Dataset Tubes DAI.md
│   ├── Tugas Besar 2 IF3070 Dasar Inteligensi Artifisial 2025_2026.md
│   └── Tubes2_Kelompok2_18223005_18223029_18223047_18223071.pdf
└── submission_lr.csv                 
```

---

## Pembagian Tugas Anggota Kelompok

### 1. **Andhika Maulana Addiputra (18223005)**

**Algoritma:**
- Decision Tree Learning (DTL) dari scratch
- DTL menggunakan Scikit-Learn
- Bonus: DTL dengan enhancement

**Laporan:**
- Implementasi DTL dari scratch
- Implementasi DTL Scikit-Learn
- Analisis DTL

---

### 2. **Kevin Azra (18223029)**

**Algoritma:**
- K-Nearest Neighbors (KNN) from scratch
- KNN menggunakan Scikit-Learn
- Bonus KNN 

**Laporan:**
- Latar Belakang
- Deskripsi Masalah
- Implementasi KNN dari scratch
- Implementasi KNN Scikit-Learn
- Analisis KNN
- Kesimpulan dan Saran
- Referensi
- Readme

---

### 3. **Arqila Surya Putra (18223047)**

**Algoritma:**
- Cleaning Data
- Preprocessing Data
- Logistic Regression menggunakan Scikit-Learn
- Logistic Regression dari scratch
- Iterasi Kaggle Submission

**Laporan:**
- Implementasi Logistic Regression dari scratch
- Implementasi Logistic Regression Scikit-Learn
- Analisis Hasil Logistic Regression
- Referensi

---

### 4. **Muhammad Zidni Alkindi (18223071)**

**Algoritma:**
- Preprocessing Data
- KNN menggunakan Scikit-Learn
- KNN dari scratch + Bonus

**Laporan:**
- Cleaning Data (Handling Missing Data, Dealing with Outliers, Data Validation, Remove Duplicates, Features Engineering)
- Preprocessing Data (Feature Scaling, Feature Encoding, Handling Imbalance Dataset, Data Normalization, Dimensionality Reduction)
- Analisis KNN

---

## Dataset

Dataset yang digunakan adalah dataset klasifikasi yang tersedia di folder `data/`. Dataset terdiri dari:
- **train.csv**: Data training untuk melatih model
- **test.csv**: Data testing untuk evaluasi model
- **sample_submission.csv**: Format referensi untuk submission

---

## Catatan

- Semua implementasi algoritma dari scratch ditulis menggunakan NumPy dan Pandas
- Hasil analisis dan performa algoritma terdapat di dalam Jupyter Notebook
- Laporan lengkap tersedia di folder `doc/`

---

**Created by Kelompok 2 - IF3070 Dasar Inteligensi Artificial 2025/2026**
