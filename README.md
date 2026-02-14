<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&height=130&color=0:16a34a,100:22c55e&text=SLA%20%26%20Incident%20Analytics&fontSize=34&fontColor=ffffff&animation=fadeIn&fontAlignY=55" />
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=14&duration=2200&pause=700&color=22C55E&center=true&vCenter=true&width=900&lines=CSV+ingest+%E2%86%92+schema+check+%E2%86%92+cleaning+NA+%E2%86%92+KPI;Resolution+time+%2B+SLA+breach+rate+%2B+trend+chart;Export+summary+(JSON%2FCSV)+%7C+Notebook+ready;Offline-friendly+guards%3A+empty+state+%2B+safe+date+parse" />
  <br/>
  <img src="https://skillicons.dev/icons?i=python,anaconda,vscode&perline=3" />
</div>

---

## Run (script)
```bash
python analysis.py sample_incidents.csv
```

---

## Run (notebook)
Open `sla_incident_analytics.ipynb` in Jupyter/VSCode.

---

## Fitur utama
- ✅ CSV ingest + **guard kolom wajib**
- ✅ Handle **NA** (`resolved_at` kosong) dan **empty dataset**
- ✅ KPI: total incident, resolved vs open, avg resolution, **SLA breach rate**
- ✅ Trend chart (sesuai data)
- ✅ Export ringkasan (untuk report/tiket)

---

## Persyaratan
- **Disarankan (Windows):** Python **3.12 (x64)** untuk instalasi dependensi yang mulus.
- **Jika pakai Python 3.14:** gunakan `pandas>=2.3.3` (jangan pin `pandas==2.2.2` karena bisa memaksa build dari source).

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

## Format CSV (schema minimal)
| Kolom | Tipe | Wajib | Contoh |
|------|------|------:|--------|
| `id` | string/int | ✅ | `INC-001` |
| `category` | string | ✅ | `network` |
| `priority` | string/int | ✅ | `P1` |
| `created_at` | datetime | ✅ | `2026-02-01 10:05:00` |
| `resolved_at` | datetime/empty | ❌ | `2026-02-01 12:40:00` |
| `sla_minutes` | number | ✅ | `240` |
| `status` | string | ❌ | `open/resolved` |

> Jika `resolved_at` kosong, incident dianggap **open** dan durasinya dihitung sesuai aturan di script.

---

## Preview output (contoh)
**Ringkasan (terminal)**
```text
Loaded: 120 incidents
Resolved: 98 | Open: 22
Avg resolution: 2h 14m
SLA breach: 12 (12.2%)
Top categories: network (34), app (29), device (18)
```

**Export summary (contoh)**
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
- ✅ Parsing tanggal aman (format aneh → pesan error jelas)
- ✅ Handle NA (`resolved_at` kosong)
- ✅ Empty state (CSV kosong / hasil filter kosong) → tidak crash

---

## Troubleshooting cepat
### `ERROR: Could not parse vswhere.exe output` saat install pandas
Penyebab: pip mencoba **build pandas dari source**.
Fix:
- Pakai **Python 3.12** (Opsi A), atau
- Naikkan pandas ke `pandas>=2.3.3` (Opsi B).

---

## Lisensi
Bebas untuk portofolio & demo internal (opsional: tambahkan MIT License).
