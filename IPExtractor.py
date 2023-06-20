import tkinter as tk
from tkinter import messagebox
from urllib.parse import urlparse
from socket import gethostbyname

def extract_ip():
    name = name_entry.get()
    url = url_entry.get()

    # Agregar esquema si no está presente
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url

    try:
        parsed_url = urlparse(url)
        host = parsed_url.netloc
        port = parsed_url.port

        # Verificar si el puerto está definido, si no, usar el puerto por defecto
        if not port:
            port = 80 if parsed_url.scheme == "http" else 443

        ip = gethostbyname(host)
        result = f"{name}, {ip}, {port}, "
        result_text.config(state=tk.NORMAL)  # Habilitar edición del texto
        result_text.insert(tk.END, result + "\n")
        result_text.config(state=tk.DISABLED)  # Deshabilitar edición del texto
    except Exception as e:
        messagebox.showerror("Error", "URL inválida")

# Crear la ventana principal
root = tk.Tk()
root.title("IP Extractor")

# Crear los widgets
name_label = tk.Label(root, text="Nombre:")
name_entry = tk.Entry(root)
url_label = tk.Label(root, text="URL:")
url_entry = tk.Entry(root)
extract_button = tk.Button(root, text="Extraer", command=extract_ip)
result_text = tk.Text(root, width=30, height=10)
result_text.config(state=tk.DISABLED)

# Posicionar los widgets en la ventana
name_label.pack()
name_entry.pack()
url_label.pack()
url_entry.pack()
extract_button.pack()
result_text.pack()

# Iniciar el bucle de eventos
root.mainloop()
