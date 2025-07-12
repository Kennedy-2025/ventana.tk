from ttkbootstrap import Style, Window, ttk
from ttkbootstrap.constants import *
from tkinter import StringVar
from datetime import datetime

# Temas personalizados
CUSTOM_THEMES = {
    "midnight": {
        "type": "dark",
        "colors": {
            "primary": "#0a21f5",
            "secondary": "#555555",
            "success": "#77b300",
            "info": "#c6c6c6",
            "warning": "#ff8800",
            "danger": "#cc0000",
            "light": "#adafae",
            "dark": "#000000",
            "bg": "#000000",
            "fg": "#ffffff",
            "selectbg": "#454545",
            "selectfg": "#ffffff",
            "border": "#060606",
            "inputfg": "#ffffff",
            "inputbg": "#191919",
            "active": "#282828"
        }
    },
    "nightout": {
        "type": "dark",
        "colors": {
            "primary": "#164fe2",
            "secondary": "#555555",
            "success": "#77b300",
            "info": "#c0c0c0",
            "warning": "#ff8800",
            "danger": "#cc0000",
            "light": "#ADAFAE",
            "dark": "#222222",
            "bg": "#000000",
            "fg": "#ffffff",
            "selectbg": "#454545",
            "selectfg": "#ffffff",
            "border": "#060606",
            "inputfg": "#ffffff",
            "inputbg": "#191919",
            "active": "#282828"
        }
    }
}

# Crear estilo y registrar temas
style = Style()
for name, data in CUSTOM_THEMES.items():
    style.register_theme(name, data)

# Ventana principal
app = Window(title="Demo ttkbootstrap avanzada", themename="midnight", size=(600, 400))

# Variable y Combobox para cambiar tema
theme_var = StringVar(value="midnight")
def cambiar_tema(event=None):
    try:
        style.theme_use(theme_var.get())
    except Exception as e:
        print(f"Error al cambiar el tema: {e}")

ttk.Label(app, text="Selecciona un tema:", font=("Helvetica", 12)).pack(pady=10)
combo = ttk.Combobox(app, textvariable=theme_var, values=list(CUSTOM_THEMES.keys()), state="readonly")
combo.pack()
combo.bind("<<ComboboxSelected>>", cambiar_tema)

# Frame para botones
frame_btn = ttk.Frame(app)
frame_btn.pack(pady=10)
ttk.Button(frame_btn, text="Primary", bootstyle=PRIMARY).pack(side=LEFT, padx=5)
ttk.Button(frame_btn, text="Success", bootstyle=SUCCESS).pack(side=LEFT, padx=5)
ttk.Button(frame_btn, text="Danger", bootstyle=DANGER).pack(side=LEFT, padx=5)

# Entry y DateEntry
ttk.Entry(app).pack(pady=5)
date_entry = ttk.DateEntry(app, bootstyle=PRIMARY, dateformat="%Y-%m-%d")
date_entry.set_date(datetime.now())
date_entry.pack(pady=5)

# Meter (medidor)
def actualizar_meter(value):
    print(f"Valor del medidor: {value}")
meter = ttk.Meter(app, bootstyle="info", amountused=45, amounttotal=100, metertype="full",
                  interactive=True, command=actualizar_meter, textfont=("Helvetica", 20, "bold"))
meter.pack(pady=15)

# Progressbar
def actualizar_progreso():
    progress['value'] = (progress['value'] + 10) % 100
progress = ttk.Progressbar(app, bootstyle="warning", length=200, mode="determinate")
progress.pack(pady=5)
progress['value'] = 70
ttk.Button(app, text="Actualizar Progreso", command=actualizar_progreso).pack(pady=5)

# Toggle buttons
toggle_frame = ttk.Frame(app)
toggle_frame.pack(pady=10)
ttk.Checkbutton(toggle_frame, text="Toggle redondeado", bootstyle="success-toggle-round").pack(side=LEFT, padx=5)
ttk.Checkbutton(toggle_frame, text="Toggle cuadrado", bootstyle="info-toggle-square").pack(side=LEFT, padx=5)

# Ejecutar app
app.mainloop()