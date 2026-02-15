import os
import time
from board import isBoardValid, groupColours, printBoard
from file_processing import readBoard, saveSolution, saveImage
from queens import solveQueenPositions

def main():
    base = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    while True:
        file = input("Masukkan nama file (.txt) dari folder input: ")
        filePath = os.path.join(base,"input", file)
        
        if not os.path.exists(filePath):
            print("File tidak ditemukan!\n")
            continue
        
        board = readBoard(filePath)
        if not isBoardValid(board):
            print("Ukuran board queen tidak valid! (N x N)\n")
            continue
        
        colours = groupColours(board)
        
        print("\n\nMencari solusi untuk board pada file:", file,"\n")
        
        start = time.perf_counter()
        found, solution, count = solveQueenPositions(colours)
        end = time.perf_counter()
        
        elapseTime = (end - start) * 1000
        
        if found :
            print("Solusi ditemukan!\nMenampilkan solusi : \n")
            printBoard(board, solution)
            
            print(f"\n\nWaktu pencarian: {round(elapseTime,2)} ms\n")
            print(f"Banyak kasus yang ditinjau: {count} kasus\n")
            choice = input("Apakah Anda ingin menyimpan solusi? (Y/N): ")
            
            if choice.lower() == 'y':
                fmt = input("Pilih format (1=txt, 2=png): ").strip()
                if fmt == '2':
                    img_dir = os.path.join(base, "test", "image")
                    os.makedirs(img_dir, exist_ok=True)
                    pngPath = os.path.join(img_dir, os.path.splitext(file)[0] + ".png")
                    if saveImage(board, solution, pngPath):
                        print(f"Solusi PNG disimpan di {pngPath}\n")
                else:
                    txt_dir = os.path.join(base, "test", "text")
                    os.makedirs(txt_dir, exist_ok=True)
                    savePath = os.path.join(txt_dir, file)
                    saveSolution(savePath, board, solution, round(elapseTime,2), count)
                    print("Solusi TXT disimpan dalam folder test/text\n")
        else :
            print("Solusi tidak ditemukan!\n")
            print(f"\n\nWaktu pencarian: {round(elapseTime,2)} ms\n")
            print(f"Banyak kasus yang ditinjau: {count} kasus\n")
            
            
            
def printBanner():
    print("-------------------- Selamat datang di program QUEENS LinkedIn SOLVER --------------------")
    print("  ___   __ __    ___    ___  ____   _____      _____  ___   _      __ __    ___  ____  ")
    print(" /   \\ |  |  |  /  _]  /  _]|    \\ / ___/     / ___/ /   \\ | |    |  |  |  /  _]|    \\ ")
    print("|     ||  |  | /  [_  /  [_ |  _  (   \\_     (   \\_ |     || |    |  |  | /  [_ |  D  )")
    print("|  Q  ||  |  ||    _]|    _]|  |  |\\__  |     \\__  ||  O  || |___ |  |  ||    _]|    / ")
    print("|     ||  :  ||   [_ |   [_ |  |  |/  \\ |     /  \\ ||     ||     ||  :  ||   [_ |    \\ ")
    print("|     ||     ||     ||     ||  |  |\\    |     \\    ||     ||     | \\   / |     ||  .  \\")
    print(" \\__,_| \\__,_||_____||_____||__|__| \\___|      \\___| \\___/ |_____|  \\_/  |_____||__|\\_|")
    print("\n\n")
    
            
if __name__ == "__main__":
    printBanner()
    main()
                
                