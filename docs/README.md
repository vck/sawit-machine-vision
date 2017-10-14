at  Lunak untuk Sistem Machine Vision Grading Buah Kelapa Sawit
---
### A. Arsitektur Perangkat Lunak

Perangkat lunak pada sistem ini terdiri 

1. Antar muka kamera-pengguna

Antar muka antara kamera dan pengguna dibangun dalam bentuk aplikasi web. Tujuannya, agar bisa diakses oleh semua platform (PC/Laptop/Smartphone). 

2. Pemrosesan citra digital 

Pemrosesan citra dilakukan dengan pustaka Pillow. Dalam sistem ini, dilakukan 2 operasi pemrosesan citra; ekstraksi fitur RGB dan konversi RGB ke gray value. 

### Pengembangan Perangkat 
Pengembangan dilakukan menggunakan bahasa pemrograman Python, 
Python dipilih karena:

1. Rapid prototyping & deployment
Prototype software dapat dikembangkan menjadi software jadi dalam waktu singkat.

2. Open source & dukungan pustaka dari komunitas
Pustaka untuk pemrosesan citra dan machine learning / machine vision disediakan oleh komunitas secara gratis. 

### Pustaka dan Framework
Pustaka dan Framework yang digunakan selama pengembangan:

1. Flask web framework 
- opensource
- rapid prototyping and deployment

2. Pillow (Python Imaging Library) 
Pillow menyediakan fungsi-fungsi yang sering digunakan dalam pemrosesan citra, seperti manipulasi gambar, ekstraksi fitur citra (RGB/gray value).

### Alur sistem

1. Raspberry Pi dihidupkan.
2. Server berjalan di latar belakang (background).
3. Akses kamera pada raspberry pi.
4. Tampilkan antarmuka kamera pada web browser. 
5. User menekan tombol "capture".
6. Citra disimpan pada disk menurut format `(DDMMYY-hhmmss).jpg`.
7. Citra yang telah disimpan diproses menggunakan Pillow untuk ekstraksi fitur RGB dan gray value.
8. Citra yang telah ditangkap beserta fitur RGB dan gray value nya ditampilkan pada antar muka.
9. Tunggu sampai ada operasi capture, ulangi 6-8.
 
### Kode sumber

1. Pemrosesan citra


```

3 from PIL import Image
4 from picamera import PiCamera

5 camera = PiCamera(sensor_mode=5)
6 filename = generate_filename()
7 camera.capture("static/"+filename)
8 im = Image.open("static/"+filename)
9 rgb_im = im.convert('RGB')
10 R,G,B = rgb_im.getpixel((1, 1))
11 grey_value = (0.3 * R, 0.59 * G, 0.11 * B)
```

Penjelasan kode:

3. Load kelas Image dari pustaka PIL, kelas Image berisi fungsi/routine untuk manipulasi citra dan ekstraksi fitur citra.

4. Load kelas PiCamera dari pustaka picamera untuk interfacing antara python dengan kamera dari Raspberry Pi.

5.  Buat object dari kelas PiCamera, dengan mode sensor 5.

6.  Buat variabel `filename` yang berisi string dengan format `DDMMYY-hhmmss.jpg` 

7.  Tangkap citra dari objek dengan fungsi capture dari objek camera, lalu simpan di folder static dengan nama dari variabel `filename`.

8. Buat objek `im` yang berisi data citra (berupa matrix) dan rutin-rutin yang untuk manipulasi.

9. Buat objek `rbg_im`, objek ini berisi matrix (3 * n), tiap row pada kolom n berisi 3 data untuk masing-masing nilai R, G, dan B.

10. Buat variabel `R`, `G`, `B` yang berisi nilai R, G, B dari citra.

11. Konversi nilai RGB ke gray value menggunakan weight 0.3, 0.9, 0.11 untuk masing-masing nilai R, G, dan B.
