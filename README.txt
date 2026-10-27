MODEL DATA MINING - DECISION TREE
=================================

Isi folder:
1. model_decision_tree.py : kode Python model Decision Tree.
2. data_pasien.csv        : dataset 10 pasien dari file Excel.
3. requirements.txt       : daftar library yang diperlukan.
4. pohon_keputusan.png    : akan dibuat otomatis saat program dijalankan.

Cara menjalankan di Visual Studio Code:
1. Ekstrak ZIP lalu buka folder ini di VS Code.
2. Pastikan Python sudah terpasang.
3. Buka Terminal pada folder proyek.
4. Jalankan:  pip install -r requirements.txt
5. Jalankan:  python model_decision_tree.py

Perbedaan dari model sebelumnya:
- Model sebelumnya menggunakan KNN, yaitu mencari tetangga terdekat.
- Model ini menggunakan Decision Tree, yaitu membuat aturan bercabang seperti pohon keputusan.

Catatan:
Dataset berisi 10 baris contoh, jadi akurasi pada data latih tidak mewakili kinerja
model pada data baru. Prediksi ini hanya untuk tugas pembelajaran data mining,
bukan untuk diagnosis medis.
