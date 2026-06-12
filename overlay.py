import tkinter as tk
import threading
import settings

class Overlay:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.attributes("-transparentcolor", "black")
        self.root.configure(bg="black")
        self.root.geometry("400x300+100+100")
        self.messages = []
        self.lock = threading.Lock()

    def set_position(self, position):
        self.root.update_idletasks()
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        if position == "top-right":
            self.root.geometry(f"400x300+{sw - 420}+20")
        elif position == "top-left":
            self.root.geometry("400x300+20+20")
        elif position == "bottom-right":
            self.root.geometry(f"400x300+{sw - 420}+{sh - 320}")
        elif position == "bottom-left":
            self.root.geometry(f"400x300+20+{sh - 320}")

    def show_message(self, author, content, fade_duration):
        def run():
            with self.lock:
                label = tk.Label(
                    self.root,
                    text=f"{author}: {content}",
                    fg=settings.get("text_color"),
                    bg="black",
                    font=("Segoe UI", settings.get("text_size")),
                    wraplength=380,
                    justify="left"
                )
                label.pack(anchor="w", padx=10, pady=4)
                self.messages.append(label)
                self.root.after(int(fade_duration * 1000), lambda: self._remove(label))

        self.root.after(0, run)
    
    def _remove(self, label):
        label.destroy()
        if label in self.messages:
            self.messages.remove(label)

    def run(self):
        from settings import get
        self.set_position(get("position"))