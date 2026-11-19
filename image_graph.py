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

    def find_connected_components(self):
        if not self.adj:
            self.build_graph()

        visited = set()
        components = []

        for start_node in self.adj:
            if start_node not in visited:
                component = []
                stack = [start_node]
                visited.add(start_node)

                while stack:
                    curr = stack.pop()
                    component.append(curr)

                    for neighbor in self.adj[curr]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            stack.append(neighbor)

                components.append(component)
            
        return components

    def color_distance(self, c1, c2):
        return ((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2 + (c1[2]- c2[2]) ** 2) ** 0.5

    def clean_boundary_pixels(self, edge_threshold = 60):
        if not self.pixel_matrix:
            self.load_image_to_matrix()

        cleaned = [row[:] for row in self.pixel_matrix]       

        for x in range(1, self.height - 1):
            for y in range (1, self.width - 1):
                curr = self.pixel_matrix[x][y]
                left, right = self.pixel_matrix[x][y - 1],  self.pixel_matrix[x][y + 1] 
                up, down = self.pixel_matrix[x - 1][y], self.pixel_matrix[x + 1][y]

                is_edge = (
                    self.color_distance(left, right) > edge_threshold
                    or self.color_distance(up, down) > edge_threshold
                )   
                if is_edge:
                    neighbors = [left, right, up, down]
                    cleaned[x][y] = min(neighbors, key = lambda n: self.color_distance(curr, n))

        return cleaned

    def find_perceived_regions(self, color_tolerance = 45):
        matrix = self.clean_boundary_pixels()
        visited = set()
        regions = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for x in range(self.height):
            for y in range(self.width):
                start_node = (x, y)
                if start_node not in visited:
                    seed_color = matrix[x][y]
                    region = []
                    stack = [start_node]
                    visited.add(start_node)

                    while stack:
                        cx, cy = stack.pop()
                        region.append((cx, cy))

                        for dx, dy in directions:
                            nx, ny = cx + dx, cy + dy
                            if 0 <= nx < self.height and 0 <= ny < self.width:
                                if (nx, ny) not in visited:
                                    neighbor_color = matrix[nx][ny]
                                    if self.color_distance(neighbor_color, seed_color) <= color_tolerance:
                                        visited.add((nx, ny))
                                        stack.append((nx, ny))

                    regions.append(region)

        return regions