# II3160 Teknologi Sistem Terintegrasi - Final Project
## Service: Warehouse Core System

Layanan ini bertanggung jawab untuk mengelola seluruh data inventaris barang, dimensi fisik, serta status ketersediaan barang di gudang.

### 👥 Anggota Kelompok
- **Muhammad Adam Mirza** - [18223015] 
- **Darryl Rayhananta Adenan** - [18223042] 

### 📝 Deskripsi Sistem
Warehouse Core merupakan *supporting subdomain* dalam sistem logistik kami. Service ini menyediakan REST API untuk pendaftaran barang baru, pemantauan stok, dan pembaruan status barang secara sinkron saat diakses oleh layanan eksternal (Shipment Service). Data disimpan secara persisten menggunakan database Supabase.

### 🛠️ Tech Stack
- **Framework:** Django 5.x
- **Database:** Supabase (PostgreSQL)
- **Tools:** Docker, Python-dotenv

### 🚀 Cara Menjalankan (Local)
1. Buat virtual environment: `python -m venv venv`
2. Aktivasi venv: `source venv/bin/activate` (Linux/Mac) atau `venv\Scripts\activate` (Windows)
3. Install dependencies: `pip install -r requirements.txt`
4. Buat file `.env` dan masukkan `API_TOKEN` serta kunci database `DATABASE_URL`.
5. Jalankan migrasi: `python manage.py migrate`
6. Jalankan server: `python manage.py runserver 8000`

### 📡 API Endpoints
- `GET /api/packages/` - List semua barang
- `POST /api/packages/` - Tambah barang baru
- `PATCH /api/packages/<id>/` - Update status & shipping cost
- `GET /api/packages/<id>/` - Detail suatu barang