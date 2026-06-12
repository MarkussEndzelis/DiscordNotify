import discord
import threading
import tkinter as tk
from tkinter import ttk
import settings
from overlay import Overlay
import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw
from control_panel import ControlPanel

intents = discord.Intents.default()
intents.message_content = True
intents.dm_messages = True
intents.dm_messages = True
intents.guild_messages = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot running as {client.user}")
    panel.win.after(0, lambda: panel.set_status(True))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    is_dm = isinstance(message.channel, discord.DMChannel)
    if is_dm and not settings.get("show_dms"):
        return
    if not is_dm and not settings.get("show_channels"):
        return
    fade = settings.get("fade_duration")
    panel.win.after(0, lambda: overlay.show_message(
        message.author.display_name, message.content, fade))

def start_bot():
    token = settings.get("token")
    if token and token.strip():
        client.run(token)
    else:
        print("No token set - bot not started")

bot_started = False

def on_start():
    global bot_started
    overlay.set_position(settings.get("position"))
    panel._minimize()
    if not bot_started:
        bot_started = True
        bot_thread = threading.Thread(target=start_bot, daemon=True)
        bot_thread.start()

def quit_app():
    panel.win.quit()

def create_tray_icon():
    img = Image.new("RGB", (64, 64), color="#5865f2")
    draw = ImageDraw.Draw(img)
    draw.ellipse([16, 16, 48, 48], fill="white")

    def quit_tray(icon, i):
        icon.stop()
        panel.win.after(0, quit_app)

    def show_panel(icon, item):
        panel.win.after(0, panel.win.deiconify)

    menu = pystray.Menu(
        item("Open", show_panel),
        item("Quit", quit_tray)
    )
    icon = pystray.Icon("DcNotify", img, "DcNotify", menu)
    icon.run()

bot_started = False

panel = ControlPanel(on_start=on_start, on_quit=quit_app)
overlay = Overlay(panel.win)
overlay.run()

tray_thread = threading.Thread(target=create_tray_icon, daemon=True)
tray_thread.start()

panel.run()

