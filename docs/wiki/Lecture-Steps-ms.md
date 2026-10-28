[English](Lecture-Steps) · [Dansk](Lecture-Steps-da) · **Bahasa Malaysia**

# Langkah pelajaran

## Langkah 1 – Buka laman

![Laman utama python.org](images/01-python-org-home.png)

`driver.get("https://www.python.org/")` memuatkan laman dalam Chrome.

**Apa yang anda peroleh:** driver ialah alat kawalan jauh untuk pelayar sebenar.
Ia mesti ditutup semula, jadi kod moden menggunakan `try/finally`.

## Langkah 2 – Cari widget dengan alat pemeriksa

![Widget Upcoming Events](images/02-event-widget.png)

Klik kanan pada widget dan pilih *Inspect*. Acara berada dalam elemen berkelas
`event-widget`; setiap acara ialah `li` yang mengandungi teg `time` dan `a`.

**Apa yang anda peroleh:** anda belajar membaca pepohon HTML dan mencari
bekas yang menyimpan data yang tepat seperti yang dikehendaki.

## Langkah 3 – Pilih lima item senarai dengan pemilih CSS

![Lima item senarai ditandakan merah](images/03-event-list-highlighted.png)

`driver.find_elements(By.CSS_SELECTOR, ".event-widget li")` mengembalikan lima
item. Pemilih berasaskan kelas lebih pendek dan lebih stabil daripada XPath
panjang yang disalin dari pemeriksa, dan ia tidak memadankan pautan lain.

**Apa yang anda peroleh:** anda mengenali strategi locator Selenium dan bila
pemilih CSS lebih baik daripada XPath.

## Langkah 4 – Bina kamus

![Kamus yang dicetak](images/04-output-dictionary.png)

Untuk setiap item kita baca `time` dan `a` lalu simpan di bawah indeks item itu,
dengan `enumerate` dan bukannya pembilang manual.

**Apa yang anda peroleh:** anda menukar elemen halaman kepada data tersusun:
kamus dalam kamus, sedia digunakan dalam bahagian program yang lain.
