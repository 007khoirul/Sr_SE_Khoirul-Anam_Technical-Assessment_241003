# Arithmetic Sequence Generator

This project generates an arithmetic sequence based on the user input.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/arithmetic_sequence.git



Logika Pemrograman
Definisikan Fungsi:

Buat fungsi bernama generate_arithmetic_sequence yang menerima tiga parameter:
n: jumlah elemen yang diinginkan,
start: nilai awal deret (default 2),
diff: beda antar elemen (default 3).
Inisialisasi List:

Di dalam fungsi, inisialisasi sebuah list kosong bernama sequence untuk menyimpan elemen-elemen dari deret.
Loop untuk Menghitung Elemen Deret:

Buat loop dari 0 hingga n-1 untuk menghitung setiap elemen deret:
Hitung elemen ke-i menggunakan rumus:
term
=
start
+
(
𝑖
×
diff
)
term=start+(i×diff)
Tambahkan nilai term ke dalam list sequence.
Kembalikan Hasil:

Setelah loop selesai, kembalikan list sequence yang berisi elemen-elemen deret.
Program Utama:

Dalam blok utama, tampilkan pesan untuk meminta pengguna memasukkan jumlah elemen deret.
Baca input pengguna dan simpan dalam variabel n.
Panggil fungsi generate_arithmetic_sequence(n) dan simpan hasilnya dalam variabel result.
Tampilkan hasil deret ke layar.

Contoh Alur Kerja
Misalkan pengguna memasukkan n = 4:

Fungsi generate_arithmetic_sequence dipanggil dengan n = 4, start = 2, dan diff = 3.
List sequence diinisialisasi sebagai kosong: [].
Loop dimulai:
Iterasi 0: term = 2 + (0 * 3) = 2, list menjadi [2].
Iterasi 1: term = 2 + (1 * 3) = 5, list menjadi [2, 5].
Iterasi 2: term = 2 + (2 * 3) = 8, list menjadi [2, 5, 8].
Iterasi 3: term = 2 + (3 * 3) = 11, list menjadi [2, 5, 8, 11].
Fungsi mengembalikan list [2, 5, 8, 11].
Program utama menampilkan output: [2, 5, 8, 11].