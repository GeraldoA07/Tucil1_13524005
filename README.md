# Queen LinkedIn Problem Solver – Tucil1_13524005

## Deskripsi Singkat
Program ini membaca papan huruf (N x N) dari berkas teks di folder `input`, memvalidasi, lalu mencari penempatan ratu sesuai dengan warna-warna yang ada tetapi harus memenuhi aturan (berdasarkan pengelompokan warna). Aturan: tidak ada 2 queen dalam satu baris/kolom, dan tidak ada queen yang bersentuhan diagonal (minimal ada satu sel kosong di antaranya). Algoritma pencarian dilakukan dengan brute force. Hasil solusi dapat ditampilkan di terminal atau GUI, lalu disimpan ke folder `test` (antara `text` atau `image`).

## Requirement & Instalasi
- Python 3.10+ (disarankan 3.11)
- Pip untuk memasang dependensi: `customtkinter` dan `Pillow`

Instal dependensi (sekali) dari root proyek:
```powershell
python -m pip install customtkinter pillow
```

## Menjalankan
### Mode CLI
- Dari root proyek:
```powershell
python src\main.py
```
- Ketik nama file input yang ada di folder `input` (mis. `test1.txt`).
- Setelah solusi ditemukan, pilih apakah ingin menyimpan sebagai teks atau PNG. Output akan berada di `test/text` atau `test/image`.

### Mode GUI
- Dari root proyek (atau dari folder `src`):
```powershell
python src\gui.py
```
- Pilih **Input File TXT** untuk memilih berkas dari folder `input`, atau **Input Manual** untuk mengetik papan secara bebas.
- Setelah solusi ditemukan, papan akan digambar dengan ikon mahkota. Tekan **Save Solution Image** untuk menyimpan sebagai PNG atau TXT (dialog pemilihan format akan muncul). File disimpan ke `test/image` atau `test/text` dengan nama mengikuti sumber input (mis. `test1.png`).

## Kompilasi (Opsional, membuat executable CLI)
Jalankan dari root proyek (Tucil1_13524005):
1. Instal PyInstaller (sekali):
   ```powershell
   python -m pip install pyinstaller
   ```
2. Bangun executable ke folder `bin`:
   ```powershell
   python -m PyInstaller --onefile --distpath bin --name queen_solver src\main.py
   ```
Hasilnya `bin\queen_solver.exe`.

## Author
Geraldo Artemius (NIM 13524005) – K1 Strategi Algoritma.
