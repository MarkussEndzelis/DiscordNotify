# DiscordNotify

Windows desktop overlay that shows Discord server messages on your screen.

## How it works
- Messages from Discord server appear as a text on your screen
- Messages fade away after a set time
- Customizable position, fade duration, text color and size
- System tray icon to open/quit
- Toggle server notifications on or off

## How to use
1. Download DcNotify.exe from Releases
2. Create new folder on your pc(e.g. Dekstop) and name it whatever you want
3. Put DcNotify.exe file in folder that you made
4. Create a Discord bot at discord.com/developers/applications
5. Go to Bot and in Privileged Gateway Intents check all of these: Presence Intent, Server Members Intent, Message Content Intent
6. Go to QAuth2 and in OAuth2 URL Generator choose bot
7. In Bot Permissions choose Administrator
8. Click the link at the very bottom and add bot at your server
9. Then go to bot and press reset token and copy your token
10. Run DcNotify.exe inside you folder
11. Paste your token, set your preferences, click Save & Start
12. The app minimizes to your system tray - right click the icon to open or quit

If something doesnt work, try:
- Resetting token in Bot, Token
- Reinviting Bot by doing 6., 7., 8. step

## Tech stack
- Python 3.14
- discord.py
- tkinter
- pystray
- Pillow
- auto-py-to-exe
