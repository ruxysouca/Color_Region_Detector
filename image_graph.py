from PIL import Image

class ImageGRaph:

    def __init__(self, image_path):
        self.image_path = image_path
        self.width = 0
        self.height = 0
        self.pixel_matrix = []
        self.adj = {}

    def load_image_to_matrix(self):
        with Image.open(self.image_path) as img:
            rgb_img = img.convert("RGB")
            self.width, self.height = rgb_img.size

            self.pixel_matrix = []
            for y in range(self.height):
                row = []
                for x in range(self.width):
                    row.append(rgb_img.getpixel((x,y)))
                self.pixel_matrix.append(row)

        return self.pixel_matrix