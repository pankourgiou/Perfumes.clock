import tkinter as tk
import time
from datetime import datetime

# Mapping each hour to a perfume brand or scent
perfume_clock = {
    0: "Yves Saint Laurent - Libre",
    1: "Dior - J'adore",
    2: "Gucci - Bloom",
    3: "Chanel - No. 5",
    4: "Jo Malone - Peony & Blush Suede",
    5: "Tom Ford - Black Orchid",
    6: "Maison Francis Kurkdjian - Baccarat Rouge 540",
    7: "Byredo - Gypsy Water",
    8: "Le Labo - Santal 33",
    9: "Versace - Bright Crystal",
    10: "Lancôme - La Vie Est Belle",
    11: "Chloé - Eau de Parfum",
    12: "Dolce & Gabbana - Light Blue",
    13: "Calvin Klein - Euphoria",
    14: "Marc Jacobs - Daisy",
    15: "Mugler - Alien",
    16: "Hermès - Twilly",
    17: "Prada - Candy",
    18: "Armani - My Way",
    19: "Azzaro- Most wanted",
    20: "Burberry - Her",
    21: "Narciso Rodriguez - For Her",
    22: "Victoria's Secret - Bombshell",
    23: "Kenzo - Flower"
}

# Colors and aesthetic settings
bg_color = "#fef6f9"
text_color = "#6b2f3e"
font_main = ("Georgia", 36, "bold")
font_small = ("Georgia", 18)

# Create the GUI
root = tk.Tk()
root.title("Perfume Clock")
root.geometry("500x300")
root.configure(bg=bg_color)

# Create time and perfume labels
time_label = tk.Label(root, font=font_main, bg=bg_color, fg=text_color)
time_label.pack(pady=30)

perfume_label = tk.Label(root, font=font_small, bg=bg_color, fg=text_color, wraplength=400)
perfume_label.pack()

# Function to update time and perfume
def update_clock():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    hour = now.hour
    perfume = perfume_clock[hour]

    time_label.config(text=current_time)
    perfume_label.config(text=f"🌸 Current scent: {perfume}")
    root.after(1000, update_clock)

update_clock()
root.mainloop()
