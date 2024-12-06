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
- **Python**: Versi 3.8+

#### b. Library Utama  
- `pandas`: Untuk pengolahan data
- `numpy`:
- `scikit-learn`: Untuk implementasi algoritma Naive Bayes  
- `flask`: Untuk pembuatan antarmuka web
- `pickle`: 

#### c. Environment  
- **Jupyter Notebook**: Untuk eksplorasi data dan pengembangan awal

## Methodology
Metode yang digunakan dalam proyek ini meliputi: 

### a. Data Collection  
Dataset diambil dari sumber [Kaggle](https://www.kaggle.com/datasets/fredericobreno/play-tennis).  

### b. Data Cleaning  
- Tidak ada nilai kosong dalam dataset.
- Menghapus kolom 'Day' yang tidak digunakan.
- Nilai semua kolom dikonversi ke tipe data kategorikal.  

### c. Modelling  
Model dibuat menggunakan algoritma **Naive Bayes** dengan langkah-langkah:  
1. Membagi dataset menjadi *train* dan *test set*.  
2. Melatih model pada *train set*.  
3. Memprediksi hasil pada *test set*.  

### d. Evaluation  
Model dievaluasi menggunakan metrik berikut:  
- **Akurasi**  
- **Confusion Matrix**  
- **Classification Report**
Hasil Evaluasi:  
[Classification Report](https://github.com/listiangr/Play_Tennis_Classification/blob/main/Classification%20Report.png)

## Interface  
Sebuah antarmuka web sederhana dibuat menggunakan **Flask** untuk memprediksi apakah seseorang akan bermain tenis berdasarkan input berikut:  
- Cuaca (*Sunny, Overcast, Rainy*).  
- Suhu (*Hot, Mild, Cool*).  
- Kelembapan (*High, Normal*).  
- Kondisi angin (*Yes, No*).  

Tampilan form:
[Interface](https://github.com/listiangr/Play_Tennis_Classification/blob/main/Simple%20Interface.png?row=true)

Output berupa hasil prediksi: **Play Tennis: Yes/No**.  

## How to Run  

### a. Persyaratan  
- Python 3.8+  
- Library: `flask`, `scikit-learn`, `pandas`, `numpy`  

### b. Langkah-Langkah  
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


---

Authors

Proyek ini dikembangkan oleh:

Listia Ningrum



---

License

Proyek ini menggunakan lisensi MIT. Lihat file LICENSE untuk detailnya.
