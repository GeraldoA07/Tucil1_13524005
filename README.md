# Queen LinkedIn Problem Solver – Tucil1_13524005

## Deskripsi Singkat
Program ini membaca papan huruf (N x N) dari berkas teks di folder `input`, memvalidasi, lalu mencari penempatan ratu sesuai dengan warna-warna yang ada tetapi harus memenuhi aturan (berdasarkan pengelompokan warna). Aturannya berupa tidak ada 2 queen dalam satu baris atau kolom, lalu tidak boleh ada queen yang letaknya bersebelahan secara diagonal bersentuhan, harus ada space di antaranya. Algoritma ini dibuat dengan brute force. Hasil solusi dapat ditampilkan di terminal dan disimpan ke folder `test`.

## Requirement & Instalasi
- Python 3.10+ (disarankan 3.11)
- Pip untuk memasang dependensi (saat ini hanya standar library, jadi tidak ada paket eksternal)

## Kompilasi (Opsional, membuat executable)
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

## Menjalankan & Penggunaan
- Jalankan langsung dengan Python dari root proyek:
	```powershell
	python src\main.py
	```
- Atau jalankan executable (jika sudah dibuat):
	```powershell
	.\bin\queen_solver.exe
	```
- Saat diminta, masukkan nama file input yang ada di folder `input`, misal `test1.txt`.
- Jika solusi ditemukan, program menampilkan papan dan menanyakan apakah ingin menyimpan. Menjawab `Y` akan membuat/menimpa berkas solusi di folder `test` dengan nama yang sama.

## Author
Geraldo Artemius (NIM 13524005) – K1 Strategi Algoritma.