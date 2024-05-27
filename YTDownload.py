import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
from threading import Thread

class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("Baixador de Videos do Utube - By Omar Mario Moussa ")
        self.root.geometry("600x400")

        self.url_label = tk.Label(root, text="URL do vídeo:")
        self.url_label.pack()

        self.url_entry = tk.Entry(root, width=80)
        self.url_entry.pack()

        self.choose_path_button = tk.Button(root, text="Escolher Diretório", command=self.choose_path)
        self.choose_path_button.pack()

        self.download_button = tk.Button(root, text="Baixar Vídeo", command=self.download_video)
        self.download_button.pack()

        self.progress_bar = tk.Label(root, text="")
        self.progress_bar.pack()

        self.log_output = tk.Text(root, height=5, width=50)
        self.log_output.pack()

    def choose_path(self):
        self.save_path = filedialog.askdirectory()

    def log(self, message):
        self.log_output.insert(tk.END, message + "\n")
        self.log_output.see(tk.END)

    def download_video(self):
        url = self.url_entry.get()
        if url:
            self.log("Iniciando o download...")
            self.download_button.config(state="disabled")
            self.url_entry.config(state="disabled")
            self.choose_path_button.config(state="disabled")

            self.thread = Thread(target=self.download_thread, args=(url,))
            self.thread.start()

    def download_thread(self, url):
        try:
            yt = YouTube(url)
            video = yt.streams.get_highest_resolution()
            self.log("Baixando vídeo: {}".format(yt.title))
            video.download(self.save_path)
            self.log("Download completo!")
        except Exception as e:
            self.log("Erro ao baixar vídeo: {}".format(str(e)))
        finally:
            self.download_button.config(state="normal")
            self.url_entry.config(state="normal")
            self.choose_path_button.config(state="normal")

def main():
    root = tk.Tk()
    app = YouTubeDownloader(root)
    root.mainloop()

if __name__ == "__main__":
    main()
