# Youtube Video Downloader GUI

import tkinter as tk
from tkinter import filedialog, messagebox
from pytube import YouTube

def choose_folder():
    folder = filedialog.askdirectory()
    if folder:
        path_label.config(text=folder)
    else:
        path_label.config(text="No folder selected")

def download_video():
    url = url_entry.get()
    save_path = path_label.cget("text")

    if not url:
        messagebox.showerror("Error", "Please enter a Youtube URL!")
        return

    if save_path == "No folder selected":
        messagebox.showerror("Error", "Please select a folder to save video.")
        return

    try:
        yt = YouTube(url)
        stream = None

        quality = quality_var.get()
        if quality == "High":
            stream = yt.streams.get_highest_resolution()
        elif quality == "Low":
            stream = yt.streams.get_lowest_resolution()
        else:
            stream = yt.streams.filter(only_audio=True).first()

        messagebox.showinfo("Downloading", f"Downloading: {yt.title}")
        stream.download(save_path)
        messagebox.showinfo("Success", f"Download completed!\nSaved to: {save_path}")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video. \n{e}")


# GUI Setup


root = tk.Tk()
root.title("Youtube Video Downloader")
root.geometry("500x350")
root.resizable(False, False)

## URL Entry
tk.Label(root, text="Youtube URL:", font=("Arial", 12)).pack(pady=10)
url_entry = tk.Entry(root, width=55)
url_entry.pack(pady=5)

## Folder Selection
tk.Button(root, text="Choose Folder", command=choose_folder).pack(pady=5)
path_label = tk.Label(root, text="No folder selected", fg="gray")
path_label.pack(pady=5)

## Quality Options
tk.Label(root, text="Select Quality:", font=("Arial", 12)).pack(pady=5)
quality_var = tk.StringVar(value="High")

tk.Radiobutton(root, text="High Quality", variable=quality_var, value="High").pack()
tk.Radiobutton(root, text="Low Quality", variable=quality_var, value="Low").pack()
tk.Radiobutton(root, text="Audio Only", variable=quality_var, value="Audio").pack()

## Download Button
tk.Button(root, text="Download", command=download_video, bg="green", fg="white",
          width=15).pack(pady=20)

root.mainloop()