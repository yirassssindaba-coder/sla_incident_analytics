<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&height=210&color=0:16a34a,100:22c55e&text=SLA%20%26%20Incident%20Analytics&fontSize=52&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=Python%20Data%20Science%20%E2%80%A2%20CSV%20Ingest%20%E2%80%A2%20KPI%20%E2%80%A2%20Trend%20Chart%20%E2%80%A2%20Export%20Summary&descAlignY=58" />
</div>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-Data%20Science-3776AB?logo=python&logoColor=white" />
  <img alt="Pandas" src="https://img.shields.io/badge/pandas-CSV%20Analytics-150458?logo=pandas&logoColor=white" />
  <img alt="Status" src="https://img.shields.io/badge/Status-Ready%20to%20Run-16a34a" />
  <img alt="Offline" src="https://img.shields.io/badge/Offline-Yes-22c55e" />
</p>

<p align="center">
  <b>Analisis SLA & insiden dari file CSV</b> — hitung KPI, cek breach, dan lihat tren insiden secara cepat untuk kebutuhan ops/supports.
</p>

---

## Fitur utama
- ✅ **CSV ingest** dengan guard kolom wajib & validasi tipe data dasar
- ✅ **KPI ringkas** (contoh: total incident, resolved vs open, rata-rata durasi, SLA breach rate)
- ✅ **Trend chart** untuk melihat pola insiden (per hari/minggu — sesuai data)
- ✅ **Export summary** (ringkasan hasil) agar mudah ditempel ke report / tiket
- ✅ **Anti-error**: handle NA, empty dataset, parsing tanggal aman, dan pesan error yang jelas

---

## Persyaratan
- **Direkomendasikan:** Python **3.12 (x64)** untuk instalasi dependensi yang mulus di Windows
- **Catatan Python 3.14:** gunakan `pandas>=2.3.3` (atau pakai Python 3.12), karena `pandas==2.2.2` akan mencoba build dari source di Python 3.14 dan sering gagal jika toolchain C++ belum siap.

---

## Instalasi (Windows / PowerShell)
### Opsi A — Paling aman (Python 3.12 + venv)
```bash
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip setuptools wheel
pip install -r requirements.txt
```

### Opsi B — Kamu sudah pakai Python 3.14
1) Edit `requirements.txt`:
```txt
pandas>=2.3.3
```
2) Install:
```bash
python -m pip install -U pip setuptools wheel
pip install -r requirements.txt
```

---

## Run (script)
```bash
python analysis.py sample_incidents.csv
```

---

## Run (notebook)
Buka `sla_incident_analytics.ipynb` di **Jupyter** / **VS Code**.

---

## Format data CSV (schema)
Minimal CSV kamu sebaiknya punya kolom seperti ini (nama kolom bisa kamu sesuaikan di script kalau berbeda):

| Kolom | Tipe | Wajib | Contoh |
|------|------|------:|--------|
| `id` | string/int | ✅ | `INC-001` |
| `category` | string | ✅ | `network` |
| `priority` | string/int | ✅ | `P1` |
| `created_at` | datetime | ✅ | `2026-02-01 10:05:00` |
| `resolved_at` | datetime/empty | ❌ | `2026-02-01 12:40:00` |
| `sla_minutes` | number | ✅ | `240` |
| `status` | string | ❌ | `open/resolved` |

> Kalau `resolved_at` kosong, incident dianggap **open** dan durasinya dihitung sampai “sekarang” (atau sesuai aturan di script).

---

## Preview output (contoh)
**Contoh ringkasan (terminal)**
```text
Loaded: 120 incidents
Resolved: 98 | Open: 22
Avg resolution: 2h 14m
SLA breach: 12 (12.2%)
Top categories: network (34), app (29), device (18)
```

**Contoh export summary (CSV/JSON)**
```json
{
  "total": 120,
  "resolved": 98,
  "open": 22,
  "avg_resolution_minutes": 134,
  "sla_breach": 12,
  "sla_breach_rate": 0.122
}
```

---

## Anti-error checklist
- ✅ Cek kolom wajib sebelum proses
- ✅ `try/except` parsing tanggal (format tak dikenal → pesan error + baris bermasalah)
- ✅ Handle NA (`resolved_at` kosong)
- ✅ Empty state (CSV kosong / hasil filter kosong) → tampil pesan, tidak crash

---

## Troubleshooting cepat
### 1) `ERROR: Could not parse vswhere.exe output` saat install pandas
Penyebab: pip mencoba **build pandas dari source** (biasanya karena versi Python tidak ada wheel untuk pandas yang dipin).

Fix paling cepat:
- Pakai **Python 3.12** (Opsi A), atau
- Naikkan pandas ke `pandas>=2.3.3` (Opsi B).

### 2) `FileNotFoundError: sample_incidents.csv`
Pastikan kamu menjalankan perintah dari folder project yang benar, atau gunakan path lengkap:
```bash
python analysis.py .\data\sample_incidents.csv
```

### 3) `KeyError` kolom tidak ditemukan
Cek nama kolom CSV kamu. Samakan dengan schema atau sesuaikan mapping di script.

---

## Lisensi
Gunakan bebas untuk portofolio & demo internal. Kalau kamu mau, tulis `MIT License` di sini.

---
