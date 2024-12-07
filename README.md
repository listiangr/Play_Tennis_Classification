# Klasifikasi Play Tennis - Naive Bayes

## Background
Permainan tenis sangat dipengaruhi oleh kondisi cuaca. Keputusan untuk bermain tenis seringkali tergantung pada faktor seperti suhu, kelembapan, dan angin. Oleh karena itu, memprediksi apakah seseorang akan bermain tenis berdasarkan kondisi cuaca dapat membantu dalam pengambilan keputusan secara otomatis, tanpa bergantung pada penilaian manual yang bisa sangat bergantung pada interpretasi individu. Dalam proyek ini, kami menggunakan algoritma Naive Bayes untuk membangun model yang dapat memprediksi keputusan bermain tenis berdasarkan data cuaca yang diberikan.

## Objectives
Tujuan dari proyek ini adalah untuk:
1. Membangun model klasifikasi menggunakan algoritma Naive Bayes untuk memprediksi apakah seseorang akan bermain tenis berdasarkan kondisi cuaca.
2. Mengevaluasi model dengan metrik seperti akurasi, precision, recall, dan confusion matrix untuk menilai kinerja model.
3. Menganalisis hasil model untuk memahami pengaruh faktor cuaca terhadap keputusan bermain tenis.
4. Membangun interface sederhana untuk mempermudah pengguna dalam memprediksi keputusan bermain tenis berdasarkan input cuaca.

## Data Overview
Dataset yang digunakan berisi informasi tentang kondisi cuaca dan keputusan apakah seseorang akan bermain tenis atau tidak. Fitur utama dalam dataset ini meliputi:
- `Outlook`: Kondisi cuaca (Sunny, Overcast, Rain)
- `Temperature`: Suhu (Hot, Mild, Cool)
- `Humidity`: Kelembapan (High, Low)
- `Wind`: Kondisi angin (Weak, Strong)
- `PlayTennis`: Keputusan bermain tenis (Yes, No)

## Dependencies
Proyek ini memerlukan beberapa dependensi berikut:

#### a. Bahasa
- `Python`: Versi 3.8+

#### b. Library
- `pandas`: Untuk pengolahan dan manipulasi data berbentuk tabel (*DataFrame*).  
- `numpy`: Untuk operasi numerik dan manipulasi array/matriks.  
- `scikit-learn`: Untuk implementasi algoritma Naive Bayes dan *machine learning*.  
- `flask`: Untuk pembuatan antarmuka web berbasis Python.  
- `pickle`: Untuk menyimpan dan memuat model atau objek Python. 

#### c. Environment  
- `Jupyter Notebook`: Untuk eksplorasi data dan pengembangan awal

#### d. Frontend
- `HTML`: Digunakan untuk membuat struktur dasar antarmuka web, seperti form input, tabel hasil prediksi, dan navigasi.
- `CSS`: Digunakan untuk mempercantik tampilan antarmuka web dengan pengaturan warna, tata letak, dan efek visual.

## Methodology
Metode yang digunakan dalam proyek ini meliputi: 

### a. Data Collection  
Dataset diambil dari sumber [Kaggle](https://www.kaggle.com/datasets/fredericobreno/play-tennis).  

### b. Data Cleaning  
- Menghapus kolom 'Day' yang tidak digunakan.
- Mengubah nilai kategorikal menjadi nilai numerik.
- Ekstraksi kolom data untuk digunakan sebaga input dan output. 

### c. Modelling  
Model dibuat menggunakan algoritma **Naive Bayes** dengan langkah-langkah:  
1. Membagi dataset menjadi `data train` dan `data test`. Rasio data yang digunakan adalah `70% data train` dan `30% data test`. 
3. Melatih model naive bayes pada data train.  
4. Memprediksi hasil pada data test.  

### d. Evaluation  
Model dievaluasi menggunakan metrix seperti `accuracy`, `precision`, `recall`, `f1-score`. Nilai `Accuracy` prediksi dari model adalah `80%`. Berikut adalah classification report dari metrix tersebut.  

![Classification Report](https://github.com/listiangr/Play_Tennis_Classification/blob/main/Classification%20Report.jpg)

## Interface  
Sebuah antarmuka web sederhana dibuat menggunakan `Flask` untuk memprediksi apakah seseorang dapat bermain tenis berdasarkan input berikut:  
- Outlook (*Sunny, Overcast, Rainy*).
- Temperature (*Hot, Mild, Cool*).  
- Humidity (*High, Normal*).  
- Wind (*Yes, No*).

Output berupa hasil prediksi: `Tidak Bisa Bermain!` **atau** `Bisa Bermain!`

Tampilan form:

![Interface](https://github.com/listiangr/Play_Tennis_Classification/blob/main/Simple%20Interface.jpg)

## How to Run  
1. Clone repository
   ```bash
   git clone https://github.com/listiangr/Play_Tennis_Classification.git
2. Install dependensi
   ```bash
   pip install -r requirements.txt
3. Run app
   ```bash
   python play_tennis_app.py
4. Open browser
   ```bash
   http://127.0.0.1:5000

