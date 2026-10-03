"""
Dock dinamico en Python para Windows.
"""

import json
import os
import tkinter as tk

# Funcion para abrir la aplicacion seleccionada


def lanzar_programa(ruta):
    try:
        # os.startfile le pide a Windows que ejecute la ruta recibida
        os.startfile(ruta)
    except Exception as error:
        print(f"Error al abrir {ruta}: {error}")

# Cargar la lista de programas desde el archivo JSON


def cargar_programas():
    if os.path.exists("programas.json"):
        with open("programas.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    return []


# 1. Ventana principal
ventana = tk.Tk()
ventana.title("Dock Dinamico")
ventana.overrideredirect(True)  # Elimina bordes y barra de titulo tradicional
# Mantiene la ventana siempre visible encima
ventana.attributes("-topmost", True)
ventana.config(bg="#1e1e2e")

# 2. Leer JSON y crear los botones dinamicamente
lista_programas = cargar_programas()

for prog in lista_programas:
    # Creamos un boton por cada elemento en el JSON
    btn = tk.Button(
        ventana,
        text=prog["nombre"],
        command=lambda r=prog["ruta"]: lanzar_programa(r),
        bg="#313244",
        fg="#cdd6f4",
        activebackground="#45475a",
        activeforeground="#ffffff",
        relief="flat",
        padx=12,
        pady=6,
    )
    btn.pack(side="left", padx=4, pady=8)

# 3. Boton para cerrar la aplicacion
btn_cerrar = tk.Button(
    ventana,
    text="x",
    command=ventana.destroy,
    bg="#f38ba8",
    fg="#11111b",
    relief="flat",
    padx=8,
    pady=6,
)
btn_cerrar.pack(side="right", padx=8, pady=8)

# Iniciar el bucle de la aplicacion
ventana.mainloop()
