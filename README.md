# SafeClickBot

SafeClickBot adalah chatbot edukasi keamanan digital berbasis rule-based yang
menggunakan Flask, JSON sebagai knowledge base, dan SQLite untuk menyimpan
riwayat percakapan.

## Fitur
- 10 intent sesuai knowledge mapping: salam, phishing, link palsu, keamanan OTP,
  password, penipuan online, malware, akun diretas, data pribadi, dan terima kasih.
- Pencocokan pertanyaan dengan normalisasi bahasa Indonesia dan skor kemiripan.
- Fallback response untuk pertanyaan di luar basis pengetahuan.
- Pertanyaan rekomendasi, riwayat chat, mode belajar, dan halaman statistik.
- Knowledge base dipisahkan dari kode Python di `themes/safeclickbot.json`.

## Menjalankan aplikasi (Windows)

Buka terminal pada folder `aplikasi-final`, lalu jalankan:

```bash
py -m venv .venv
.venv\\Scripts\\activate
py -m pip install -r requirements.txt
python app.py
```

Buka `http://127.0.0.1:5000` di browser, lalu pilih SafeClickBot.

## Menjalankan pengujian

```bash
python -m pytest
```

## Mengubah knowledge base

Edit file `themes/safeclickbot.json`. Setiap intent memiliki:
- `tag`: identitas intent.
- `patterns`: variasi pertanyaan pengguna.
- `responses`: variasi jawaban chatbot.

Pastikan setiap `tag` unik dan setiap intent memiliki minimal satu pattern
serta satu response. Engine akan memvalidasi struktur tema saat aplikasi dimulai.
