[English](Modernisation) · [Dansk](Modernisation-da) · **Bahasa Malaysia**

# Pemodenan

| Penyelesaian asal | Penyelesaian moden | Sebab |
| --- | --- | --- |
| Satu `main.py` | Lapisan dalam `src/scraping_python_org` (domain, application, infrastructure, presentation) | Peraturan perniagaan tidak bergantung pada Selenium; use case diuji dengan palsu (fake) |
| XPath mutlak yang panjang | Pemilih CSS `.event-widget li` | Pendek, mudah dibaca, tahan perubahan reka letak |
| Pembilang manual `c` | `enumerate` | Kod lebih sedikit, tiada ralat off-by-one |
| `detach=True` diikuti `driver.quit()` | Chrome headless dalam context manager yang sentiasa menutup | Tiada tetingkap pelayar tertinggal, berjalan tanpa desktop |
| `selenium` tanpa versi dalam `requirements.txt` | `pyproject.toml` dengan versi minimum | Pemasangan yang boleh diulang |
| Tiada ujian | Ujian unit dan ujian pelayar headless pada halaman tersimpan | Perubahan selamat |
| Tiada petunjuk jenis | `mypy --strict`, `ruff` | Ralat ditemui sebelum dijalankan |

**Apa yang anda peroleh:** pengikis yang boleh diubah dengan yakin; idea yang
sama seperti dalam pelajaran, tetapi dibina seperti projek sebenar.
