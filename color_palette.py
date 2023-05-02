import random
from pprint import pprint # pretty print  - no need to install
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QComboBox, QSlider)
from PySide6.QtCore import Slot, Qt 
from PySide6.QtGui import QPixmap, QColor
from PySide6 import QtGui, QtWidgets

NEUTRAL_COLORS = [(255, 255, 255), (128, 128, 128), (245, 245, 220)]
ACCENT_COLORS = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), 
                 (0, 255, 255), (0, 0, 255), (128, 0, 128), (255, 0, 255)]

class Colors(QWidget):
    def __init__(self):
        super().__init__()

        #Basic window structure
        self.first_label = QLabel('<h1>Color Palette</h1>') 
        self.rgb_label = QLabel("RGB: (0) to (255)")
        self.hex_label = QLabel("Hex:")
        self.btn = QPushButton('SHOW COLORS')
        self.btn.setFixedWidth(200)
        

        #set background color to lilac
        self.set_background('#c199e0')

        #create color sliders:
        #R:
        self.red_slider = QSlider(Qt.Horizontal)  # create a horizontal slider
        self.red_slider.setMinimum(0)             # set the minimum value to 0
        self.red_slider.setMaximum(255)           # set the maximum value to 255
        self.red_slider.setTickPosition(QSlider.TicksBelow)
        self.red_slider.setTickInterval(10)        # set the tick interval to 1
        self.red_slider.setValue(128)  
        #G:
        self.green_slider = QSlider(Qt.Horizontal)  # create a horizontal slider
        self.green_slider.setMinimum(0)             # set the minimum value to 0
        self.green_slider.setMaximum(255)           # set the maximum value to 255
        self.green_slider.setTickPosition(QSlider.TicksBelow)
        self.green_slider.setTickInterval(10)        # set the tick interval to 1
        self.green_slider.setValue(128)  
        #B:
        self.blue_slider = QSlider(Qt.Horizontal)  # create a horizontal slider
        self.blue_slider.setMinimum(0)             # set the minimum value to 0
        self.blue_slider.setMaximum(255)           # set the maximum value to 255
        self.blue_slider.setTickPosition(QSlider.TicksBelow)
        self.blue_slider.setTickInterval(10)        # set the tick interval to 1
        self.blue_slider.setValue(128)

        # Color Picker label
        vbox = QVBoxLayout() # Vertical Layout
        vbox.addWidget(self.first_label)

        # Create layouts for color boxes
        self.boxes = QHBoxLayout()

        #RGB sliders
        rgb_container = QWidget()
        rgb_container_layout = QVBoxLayout()
        rgb_container_layout.addWidget(self.red_slider)
        rgb_container_layout.addWidget(self.green_slider)
        rgb_container_layout.addWidget(self.blue_slider)
        rgb_container.setLayout(rgb_container_layout)

        #RGB label & sliders
        hbox = QHBoxLayout()  # Horizontal
        hbox.addWidget(self.rgb_label)
        hbox.addWidget(rgb_container)
        
        #overall layout
        vbox.addLayout(hbox)
        vbox.addLayout(self.boxes)
        vbox.addWidget(self.btn)

        self.resize(600, 600)
        self.setLayout(vbox)
        self.red_slider.valueChanged.connect(self.update_color) #when slider is changed
        self.green_slider.valueChanged.connect(self.update_color) #when slider is changed
        self.blue_slider.valueChanged.connect(self.update_color) #when slider is changed
        self.btn.clicked.connect(self.generate_color_palette)

        # # Add color boxes to layout
        # for color in self.color_palette:
        #     color_box = QLabel(self)
        #     color_box.setFixedSize(100, 100)
            
        #     color_box.setStyleSheet(f"background-color: {color.name()}")
        #     self.boxes.addWidget(color_box)


    @Slot()
    def set_background(self, color):
        p = self.palette()
        p.setColor(self.backgroundRole(), color)
        self.setPalette(p)

    @Slot()
    def update_color(self):
        r = self.red_slider.value()
        g = self.green_slider.value()
        b = self.blue_slider.value()
        color = QColor(r, g, b)
        self.set_background(color)

    def generate_color_palette(self):
        r = self.red_slider.value()
        g = self.green_slider.value()
        b = self.blue_slider.value()
       
        color1 = QColor(r+50, g-20, b-10)
        color2 = QColor(r-20, g+5, b+20)
        color3 = QColor(r+50, g-30, b+30)
        color4 = QColor(r+40, g-2, b+30)

        color4 = color4.getRgb()[:3]
        color1 = color1.getRgb()[:3]
        color2 = color2.getRgb()[:3]
        color3 = color3.getRgb()[:3]


        # Create palette with the base color, one neutral color, and one accent color
        palette_list = [color4, color1, color2, color3]
        palette_list[1] = tuple(255 - i for i in color4)

         # Add color boxes to layout
        for color in palette_list:
            color_box = QtWidgets.QFrame(self)
            color_box.setFixedSize(100, 100)
            color_box.setStyleSheet(f"background-color: rgb{color};")
            self.boxes.addWidget(color_box)
    
# source cst205env/bin/activate

app = QApplication([])
win = Colors()
win.show()
sys.exit(app.exec())