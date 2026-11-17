import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from image_graph import ImageGraph

class RegionApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Color Region Detector")
        self.root.geometry("700x500")

        self.image_path = None
        self.tk_image = None
        self.graph = None

        control_frame = tk.Frame(self.root, pady = 10)
        control_frame.grid(row = 0, column = 0)

        self.load_button = tk.Button(control_frame, text = "Load image", width = 15, font = ("Courier", 11, "bold"))
        self.load_button.grid(row = 0, column = 1, padx = 10)

        self.detect_button = tk.Button(control_frame, text = "Detect region", width = 15, state = tk.DISABLED, font = ("Courier", 11, "bold"))
        self.detect_button.grid(row = 0, column = 2, padx = 5)

        self.result_label = tk.Label(control_frame, text = "Regions found: -", font = ("Courier", 11, "bold"))
        self.result_label.grid(row = 0, column = 3, padx = 20)

        self.canvas = tk.Canvas(self.root, bg="#f0f0f0", width = 750, height = 560)
        self.canvas.grid(row = 1, column = 0, pady = 10)