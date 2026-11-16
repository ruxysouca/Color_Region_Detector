from PIL import Image

class ImageGraph:

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

    def build_graph(self):
        if not self.pixel_matrix:
            self.load_image_to_matrix()

        self.adj = {}
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for y in range(self.height):
            for x in range(self.width):
                node = (y, x)
                self.adj[node] = []
                current_color = self.pixel_matrix[y][x]

                for dy, dx in directions:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < self.height and 0 <= nx < self.width:
                        if self.pixel_matrix[ny][nx] == current_color:
                            self.adj[node].append((ny, nx))

        return self.adj