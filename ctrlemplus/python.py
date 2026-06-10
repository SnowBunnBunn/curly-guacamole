import os
import re
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

BASE_URL = "https://curly-guacamole-olive.vercel.app/ctrlemplus/"
IMAGE_EXTENSIONS = (".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp")


def natural_sort_key(filename):
    return [
        int(text) if text.isdigit() else text.lower()
        for text in re.split(r"(\d+)", filename)
    ]


class ImageLinkViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Link Viewer")
        self.root.geometry("850x740")
        self.root.configure(bg="#1e1e1e")

        self.base_folder = os.path.dirname(os.path.abspath(__file__))
        self.image_folder = None
        self.folder_name = ""
        self.images = []
        self.index = 0
        self.current_photo = None

        folder_frame = tk.Frame(root, bg="#1e1e1e")
        folder_frame.pack(pady=15)

        tk.Label(
            folder_frame,
            text="Nom du dossier :",
            bg="#1e1e1e",
            fg="white",
            font=("Segoe UI", 11)
        ).pack(side="left", padx=5)

        self.folder_entry = tk.Entry(
            folder_frame,
            width=35,
            bg="#2b2b2b",
            fg="white",
            insertbackground="white",
            font=("Segoe UI", 11)
        )
        self.folder_entry.pack(side="left", padx=5)

        self.load_button = tk.Button(
            folder_frame,
            text="Charger",
            command=self.load_folder,
            width=12
        )
        self.load_button.pack(side="left", padx=5)

        self.folder_entry.bind("<Return>", lambda e: self.load_folder())

        self.image_label = tk.Label(root, bg="#1e1e1e")
        self.image_label.pack(pady=20)

        self.filename_label = tk.Label(
            root,
            text="Entre un nom de dossier puis clique sur Charger",
            bg="#1e1e1e",
            fg="white",
            font=("Segoe UI", 12)
        )
        self.filename_label.pack()

        self.link_entry = tk.Entry(
            root,
            width=95,
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

        if os.path.exists("folder.txt"):
            with open("folder.txt", "r", encoding="utf-8") as f:
                saved_folder = f.read().strip()
                self.folder_entry.insert(0, saved_folder)
                if saved_folder:
                    self.load_folder()

    def load_folder(self):
        self.folder_name = self.folder_entry.get().strip().strip("/\\")

        if not self.folder_name:
            messagebox.showerror("Erreur", "Entre un nom de dossier.")
            return

        self.image_folder = os.path.join(self.base_folder, self.folder_name)

        if not os.path.isdir(self.image_folder):
            messagebox.showerror(
                "Erreur",
                f"Le dossier n'existe pas :\n{self.image_folder}"
            )
            return

        self.images = sorted(
            [
                f for f in os.listdir(self.image_folder)
                if f.lower().endswith(IMAGE_EXTENSIONS)
            ],
            key=natural_sort_key
        )

        if not self.images:
            messagebox.showerror(
                "Erreur",
                f"Aucune image trouvée dans le dossier :\n{self.folder_name}"
            )
            return

        with open("folder.txt", "w", encoding="utf-8") as f:
            f.write(self.folder_name)

        self.index = 0
        self.show_image()

    def show_image(self):
        if not self.images or not self.image_folder:
            return

        filename = self.images[self.index]
        path = os.path.join(self.image_folder, filename)

        image = Image.open(path)
        image.thumbnail((700, 500))

        self.current_photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=self.current_photo)

        link = f"{BASE_URL}{self.folder_name}/{filename}"

        self.filename_label.config(
            text=f"{self.index + 1} / {len(self.images)} — {filename}"
        )

        self.link_entry.delete(0, tk.END)
        self.link_entry.insert(0, link)

    def copy_link(self):
        link = self.link_entry.get()

        if not link:
            return

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