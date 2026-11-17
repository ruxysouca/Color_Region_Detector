# Color Region Detector

A python desktop application that determines the number of independent color regions in an image by modeling the pixel matrix as an undirected graph and applying an **iterative Depth-First Search Connected Components** algorithm.

## Features

- **Pixel Matrix Extraction:** Converts input images (`PNG`, `JPG`, `JPEG`, `BMP`) into a 2D RGB pixel matrix using `Pillow`.
- **Graph Construction:** Models each pixel `(row, col)` as a graph vertex and connects adjacent pixels (4-connectivity: up, down, left, right) sharing identical RGB values.
- **Iterative DFS Connected Components:** Identifies all independent color regions using an explicit stack-based DFS traversal (strictly non-recursive to prevent stack overflow on high-resolution images).
- **Interactive GUI:** Built with `tkinter`, allowing users to load images, preview them on a centered canvas, and compute the exact region count.

## Project Structure

```text
Color_Region_Detector/
├── data/               # Sample test images (e.g., img1.png, img3.png)
├── image_graph.py      # Image-to-matrix conversion, graph builder, and iterative DFS algorithm
├── region_app.py       # Tkinter graphical user interface
├── main.py             # Application entry point
├── LICENSE             # MIT License
└── README.md           # Project documentation
