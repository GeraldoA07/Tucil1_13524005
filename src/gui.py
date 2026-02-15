import os
import time
import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageTk

from board import isBoardValid, groupColours
from file_processing import readBoard, saveSolution, saveImage
from queens import solveQueenPositions

ctk.set_appearance_mode("light") 
ctk.set_default_color_theme("blue")

basePath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
crownPath = os.path.join(basePath, "assets", "crown.png")

colorPalette = [
    "#C6E0B4", "#FFE699", "#A9D18E", "#F4B6B6", "#9DC3E6",
    "#B4A7D6", "#D996B6", "#F9CB9C", "#A2C4C9", "#D9D9D9",
    "#93C47D", "#FFD966", "#6FA8DC", "#E06666", "#8E7CC3",
    "#C27BA0", "#F6B26B", "#76A5AF", "#B7B7B7", "#B6D7A8"
]

def getColour(colourMap, key):
    key = key.upper()
    if key not in colourMap:
        colourMap[key] = colorPalette[len(colourMap) % len(colorPalette)]
    return colourMap[key] 

class QueensGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Queens Solver Pro")
        self.geometry("600x250") 
        self.configure(fg_color="#FFFFFF")
        self.resizable(False, False)
        
        self.curBoard = None
        self.curSol = None
        self.curInput = "solution"
        
        self.crownTk = None
        self.crownBase = Image.open(crownPath).convert("RGBA")

        self.headerFrame = ctk.CTkFrame(self, fg_color="transparent")
        self.headerFrame.pack(pady=(30, 10), fill="x")

        self.titleLabel = ctk.CTkLabel(
            self.headerFrame, 
            text="Queens Solver", 
            font=ctk.CTkFont(family="Segoe UI", size=32, weight="bold")
        )
        self.titleLabel.pack()

        self.buttonFrame = ctk.CTkFrame(self, fg_color="transparent")
        self.buttonFrame.pack(pady=10)

        self.btnManual = ctk.CTkButton(
            self.buttonFrame, text="Input Manual", 
            command=self.inputManual, corner_radius=12, font=("Segoe UI", 14, "bold"),
            height=40, width=160
        )
        self.btnManual.grid(row=0, column=0, padx=15)

        self.btnFile = ctk.CTkButton(
            self.buttonFrame, text="Input File TXT", 
            command=self.inputFile, corner_radius=12, font=("Segoe UI", 14, "bold"),
            height=40, width=160
        )
        self.btnFile.grid(row=0, column=1, padx=15)

        self.mainContainer = ctk.CTkFrame(self, fg_color="#F0F2F5", corner_radius=20)
        
        self.canvas = tk.Canvas(
            self.mainContainer, 
            bg="#F0F2F5", 
            highlightthickness=0, 
            bd=0
        )
        self.canvas.pack(pady=20, padx=20)

        self.saveButton = ctk.CTkButton(
            self, text="Save Solution Image", 
            command=self.saveSolution, 
            fg_color="#28a745", hover_color="#218838",
            corner_radius=12, font=("Segoe UI", 14, "bold"),
            height=40
        )

    def inputFile(self):
        filePath = filedialog.askopenfilename(
            initialdir=os.path.join(basePath, "input"),
            filetypes=[("Text Files", "*.txt")]
        )
        if filePath:
            self.curInput = os.path.splitext(os.path.basename(filePath))[0]
            boardData = readBoard(filePath)
            self.processBoard(boardData)

    def showDialog(self, n):
        result = {"data": None}
        
        dialog = ctk.CTkToplevel(self)
        dialog.title("Input Board Configuration")
        dialog.geometry("400x450")
        dialog.grab_set() 
        dialog.resizable(False, False)

        label = ctk.CTkLabel(dialog, text=f"Masukkan konfigurasi board {n}x{n}:", font=("Segoe UI", 13, "bold"))
        label.pack(pady=(15, 5))

        textbox = ctk.CTkTextbox(dialog, width=350, height=250, border_width=2)
        textbox.pack(padx=20, pady=10) 
        
        def submit():
            result["data"] = textbox.get("1.0", "end-1c")
            dialog.destroy()

        def cancel():
            dialog.destroy()

        btn_frame = ctk.CTkFrame(dialog, fg_color="transparent")
        btn_frame.pack(pady=15)

        ctk.CTkButton(btn_frame, text="Submit", width=100, command=submit).grid(row=0, column=0, padx=10)
        ctk.CTkButton(btn_frame, text="Cancel", width=100, fg_color="#aaaaaa", hover_color="#888888", command=cancel).grid(row=0, column=1, padx=10)

        self.wait_window(dialog)
        return result["data"]

    def inputManual(self):
        inputSize = ctk.CTkInputDialog(text="Masukkan ukuran N:", title="Board Size").get_input()
        
        if not inputSize or not inputSize.isdigit():
            return
            
        boardSize = int(inputSize)
        inputBoard = self.showDialog(boardSize)
        
        if inputBoard:
            board = inputBoard.strip().split("\n")
            if len(board) != boardSize:
                messagebox.showerror("Error", f"Jumlah baris harus {boardSize}.")
                return

            self.curInput = f"manual_{boardSize}x{boardSize}"
            self.processBoard(board)

    def processBoard(self, boardData):
        if not isBoardValid(boardData):
            messagebox.showerror("Error", "Board tidak valid!")
            return

        colourGroups = groupColours(boardData)
        startTime = time.perf_counter()
        isFound, solutionData, caseCount = solveQueenPositions(colourGroups)
        endTime = time.perf_counter()
        elapsedTime = (endTime - startTime) * 1000

        if not isFound:
            messagebox.showinfo("Result", "Solusi tidak ditemukan.")
            return

        self.curBoard = boardData
        self.curSol = solutionData
        self.lastElapsed = round(elapsedTime)
        self.lastCaseCount = caseCount
        
        self.drawBoard()
        self.mainContainer.pack(pady=20, padx=40)
        self.saveButton.pack(pady=(10, 30))
        
        self.update_idletasks()
        newHeight = self.winfo_reqheight()
        self.geometry(f"600x{newHeight}")
        
        messagebox.showinfo("Success", f"Selesai dalam {round(elapsedTime)} ms\nKasus: {caseCount}")

    def drawBoard(self):
        self.canvas.delete("all")
        nSize = len(self.curBoard)
        
        maxCellSize = 400 // nSize
        cellSize = min(50, maxCellSize) 
        totalPixelSize = nSize * cellSize

        self.canvas.config(width=totalPixelSize, height=totalPixelSize)

        colourMap = {}
        queenPositions = set(self.curSol.values())
        pilCrown = Image.open(crownPath).convert("RGBA")
        resizedCrown = pilCrown.resize((int(cellSize * 0.7), int(cellSize * 0.7)), Image.LANCZOS)
        self.crownTk = ImageTk.PhotoImage(resizedCrown)
        self.crownBase = self.crownBase  

        for r in range(nSize):
            for c in range(nSize):
                x1, y1 = c * cellSize, r * cellSize
                x2, y2 = x1 + cellSize, y1 + cellSize

                cellFill = getColour(colourMap, self.curBoard[r][c])
                
                self.canvas.create_rectangle(
                    x1, y1, x2, y2, 
                    fill=cellFill, 
                    outline="#FFFFFF", 
                    width=2
                )

                if (r, c) in queenPositions:
                    self.canvas.create_image(
                        (x1 + x2) / 2, (y1 + y2) / 2,
                        image=self.crownTk,
                    )
                    

    def saveSolution(self):
        if not self.curBoard or not self.curSol: 
            return
        imgDir = os.path.join(basePath, "test", "image")
        txtDir = os.path.join(basePath, "test", "text")
        os.makedirs(imgDir, exist_ok=True)
        os.makedirs(txtDir, exist_ok=True)
        defaultStem = self.curInput

        choice = {"val": None}
        dlg = ctk.CTkToplevel(self)
        dlg.title("Simpan sebagai")
        dlg.resizable(False, False)
        dlg.grab_set()
        
        def choosePNG():
            choice["val"] = "png"
            dlg.destroy()

        def chooseTXT():
            choice["val"] = "txt"
            dlg.destroy()

        def chooseCancel():
            choice["val"] = None
            dlg.destroy()

        ctk.CTkLabel(dlg, text="Pilih format penyimpanan:", font=("Segoe UI", 14, "bold")).pack(padx=20, pady=(15, 10))
        btn_frame = ctk.CTkFrame(dlg, fg_color="transparent")
        btn_frame.pack(pady=(0, 15))

        ctk.CTkButton(btn_frame, text="PNG", width=90,
                      command=choosePNG).grid(row=0, column=0, padx=6)
        ctk.CTkButton(btn_frame, text="TXT", width=90,
                      command=chooseTXT).grid(row=0, column=1, padx=6)
        ctk.CTkButton(btn_frame, text="Cancel", width=90, fg_color="#aaaaaa", hover_color="#888888",
                      command=lambda: (choice.update(val=None), dlg.destroy())).grid(row=0, column=2, padx=6)

        dlg.wait_window()
        if choice["val"] is None:
            return

        if choice["val"] == "png":
            targetPath = os.path.join(imgDir, defaultStem + ".png")
            saveImage(self.curBoard, self.curSol, targetPath)
            messagebox.showinfo("Saved", f"Berhasil disimpan ke {targetPath}!")
        else:
            targetPath = os.path.join(txtDir, defaultStem + ".txt")
            saveSolution(targetPath, self.curBoard, self.curSol, self.lastElapsed, self.lastCaseCount)
            messagebox.showinfo("Saved", f"Berhasil disimpan ke {targetPath}!")

if __name__ == "__main__":
    app = QueensGUI()
    app.mainloop()