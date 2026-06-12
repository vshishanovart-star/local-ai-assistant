import tkinter as tk


root = tk.Tk()

root.title("Local AI Assistant")
root.geometry("800x500")

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

run_button = tk.Button(
    root,
    text="Run Task"
)

run_button.pack(pady=10)

output_box = tk.Text(
    root
)

output_box.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=10
)

root.mainloop()