
import tkinter as tk
from tkinter import filedialog
import os
import subprocess

def select_file():
    filepath = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4 *.avi *.mkv")])
    if filepath:
        input_path.set(filepath)

def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
    if filepath:
        output_path.set(filepath)

def run_processing():
    input_video = input_path.get()
    output_video = output_path.get()
    distortion = distortion_type.get()
    intensity = float(intensity_value.get())

    if not input_video or not output_video:
        status_label.config(text="Please specify input and output paths!", fg="red")
        return

    subprocess.run([
        "python", "main.py",
        "--input", input_video,
        "--output", output_video,
        "--type", distortion,
        "--intensity", str(intensity)
    ])

    status_label.config(text="Processing complete! Check output path.", fg="green")

root = tk.Tk()
root.title("Reality Distortion Field - GUI")

input_path = tk.StringVar()
output_path = tk.StringVar()
distortion_type = tk.StringVar(value="temporal")
intensity_value = tk.StringVar(value="1.0")

tk.Label(root, text="Input Video:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
tk.Entry(root, textvariable=input_path, width=50).grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=select_file).grid(row=0, column=2, padx=10, pady=5)

tk.Label(root, text="Output Video:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
tk.Entry(root, textvariable=output_path, width=50).grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text="Save As", command=save_file).grid(row=1, column=2, padx=10, pady=5)

tk.Label(root, text="Distortion Type:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
tk.OptionMenu(root, distortion_type, "temporal", "spatial", "glitch").grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Intensity (0.1 - 3.0):").grid(row=3, column=0, padx=10, pady=5, sticky="e")
tk.Entry(root, textvariable=intensity_value).grid(row=3, column=1, padx=10, pady=5)

tk.Button(root, text="Process Video", command=run_processing).grid(row=4, column=1, pady=10)
status_label = tk.Label(root, text="")
status_label.grid(row=5, column=1, pady=10)

root.mainloop()
    