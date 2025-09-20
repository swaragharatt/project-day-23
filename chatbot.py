import tkinter as tk
from tkinter import font
import random

bot_responses = {
    "hello": ["Hi there!", "Hello!", "Hey!", "Hi! How can I help you today?"],
    "hey": ["Hey! Nice to see you!", "Hey there!", "Hello! How's it going?"],
    "how are you": ["I'm doing great, thanks!", "I'm fine, how about you?"],
    "your name": ["I'm Gemmy, your Python chatbot.", "Call me Gemmy!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"]
}

def get_bot_reply(message):
    message = message.lower()
    for key in bot_responses:
        if key in message:
            return random.choice(bot_responses[key])
    return "I'm not sure how to respond to that yet."

root = tk.Tk()
root.title("Python Chatbot")
root.geometry("520x650")
root.configure(bg="#1E1E1E")

try:
    font.Font(family="Orbitron")
    title_font = "Orbitron"
except tk.TclError:
    title_font = "Press Start 2P"

chat_font = "Courier New"

title_label = tk.Label(root, text="💬 gemmy", font=(title_font, 24, "bold"), fg="#E0BBE4", bg="#1E1E1E")
title_label.pack(pady=(15, 10))

canvas = tk.Canvas(root, bg="#1E1E1E", highlightthickness=0)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#1E1E1E")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="top", fill="both", expand=True, padx=(10,0), pady=(0,0))
scrollbar.pack(side="right", fill="y", pady=(0,0))

def add_message(message, sender="user"):
    bubble_color = "#9C27B0" if sender == "user" else "#C9C9C9"
    text_color = "#FFFFFF"
    anchor_side = "w" if sender == "user" else "e"

    bubble = tk.Label(scrollable_frame, text=message, font=(chat_font, 13),
                      bg=bubble_color, fg=text_color, padx=12, pady=8,
                      wraplength=360, justify="left", anchor="w")
    bubble.pack(anchor=anchor_side, pady=5, padx=10)
    canvas.update_idletasks()
    canvas.yview_moveto(1)

def send_message(event=None):
    msg = entry_box.get().strip()
    if not msg or msg == "Type your message here...":
        return
    add_message(msg, "user")
    entry_box.delete(0, tk.END)
    reply = get_bot_reply(msg)
    add_message(reply, "bot")

input_frame = tk.Frame(root, bg="#1E1E1E")
input_frame.pack(side="bottom", fill="x", padx=10, pady=10)

entry_box = tk.Entry(input_frame, font=(chat_font, 14), fg="#6A5ACD", bg="#2A2A2A",
                     relief=tk.FLAT, bd=0, insertbackground="#E0BBE4")
entry_box.pack(side="left", fill="x", expand=True, padx=(0,10), ipady=8)
entry_box.insert(0, "Type your message here...")

def clear_placeholder(event):
    if entry_box.get() == "Type your message here...":
        entry_box.delete(0, tk.END)
        entry_box.config(fg="#E0BBE4")

def restore_placeholder(event):
    if not entry_box.get():
        entry_box.insert(0, "Type your message here...")
        entry_box.config(fg="#6A5ACD")

entry_box.bind("<FocusIn>", clear_placeholder)
entry_box.bind("<FocusOut>", restore_placeholder)

send_btn = tk.Button(input_frame, text="Send", font=(chat_font, 14, "bold"),
                     bg="#882D9E", fg="#FFFFFF", relief=tk.FLAT,
                     activebackground="#9C27B0", activeforeground="#FFFFFF",
                     command=send_message)
send_btn.pack(side="right", ipadx=18, ipady=7)

root.bind("<Return>", send_message)

root.mainloop()
