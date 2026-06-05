import os
import re
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

BASE_URL = "https://curly-guacamole-olive.vercel.app/crtlemplus/1/"
IMAGE_EXTENSIONS = (".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp")


def natural_sort_key(filename):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(r"(\d+)", filename)]


class ImageLinkViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Link Viewer")
        self.root.geometry("800x700")
        self.root.configure(bg="#1e1e1e")

        self.folder = os.path.dirname(os.path.abspath(__file__))

        self.images = sorted(
            [f for f in os.listdir(self.folder) if f.lower().endswith(IMAGE_EXTENSIONS)],
            key=natural_sort_key
        )

        self.index = 0
        self.current_photo = None

        self.image_label = tk.Label(root, bg="#1e1e1e")
        self.image_label.pack(pady=20)

        self.filename_label = tk.Label(
            root,
            text="",
            bg="#1e1e1e",
            fg="white",
            font=("Segoe UI", 12)
        )
        self.filename_label.pack()

        self.link_entry = tk.Entry(
            root,
            width=80,
            bg="#2b2b2b",
            fg="white",
            insertbackground="white",
            font=("Segoe UI", 11)
        )
        self.link_entry.pack(pady=10)

        button_frame = tk.Frame(root, bg="#1e1e1e")
        button_frame.pack(pady=10)

        self.prev_button = tk.Button(
            button_frame,
            text="← Gauche",
            command=self.previous_image,
            width=15
        )
        self.prev_button.grid(row=0, column=0, padx=10)

        self.copy_button = tk.Button(
            button_frame,
            text="Copier le lien",
            command=self.copy_link,
            width=15
        )
        self.copy_button.grid(row=0, column=1, padx=10)

        self.next_button = tk.Button(
            button_frame,
            text="Droite →",
            command=self.next_image,
            width=15
        )
        self.next_button.grid(row=0, column=2, padx=10)

        if not self.images:
            messagebox.showerror("Erreur", "Aucune image trouvée dans le dossier.")
        else:
            self.show_image()

    def show_image(self):
        filename = self.images[self.index]
        path = os.path.join(self.folder, filename)

        image = Image.open(path)
        image.thumbnail((700, 500))

        self.current_photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=self.current_photo)

        link = BASE_URL + filename

        self.filename_label.config(
            text=f"{self.index + 1} / {len(self.images)} — {filename}"
        )

        self.link_entry.delete(0, tk.END)
        self.link_entry.insert(0, link)

    def copy_link(self):
        link = self.link_entry.get()
        self.root.clipboard_clear()
        self.root.clipboard_append(link)
        self.root.update()

    def previous_image(self):
        if self.images:
            self.index = (self.index - 1) % len(self.images)
            self.show_image()

    def next_image(self):
        if self.images:
            self.index = (self.index + 1) % len(self.images)
            self.show_image()


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageLinkViewer(root)
    root.mainloop()