import os
import time
from board import isBoardValid, groupColours, printBoard
from file_processing import readBoard, saveSolution
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
            
            print(f"\n\nWaktu pencarian: {round(elapseTime)} ms\n")
            print(f"Banyak kasus yang ditinjau: {count} kasus\n")
            choice = input("Apakah Anda ingin menyimpan solusi? (Y/N): ")
            
            if choice.lower() == 'y':
                if not os.path.exists(os.path.join(base, "test")):
                    os.makedirs(os.path.join(base, "test"))
                
                savePath = os.path.join(base,"test", file)
                saveSolution(savePath, board, solution, round(elapseTime), count)
                print("Solusi berhasil disimpan dalam folder test\n")
        else :
            print("Solusi tidak ditemukan!\n")
            
if __name__ == "__main__":
    main()
                
                