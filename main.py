import discord
import threading
import tkinter as tk
from tkinter import ttk
import settings
from overlay import Overlay

overlay = Overlay()

intents = discord.Intents.default()
intents.message_content = True
intents.dm_messages = True
intents.dm_messages = True
intents.guild_messages = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot running as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    is_dm = isinstance(message.channel, discord.DMChannel)
    show_dms = settings.get("show_dms")
    show_channels = settings.get("show_channels")
    if is_dm and not show_dms:
        return
    if not is_dm and not show_channels:
        return
    fade = settings.get("fade_duration")
    overlay.show_message(message.author.display_name, message.content, fade)

def start_bot():
    token = settings.get("token")
    if token and token.strip():
        client.run(token)
    else:
        print("No token set - bot not started")

def launch_settings_window():
    cfg = settings.load()
    win = tk.Toplevel()
    win.title("DcNotify Settings")
    win.geometry("360x320")
    win.configure(bg="#1e1e2e")
    win.resizable(False, False)

    def label(text, row):
        tk.Label(win, text=text, fg="white", bg="#1e1e2e", 
                 font=("Segoe UI", 11)).grid(row=row, column=0, padx=20, pady=8, sticky="w")
        
    label("Bot Token:", 0)
    token_var = tk.StringVar(value=cfg["token"])
    tk.Entry(win, textvariable=token_var, width=30, show="*").grid(row=0, column=1, padx=10)

    label("Fade Duration (sec):", 1)
    fade_var = tk.IntVar(value=cfg["fade_duration"])
    tk.Spinbox(win, from_=1, to=30, textvariable=fade_var, width=5).grid(row=1, column=1, padx=10, sticky="w")

    label("Position:", 2)
    pos_var = tk.StringVar(value=cfg["position"])
    ttk.Combobox(win, textvariable=pos_var, values=[
        "top-right", "top-left", "bottom-right", "bottom-left"
    ], width=15, state="readonly").grid(row=2, column=1, padx=10, sticky="w")

    label("Show DMs:", 3)
    dm_var = tk.BooleanVar(value=cfg["show_dms"])
    tk.Checkbutton(win, variable=dm_var, bg="#1e1e2e").grid(row=3, column=1, sticky="w", padx=10)

    label("Show Channels:", 4)
    ch_var = tk.BooleanVar(value=cfg["show_channels"])
    tk.Checkbutton(win, variable=ch_var, bg="#1e1e2e").grid(row=4, column=1, sticky="w", padx=10)

    def save_and_close():
        settings.set("token", token_var.get())
        settings.set("fade_duration", fade_var.get())
        settings.set("position", pos_var.get())
        settings.set("show_dms", dm_var.get())
        settings.set("show_channels", ch_var.get())
        overlay.set_position(pos_var.get())
        win.destroy()

    tk.Button(win, text="Save", command=save_and_close,
              bg="#5865f2", fg="white", font=("Segoe UI", 11),
              padx=20, pady=6).grid(row=5, column=0, columnspan=2, pady=20)
    
btn = tk.Button(
    overlay.root,
    text="⚙",
    command=launch_settings_window,
    bg="black",
    fg="#576574",
    font=("Segoe UI", 10),
    borderwidth=0,
    cursor="hand2"
)
btn.place(relx=1.0, rely=0.0, anchor="ne")
overlay.show_message("Test", "Hello this is a test message", 5)

bot_thread = threading.Thread(target=start_bot, daemon=True)
bot_thread.start()

overlay.run()
        

    