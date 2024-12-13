import tkinter as tk

def add_tooltip(widget, text):
    tooltip_window = None

    def show_tooltip(event=None):
        nonlocal tooltip_window
        x, y, _, _ = widget.bbox("insert")
        x += widget.winfo_rootx() + 25
        y += widget.winfo_rooty() + 20

        tooltip_window = tk.Toplevel(widget)
        tooltip_window.wm_overrideredirect(True)  # Sin barra de título
        tooltip_window.wm_geometry(f"+{x}+{y}")

        label = tk.Label(
            tooltip_window,
            text=text,
            background="lavender",
            foreground="black",
            borderwidth=1,
            relief="solid",
            font=("Helvetica", 10)
        )
        label.pack(ipadx=5, ipady=2)

    def hide_tooltip(event=None):
        nonlocal tooltip_window
        if tooltip_window:
            tooltip_window.destroy()
            tooltip_window = None

    widget.bind("<Enter>", show_tooltip)
    widget.bind("<Leave>", hide_tooltip)
