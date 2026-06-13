# DiscordNotify

Windows desktop overlay that shows Discord server messages on your screen.

## How it works
- Messages from Discord server appear as a text on your screen
- Messages fade away after a set time
- Customizable position, fade duration, text color and size
- System tray icon to open/quit
- Toggle server notifications on or off

## How to use
1. Download DcNotify.exe and config.json from Releases
2. Put both files in the same folder ( you can name folder whatever you want)
3. Create a Discord bot at discord.com/developers/applications
4. Go to QAuth2 and in OAuth2 URL Generator choose bot
5. In Bot Permissions choose Administrator
6. Click the link at the very bottom and add bot at your server
7. Then go to bot and press reset token and copy your token
8. Run DcNotify.exe
9. Paste your token, set your preferences, click Save & Start
10. The app minimizes to your system tray - right click the icon to open or quit

## Tech stack
- Python 3.14
- discord.py
- tkinter
- pystray
- Pillow
- auto-py-to-exe
