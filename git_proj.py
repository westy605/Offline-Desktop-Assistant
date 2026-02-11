
import tkinter as tk
from tkinter import messagebox
import datetime
import random
import os

# ---------------- DATA ----------------
quotes = [
    "Keep going, you're doing great! ",
    "Small steps still move you forward ",
    "Consistency beats talent ",
    "You are learning real skills ",
    "Every bug you fix makes you better "
]

notes_file = "notes.txt"

# ---------------- FUNCTIONS ----------------
def get_time():
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")


def get_date():
    today = datetime.date.today()
    return today.strftime("%B %d, %Y")


def show_quote():
    quote = random.choice(quotes)
    messagebox.showinfo("Motivation", quote)


def save_note():
    text = note_entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "Note is empty!")
        return

    with open(notes_file, "a", encoding="utf-8") as f:
        f.write(text + "\n" + "-"*30 + "\n")

    note_entry.delete("1.0", tk.END)
    messagebox.showinfo("Saved", "Note saved locally!")


def load_notes():
    if not os.path.exists(notes_file):
        messagebox.showinfo("Notes", "No saved notes yet")
        return

    with open(notes_file, "r", encoding="utf-8") as f:
        data = f.read()

    notes_window = tk.Toplevel(root)
    notes_window.title("Your Notes")
    notes_window.geometry("400x400")

    text_area = tk.Text(notes_window, wrap=tk.WORD)
    text_area.pack(fill=tk.BOTH, expand=True)
    text_area.insert(tk.END, data)
    text_area.config(state=tk.DISABLED)


# ---------------- GUI ----------------
root = tk.Tk()
root.title("Offline Desktop Assistant")
root.geometry("450x500")
root.resizable(False, False)

header = tk.Label(root, text="Offline Desktop Assistant", font=("Arial", 16, "bold"))
header.pack(pady=10)

info_frame = tk.Frame(root)
info_frame.pack(pady=5)

clock_label = tk.Label(info_frame, text="", font=("Arial", 12))
clock_label.pack()

date_label = tk.Label(info_frame, text=f"{get_date()}", font=("Arial", 10))
date_label.pack()


def update_clock():
    clock_label.config(text=f"Time: {get_time()}")
    root.after(1000, update_clock)

update_clock()

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

quote_btn = tk.Button(btn_frame, text="Motivation Quote", width=20, command=show_quote)
quote_btn.grid(row=0, column=0, pady=5)

view_notes_btn = tk.Button(btn_frame, text="View Notes", width=20, command=load_notes)
view_notes_btn.grid(row=1, column=0, pady=5)

note_label = tk.Label(root, text="Quick Note:")
note_label.pack()

note_entry = tk.Text(root, height=8, width=45)
note_entry.pack(pady=5)

save_btn = tk.Button(root, text="Save Note Locally", width=25, command=save_note)
save_btn.pack(pady=10)

footer = tk.Label(root, text="Made by Westy---100% offline---no setup", font=("Arial", 9))
footer.pack(pady=10)

root.mainloop()

