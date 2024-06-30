from main import main
from tkinter import Tk, filedialog
import os

def choose_directory(titulo):
    root = Tk()
    root.withdraw()  # Hide the main window
    data_directory = filedialog.askdirectory(title=titulo)
    return data_directory

def main_wrapper():
    data_directory = choose_directory("Selecione o Diretório com os Dados:")
    output_directory = choose_directory('Salver em:')
    main(data_directory, output_directory)

if __name__ == "__main__":
    main_wrapper()
