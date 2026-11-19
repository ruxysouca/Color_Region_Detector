import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from image_graph import ImageGraph

class RegionApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Color Region Detector")
        self.root.geometry("660x600")

        self.image_path = None
        self.tk_image = None
        self.graph = None

        control_frame = tk.Frame(self.root, pady = 10)
        control_frame.grid(row = 0, column = 0)

        self.load_button = tk.Button(control_frame, text = "Load image", width = 15, font = ("Courier", 11, "bold"), command = self.load_image)
        self.load_button.grid(row = 0, column = 1, padx = 10)

        self.detect_button = tk.Button(control_frame, text = "Detect region", width = 15, state = tk.DISABLED, font = ("Courier", 11, "bold"), command = self.detect_regions)
        self.detect_button.grid(row = 0, column = 2, padx = 5)

        self.result_label = tk.Label(control_frame, text = "Raw regions: -\nPerceived: -", font = ("Courier", 11, "bold"), justify = tk.LEFT)
        self.result_label.grid(row = 0, column = 3, padx = 20)

        self.canvas = tk.Canvas(self.root, bg="white", width = 540, height = 500)
        self.canvas.grid(row = 1, column = 0, padx = 60, pady = 10)

    def load_image(self):
        path = filedialog.askopenfilename(
            initialdir = "data",
            title = "Select an image",
            filetypes = [("Image files", "*.png *.jpg *.jpeg *.bmp")],
        )
        if not path:
            return

        self.image_path = path
        self.graph = ImageGraph(path)

        with Image.open(path) as img:
            display_img = img.resize((460, 460))
            self.tk_image = ImageTk.PhotoImage(display_img)

        self.canvas.delete("all")
        self.canvas.create_image(270, 250, image = self.tk_image, anchor = tk.CENTER)

        self.detect_button.config(state=tk.NORMAL)
        self.result_label.config(text = "Raw regions: -\nPerceived: -", font = ("Courier", 11, "bold"))

    def detect_regions(self):
        if not self.graph:
            return

        self.result_label.config(text = "Processing...")
        self.root.update_idletasks()

        self.graph.load_image_to_matrix()
        self.graph.build_graph()
        components = self.graph.find_connected_components()

        perceived = self.graph.find_perceived_regions()
        total_regions = len(components)
        perceived_regions = len(perceived)

        self.result_label.config(text =  f"Raw regions: {total_regions}\nPerceived: {perceived_regions}")