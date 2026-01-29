# Tes Junior Programmer – Django

## Overview
Project ini dibuat untuk menyelesaikan Tes Junior Programmer dengan studi kasus integrasi API FastPrint menggunakan Django.

Fokus utama:
- Mengambil data dari API
- Menyimpan data ke database relasional yang sudah tersedia
- Menampilkan dan mengelola data menggunakan CRUD

---

## Tech Stack
- Python
- Django
- Django REST Framework
- Database existing (managed = False)
- Requests

---

## Database & Model
Struktur database sudah tersedia sebelumnya, sehingga Django digunakan sebagai ORM tanpa mengelola migrasi.

Penyesuaian model:
- `id_produk` dari API digunakan sebagai primary key
- Data `kategori` dan `status` dari API disimpan ke tabel master terpisah
- Relasi menggunakan foreign key

---

## Menjalankan Project

```bash
pip install django djangorestframework requests
python manage.py runserver
