from flask import Flask, request, render_template
import pickle
import numpy as np 

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Membuka dan memuat model yang telah disimpan sebelumnya
model_file = open('model_play_tennis.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

# Route untuk halaman utama
@app.route('/')
def index():
    # Mengembalikan tampilan HTML dengan nilai default untuk hasil
    return render_template('index.html', hasil=0)

# Route untuk melakukan prediksi berdasarkan input dari pengguna
@app.route('/predict', methods=['POST'])
def predict():
    '''
    Fungsi untuk memprediksi apakah bisa bermain berdasarkan input pengguna
    dan menampilkan hasil prediksi ke halaman HTML
    '''
    # Mendapatkan data input dari form di halaman HTML
    outlook = int(request.form['outlook'])  
    temp = int(request.form['temp'])       
    humidity = int(request.form['humidity'])
    wind = int(request.form['wind'])      
    
    # Membuat array 2D dengan input pengguna untuk digunakan dalam prediksi
    x = np.array([[outlook, temp, humidity, wind]])
    
    # Melakukan prediksi menggunakan model yang telah dimuat
    prediction = model.predict(x)
    
    # Daftar kategori outlook, temperatur, humidity, dan wind untuk ditampilkan dalam hasil
    outlooks = ['Overcast', 'Rain', 'Sunny']
    temps = ['Cool', 'Hot', 'Mild']
    humiditys = ['High', 'Normal']
    winds = ['Strong', 'Weak']
    
    # Menentukan hasil berdasarkan prediksi (0 berarti tidak bisa bermain, 1 berarti bisa bermain)
    if(prediction == 0):
        play = "Tidak Bisa Bermain!"
    elif(prediction == 1):
        play = "Bisa Bermain!"
    
    # Mengembalikan hasil prediksi ke halaman HTML, bersama dengan input yang telah dipilih pengguna
    return render_template('index.html', hasil=play, outlook=outlooks[outlook], temp=temps[temp], 
                           humidity=humiditys[humidity], wind=winds[wind])

# Menjalankan aplikasi Flask dalam mode debug
if __name__ == '__main__':
    app.run(debug=True)
