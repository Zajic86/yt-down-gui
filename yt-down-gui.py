import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube
import tkinter.font as tkfont


def download_content():
    url = url_entry.get()
    choice = choice_var.get()
    save_path = save_path_var.get()

    if not url:
        info_text.set("YouTube video URL")
        return

    if not save_path:
        info_text.set("Save path")
        return

    if choice == "Video":
        video = YouTube(url)
        stream = video.streams.get_highest_resolution()
        stream.download(output_path=save_path)
        messagebox.showinfo("Download complete", "Video downloaded to: " + save_path)
    elif choice == "Audio":
        video = YouTube(url)
        stream = video.streams.filter(only_audio=True).first()
        stream.download(output_path=save_path)
        messagebox.showinfo("Download complete", "Audio downloaded to: " + save_path)
    else:
        info_text.set("Wrong choice")


def browse_path():
    path = filedialog.askdirectory()
    save_path_var.set(path)


def exit_program():
    root.quit()


# Create main window
root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("400x320")  # Dimensions

bold_font = tkfont.Font(family="Helvetica", size=12, weight="bold")

# create url field
url_label = ttk.Label(root, text="Paste YouTube URL", font=bold_font)
url_label.pack(pady="5")
url_entry = ttk.Entry(root)
url_entry.pack(fill="x", padx="10")

# create radiobuttons () video, () only audio
choice_label = ttk.Label(root, text="video / audio only", font=bold_font)
choice_label.pack(pady="5")
choice_var = tk.StringVar()
choice_var.set("Video")
video_radio = ttk.Radiobutton(root, text="Video", variable=choice_var, value="Video")
audio_radio = ttk.Radiobutton(root, text="Audio", variable=choice_var, value="Audio")
video_radio.pack()
audio_radio.pack()

# drop-down list for path
save_path_label = ttk.Label(root, text="Choose path:", font=bold_font)
save_path_label.pack(pady="5")
save_path_var = tk.StringVar()
save_path_combobox = ttk.Combobox(root, textvariable=save_path_var)
save_path_combobox.pack(fill="x", padx="10")
browse_button = ttk.Button(root, text="Browse...", command=browse_path)
browse_button.pack(pady="2")

# download button
download_button = ttk.Button(root, text="Download", command=download_content, style="Green.TButton")
download_button.pack(pady="3", fill="x", padx="10")

# exit button
exit_button = ttk.Button(root, text="Exit", command=exit_program, style="Red.TButton")
exit_button.pack(pady="3")

# text field for info
info_text = tk.StringVar()
info_label = ttk.Label(root, textvariable=info_text)
info_label.pack()

# buttons
style = ttk.Style()
style.configure("Red.TButton", foreground="white", background="red")
style.configure("Green.TButton", foreground="white", background="green")
style.map("Red.TButton", background=[("active", "darkred")], foreground=[("active", "white")])
style.map("Green.TButton", background=[("active", "darkgreen")], foreground=[("active", "white")])

root.mainloop()
