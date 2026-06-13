import os
import tkinter as tk
from PIL import Image, ImageTk


root = tk.Tk()

root.title("Local AI Assistant")
root.geometry("1000x950")

title = tk.Label(
    root,
    text="Local AI Assistant",
    font=("Arial", 18)
)

title.pack(pady=10)

task_input = tk.Text(
    root,
    height=8
)

task_input.pack(
    fill="x",
    padx=20
)

from gui_runner import run_task

current_image_path = None


def open_image(event=None):

    global current_image_path

    if current_image_path:
        os.startfile(current_image_path)

run_button = tk.Button(
    root,
    text="Run Task",
    command=lambda: run_task(
        task_input.get(
            "1.0",
            "end-1c"
        ),
        output_box,
        image_label
    )
)

run_button.pack(pady=10)

output_box = tk.Text(
    root,
    height=4
)

output_box.pack(
    fill="x",
    padx=20,
    pady=10
)

image_label = tk.Label(
    root,
    cursor="hand2"
)

image_label.pack(
    pady=10
)

image_label.bind(
    "<Button-1>",
    open_image
)

root.mainloop()