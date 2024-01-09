import tkinter as tk
from tkinter import filedialog
import qrcode
from tkinter import ttk

def generate_qr_code():
    url = url_entry.get()  # Kullanıcının girdiği URL'yi al
    if url:
        qr = qrcode.make(url)  # QR kodunu oluştur
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            qr.save(save_path)  # PNG olarak kaydet
            result_label.config(text="QR kodu başarıyla kaydedildi.", fg="green")
            
            # Metin kutusunu ve etiketleri temizle
            url_entry.delete(0, tk.END)
            result_label.config(text="", fg="black")
        else:
            result_label.config(text="Kaydetme iptal edildi.", fg="red")
    else:
        result_label.config(text="Lütfen bir URL girin.", fg="red")

def popup(event):
    menu.tk_popup(event.x_root, event.y_root)

root = tk.Tk()
root.title("QR Kodu Oluşturucu")

url_entry = ttk.Entry(root, width=40)
url_entry.pack()

menu = tk.Menu(root, tearoff=0)
menu.add_command(label="Kopyala", command=lambda: root.clipboard_append(url_entry.get()))
menu.add_command(label="Kes", command=lambda: url_entry.delete('sel.first', 'sel.last'))
menu.add_command(label="Yapıştır", command=lambda: url_entry.insert('insert', root.clipboard_get()))

url_entry.bind("<Button-3>", popup)

generate_button = tk.Button(root, text="QR Kodu Oluştur", command=generate_qr_code)
generate_button.pack()

result_label = tk.Label(root, text="", fg="black")
result_label.pack()

root.mainloop()
