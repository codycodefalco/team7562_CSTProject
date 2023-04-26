import random
from PySide6 import QtGui, QtWidgets

NEUTRAL_COLORS = [(255, 255, 255), (128, 128, 128), (245, 245, 220)]
ACCENT_COLORS = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), 
                 (0, 255, 255), (0, 0, 255), (128, 0, 128), (255, 0, 255)]

class ColorPalette(QtWidgets.QWidget):
    def __init__(self, colors):
        super().__init__()

        # Set window title and size
        self.setWindowTitle('Color Palette')
        self.setMinimumSize(500, 100)

        # Create layout for color boxes
        layout = QtWidgets.QHBoxLayout()

        # Add color boxes to layout
        for color in colors:
            color_box = QtWidgets.QFrame(self)
            color_box.setFixedSize(100, 100)
            color_box.setStyleSheet(f"background-color: rgb{color};")
            layout.addWidget(color_box)

        # Set layout for window
        self.setLayout(layout)

def generate_color_palette(base_color):
    # Convert base color from hex to RGB format
    rgb_base = base_color.getRgb()[:3]

    # Choose two random neutral colors from NEUTRAL_COLORS list
    neutral1, neutral2 = random.sample(NEUTRAL_COLORS, 2)

    # Choose two random accent colors from ACCENT_COLORS list
    accent1, accent2 = random.sample(ACCENT_COLORS, 2)

    # Create palette with the base color, one neutral color, and one accent color
    palette = [rgb_base, neutral1, accent1, neutral2]

    # Replace the first neutral color with the complement of the base color
    palette[1] = tuple(255 - i for i in rgb_base)

    return palette

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    base_color = QtWidgets.QColorDialog.getColor()

    if base_color.isValid():
        palette = generate_color_palette(base_color)

        palette_window = ColorPalette(palette)
        palette_window.show()

        app.exec_()
