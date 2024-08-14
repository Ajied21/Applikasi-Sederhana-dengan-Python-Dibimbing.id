# Applikasi Sederhana dengan Python @Dibimbing.id 

Ini adalah aplikasi pemrosesan pesanan berbasis Python yang memungkinkan Anda untuk mengelola pesanan, menghitung pajak, dan menampilkan ringkasan pesanan. Aplikasi ini dirancang untuk dijalankan dari baris perintah dan dapat di-containerized menggunakan Docker.

## Fitur

- **Manajemen Pesanan**: Membuat dan mengelola pesanan dengan detail seperti ID pesanan, nama pelanggan, tanggal pesanan, waktu pesanan, dan total jumlah.
- **Perhitungan Pajak**: Menghitung pajak berdasarkan tarif pajak yang diberikan.
- **Tampilan Pesanan**: Menampilkan informasi detail pesanan, termasuk pajak yang dihitung, dalam format yang rapi.
- **Perhitungan Total Pendapatan dan Pajak**: Menghitung total pendapatan dan pajak dari semua pesanan.

## Prasyarat

- Python 3.10
- Docker (untuk containerization)

## Instalasi

### Pengaturan Lokal

1. Clone repository:

   git clone https://github.com/username-anda/nama-repo-anda.git
   cd nama-repo-anda

2. Bangun image Docker:

    docker build -t order-processing-app . (nama bebas)

3. Jalankan container Docker:

    docker run --rm order-processing-app --order_id <ORDER_ID> --customer_name <NAMA_PELANGGAN> --total_amount <TOTAL_JUMLAH>

Argumen:

-- order_id: ID pesanan (string).
-- customer_name: Nama pelanggan (string).
-- order_date: Tanggal pesanan (string dalam format YYYY-MM-DD). Secara default, menggunakan tanggal  saat ini jika tidak diberikan.
-- order_time: Waktu pesanan (string dalam format HH:MM AM/PM). Secara default, menggunakan waktu saat ini di zona waktu Asia/Jakarta jika tidak diberikan.
-- total_amount: Total jumlah pesanan (float).
-- tax_rate: Tarif pajak yang akan diterapkan (float antara 0 dan 1). Secara default 0.07 (7%) jika tidak diberikan.

Output:

Aplikasi akan menampilkan detail pesanan, termasuk pajak yang dihitung, dalam format yang rapi. Selain itu, aplikasi juga akan menampilkan total pendapatan dan total pajak untuk semua pesanan yang telah diproses.
