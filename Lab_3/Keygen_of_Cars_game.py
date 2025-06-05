import tkinter as tk
import random
from PIL import Image, ImageTk


class KeygenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Key Generator")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        self.bg_image = Image.open("game_bg.jpg")
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = tk.Label(root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(
            self.root,
            text="THE CRAZY CARS",
            font=("Arial", 24, "bold"),
            fg="#4A90E2",
            bg="#1A1A1A"
        )
        title.pack(pady=30)

        input_frame = tk.Frame(self.root, bg="#1A1A1A", padx=10, pady=10)
        input_frame.pack(pady=10)

        tk.Label(
            input_frame,
            text="Enter your name:",
            font=("Arial", 14),
            fg="white",
            bg="#1A1A1A"
        ).pack(side=tk.LEFT)

        self.name_entry = tk.Entry(
            input_frame,
            font=("Arial", 14),
            width=25,
            bd=2,
            relief=tk.GROOVE
        )
        self.name_entry.pack(side=tk.LEFT, padx=10)
        self.name_entry.focus()

        generate_btn = tk.Button(
            self.root,
            text="GENERATE KEY",
            font=("Arial", 16, "bold"),
            bg="#4A90E2",
            fg="white",
            activebackground="#3A7BC8",
            command=self.generate_key,
            padx=20,
            pady=10,
            bd=0,
            relief=tk.GROOVE
        )
        generate_btn.pack(pady=20)

        self.key_var = tk.StringVar()
        key_entry = tk.Entry(
            self.root,
            textvariable=self.key_var,
            font=("Consolas", 18, "bold"),
            width=20,
            justify=tk.CENTER,
            bd=3,
            relief=tk.SUNKEN,
            state='readonly',
            readonlybackground="#2C2C2C",
            fg="#50C878"
        )
        key_entry.pack(pady=10)

        self.status_var = tk.StringVar()
        status_label = tk.Label(
            self.root,
            textvariable=self.status_var,
            font=("Arial", 12),
            fg="white",
            bg="#1A1A1A"
        )
        status_label.pack(pady=5)

        weight_info = tk.Label(
            self.root,
            text="Key validation: sum of weights per block must be between 100-110",
            font=("Arial", 10),
            fg="#AAAAAA",
            bg="#1A1A1A"
        )
        weight_info.pack(pady=15)

        self.root.bind('<Return>', lambda event: self.generate_key())

    def calculate_weight(self, char):

        if char in '0123456789':
            return int(char)
        return ord(char) - 55

    def generate_block(self):

        while True:
            block = ''.join(random.choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=4))
            total = sum(self.calculate_weight(c) for c in block)
            if 100 <= total <= 110:
                return block, total

    def generate_key(self):

        name = self.name_entry.get().strip()
        if not name:
            self.status_var.set("Please enter your name first!")
            return

        key_blocks = []
        weights = []
        for _ in range(3):
            block, total = self.generate_block()
            key_blocks.append(block)
            weights.append(total)

        key = '-'.join(key_blocks)
        self.key_var.set(key)
        self.status_var.set(f"Valid key! Block weights: {weights}")


if __name__ == "__main__":
    root = tk.Tk()
    app = KeygenApp(root)
    root.mainloop()