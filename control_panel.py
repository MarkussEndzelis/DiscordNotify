import tkinter as tk
from tkinter import ttk
import settings

class ControlPanel:
    def __init__(self, on_start, on_quit):
        self.on_start = on_start
        self.on_quit = on_quit
        self.win = tk.Tk()
        self.win.title("DcNotify")
        self.win.geometry("320x560")
        self.win.configure(bg="#1e1e2e")
        self.win.resizable(False, False)
        self.win.protocol("WM_DELETE_WINDOW", self._minimize)
        self._build()

    def _build(self):
        tk.Label(self.win, text="DcNotify", fg="white", bg="#1e1e2e", font=("Segoe UI", 20, "bold")).pack(pady=(24, 4))
        tk.Label(self.win, text="Discord message overlay", fg="#576574", bg="#1e1e2e", font=("Segoe UI", 10)).pack(pady=(0, 20))

        self.status_label = tk.Label(self.win, text="Not connected", fg="#576574", bg="#1e1e2e", font=("Segoe UI", 11))
        self.status_label.pack(pady=(0, 20))

        cfg = settings.load()

        self._row("Bot Token:", "token", cfg, show="*")
        self._row("Fade Duration (sec):", "fade_duration", cfg)
        self._position_row(cfg)
        self._check_row("Show DMs", "show_dms", cfg)
        self._check_row("Show Channels", "show_channels", cfg)
        self._color_row(cfg)
        self._size_row(cfg)

        tk.Button(self.win, text="Save & Start", command=self._save_and_start, bg="#5865f2", fg="white", font=("Segoe UI", 11),
                  padx=20, pady=8, borderwidth=0, cursor="hand2").pack(pady=(20, 8), fill="x", padx=30)
        
        tk.Button(self.win, text="Quit", command=self.on_quit, bg="#2f3542", fg="white", font=("Segoe UI", 11),
                  padx=20, pady=8, borderwidth=0, cursor="hand2").pack(fill="x", padx=30)
        
    def _row(self, label, key, cfg, show=None):
        tk.Label(self.win, text=label, fg="#a0a0b0", bg="#1e1e2e",
                 font=("Segoe UI", 10)).pack(anchor="w", padx=30)
        var = tk.StringVar(value=str(cfg.get(key, "")))
        entry = tk.Entry(self.win, textvariable=var, bg="#2f3542", fg="white",
                         insertbackground="white", font=("Segoe UI", 10),
                         borderwidth=0, show=show or "")
        entry.pack(fill="x", padx=30, pady=(2, 8))
        setattr(self, f"var_{key}", var)

    def _position_row(self, cfg):
        tk.Label(self.win, text="Position:", fg="#a0a0b0", bg="#1e1e2e",
                 font=("Segoe UI", 10)).pack(anchor="w", padx=30)
        self.var_position = tk.StringVar(value=cfg.get("position", "top-right"))
        ttk.Combobox(self.win, textvariable=self.var_position, values=[
            "top-right", "top-left", "bottom-right", "bottom-left"
        ], width=20, state="readonly").pack(anchor="w", padx=30, pady=(2, 8))

    def _check_row(self, label, key, cfg):
        var = tk.BooleanVar(value=cfg.get(key, True))
        tk.Checkbutton(self.win, text=label, variable=var, bg="#1e1e2e",
                       fg="white", selectcolor="#2f3542",
                       font=("Segoe UI", 10)).pack(anchor="w", padx=30)
        setattr(self, f"var_{key}", var)

    def _color_row(self, cfg):
        tk.Label(self.win, text="Text Color:", fg="#a0a0b0", bg="#1e1e2e", font=("Segoe UI", 10)).pack(anchor="w", padx=30)
        frame = tk.Frame(self.win, bg="#1e1e2e")
        frame.pack(anchor="w", padx=30, pady=(2, 8))
        self.var_text_color = tk.StringVar(value=cfg.get("text_color", "#ffffff"))
        colors = ["#ffffff", "#ffd700", "#00cfff", "#ff6b6b", "#2ed573"]
        for c in colors:
            tk.Button(frame, bg=c, width=2, height=1, borderwidth=0,
                      cursor="hand2",
                      command=lambda col=c: self.var_text_color.set(col)).pack(side="left", padx=2)

    def _size_row(self, cfg):
        tk.Label(self.win, text="Text Size:", fg="#a0a0b0", bg="#1e1e2e",
                 font=("Segoe UI", 10)).pack(anchor="w", padx=30)
        self.var_text_size = tk.IntVar(value=cfg.get("text_size", 13))
        tk.Spinbox(self.win, from_=10, to=24, textvariable=self.var_text_size,
                   width=5, bg="#2f3542", fg="white", buttonbackground="#2f3542",
                   font=("Segoe UI", 10)).pack(anchor="w", padx=30, pady=(2, 8))        

    def _save_and_start(self):
        settings.set("token", self.var_token.get())
        settings.set("fade_duration", int(self.var_fade_duration.get()))
        settings.set("position", self.var_position.get())
        settings.set("show_dms", self.var_show_dms.get())
        settings.set("show_channels", self.var_show_channels.get())
        settings.set("text_color", self.var_text_color.get())
        settings.set("text_size", self.var_text_size.get())
        self.on_start()

    def set_status(self, connected):
        if connected:
            self.status_label.config(text="Connected", fg="#2ed573")
        else:
            self.status_label.config(text="Disconnected", fg="#ff4757")

    def _minimize(self):
        self.win.withdraw()

    def run(self):
        self.win.mainloop()