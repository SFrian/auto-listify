import tkinter as tk
from tkinter import filedialog
import os

# Function to handle file selection
def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(title="Pilih file untuk diformat")
    return file_path

# Function to handle file save
def save_file(text, default_filename="formatted_list.txt"):
    root = tk.Tk()
    root.withdraw()
    save_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        initialfile=default_filename,
        title="Simpan hasil format"
    )
    if save_path:
        with open(save_path, "w", encoding="utf-8") as file:
            file.write(text)
        print(f"File berhasil disimpan di: {save_path}")
    else:
        print("Penyimpanan dibatalkan.")

# Define the function to format the text
def format_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]
    return ",".join(lines)

# Main function
def main():
    file_path = select_file()
    if not file_path:
        print("Tidak ada file yang dipilih.")
        return

    formatted_text = format_text(file_path)
    print("Formatted Text:", formatted_text)
    save_file(formatted_text)

if __name__ == "__main__":
    main()
