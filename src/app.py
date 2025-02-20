import tkinter as tk
from tkinter import filedialog
from navigator import list_aiff_files
from player import MusicPlayer

class MusicPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AIFF Music Player")

        self.player = MusicPlayer()
        self.file_list = []
        self.selected_file = None

        # Frame para selecionar diretório
        self.dir_frame = tk.Frame(self.root)
        self.dir_frame.pack(pady=5)
        self.dir_button = tk.Button(self.dir_frame, text="Selecionar pasta", command=self.select_directory)
        self.dir_button.pack(side=tk.LEFT)

        # Lista de arquivos
        self.listbox = tk.Listbox(self.root, width=60)
        self.listbox.pack(pady=5)
        self.listbox.bind('<<ListboxSelect>>', self.on_file_select)

        # Botões de controle
        self.control_frame = tk.Frame(self.root)
        self.control_frame.pack(pady=5)

        self.play_button = tk.Button(self.control_frame, text="Play", command=self.play_song)
        self.play_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = tk.Button(self.control_frame, text="Stop", command=self.stop_song)
        self.stop_button.pack(side=tk.LEFT, padx=5)

    def select_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.file_list = list_aiff_files(directory)
            self.listbox.delete(0, tk.END)
            for f in self.file_list:
                self.listbox.insert(tk.END, f)

    def on_file_select(self, event):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            self.selected_file = self.file_list[index]

    def play_song(self):
        if self.selected_file:
            self.player.load(self.selected_file)
            self.player.play()

    def stop_song(self):
        self.player.stop()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayerApp(root)
    root.mainloop()
