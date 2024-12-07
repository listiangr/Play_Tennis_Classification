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
Evaluasi model dilakukan dengan menggunakan **Classification Report** yang mencakup metrik `precision`, `recall`, `f1-score`, dan `accuracy`. Berikut adalah hasil evaluasi:

![Classification Report](https://github.com/listiangr/Play_Tennis_Classification/blob/main/Classification%20Report.jpg)

Berdasarkan hasil **Classification Report** di atas, berikut adalah penjelasan dari metrik-metrik yang digunakan untuk mengevaluasi performa model:

1. **Akurasi Model**: Model berhasil memprediksi dengan benar `80%` dari total data yang ada.
2. **Kelas 0 (Negatif)**:
   - `Precision = 0.50`: Hanya 50% prediksi kelas 0 yang benar-benar akurat. Ini menunjukkan model sering salah dalam mengidentifikasi kelas 0 meskipun recall-nya sempurna.
   - `Recall = 1.00`: Model berhasil mendeteksi semua data berlabel kelas 0, artinya model tidak melewatkan satupun data kelas 0.
   - `F1-Score = 0.67`: Metrik ini adalah rata-rata harmonik dari precision dan recall. Dengan precision yang rendah dan recall yang sempurna, F1-score tercatat cukup moderat.
   - `Support = 1`: Hanya ada 1 data berlabel kelas 0 dalam dataset, yang membuat metrik ini sangat dipengaruhi oleh data tersebut.

4. **Kelas 1 (Positif)**:
   - `Precision = 1.00`: Semua prediksi kelas 1 benar, yang menunjukkan model sangat akurat dalam mengidentifikasi kelas 1.
   - `Recall = 0.75`: Dari semua data berlabel kelas 1, model berhasil mendeteksi 75% dari data tersebut.
   - `F1-Score = 0.86`: F1-Score yang tinggi mencerminkan bahwa model cukup baik dalam menyeimbangkan antara precision dan recall.
   - `Support = 4`: Terdapat 4 data berlabel kelas 1 dalam dataset.
  
## Interface  
Sebuah antarmuka web sederhana dibuat menggunakan `Flask` untuk memprediksi apakah seseorang dapat bermain tenis berdasarkan input berikut:  
- Outlook (*Sunny, Overcast, Rainy*).
- Temperature (*Hot, Mild, Cool*).  
- Humidity (*High, Normal*).  
- Wind (*Yes, No*).

Output berupa hasil prediksi: `Tidak Bisa Bermain!` **atau** `Bisa Bermain!`

Tampilan form:

![Interface](https://github.com/listiangr/Play_Tennis_Classification/blob/main/Simple%20Interface.jpg)

## Kesimpulan
- Model menunjukkan **akurasinya sebesar 80%**, yang menunjukkan kinerja yang cukup baik secara keseluruhan.
- **Precision** untuk kelas 1 sangat tinggi (1.00), namun **recall** untuk kelas 1 masih bisa diperbaiki agar lebih banyak data kelas 1 yang terdeteksi.
- **Precision** untuk kelas 0 lebih rendah (0.50), tetapi **recall** untuk kelas 0 sempurna (1.00), yang berarti model berhasil mendeteksi semua data kelas 0 meskipun dengan akurasi yang lebih rendah.
- Ketidakseimbangan jumlah data antara kelas 0 dan kelas 1 (support kelas 0 = 1, kelas 1 = 4) memengaruhi hasil evaluasi.

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

