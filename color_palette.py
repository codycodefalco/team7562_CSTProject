import sys, random
from pprint import pprint
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
        self.btn.setFixedWidth(300)
        

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
        boxes = QHBoxLayout()
        
        box1Widget = QWidget()
        box1v = QVBoxLayout(box1Widget)
        self.box1 = QtWidgets.QFrame(self)
        self.box1.setFixedSize(100, 100)
        self.box1Label = QLabel()
        box1v.addWidget(self.box1)
        box1v.addWidget(self.box1Label)

        box2Widget = QWidget()
        box2v = QVBoxLayout(box2Widget)
        self.box2 = QtWidgets.QFrame(box2Widget)
        self.box2.setFixedSize(100, 100)
        self.box2Label = QLabel()
        box2v.addWidget(self.box2)
        box2v.addWidget(self.box2Label)

        box3Widget = QWidget()
        box3v = QVBoxLayout(box3Widget)
        self.box3 = QtWidgets.QFrame(box3Widget)
        self.box3.setFixedSize(100, 100)
        self.box3Label = QLabel()
        box3v.addWidget(self.box3)
        box3v.addWidget(self.box3Label)

        box4Widget = QWidget()
        box4v = QVBoxLayout(box4Widget)
        self.box4 = QtWidgets.QFrame(box4Widget)
        self.box4.setFixedSize(100, 100)
        self.box4Label = QLabel()
        box4v.addWidget(self.box4)
        box4v.addWidget(self.box4Label)

        boxes.addWidget(box1Widget)
        boxes.addWidget(box2Widget)
        boxes.addWidget(box3Widget)
        boxes.addWidget(box4Widget)  

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
        
        #left side vertical layout
        vbox.addLayout(hbox)
        vbox.addLayout(boxes)
        vbox.addWidget(self.btn)

        #Right side Clothing layout:
        clothingbox = QVBoxLayout()
        self.shirt_box = QLabel()
        self.shirt_img = QPixmap('image/shirt.webp')
        self.shirt_box.setPixmap(self.shirt_img)
        clothingbox.addWidget(self.shirt_box) 

        #overall layout
        bigHbox = QHBoxLayout()
        bigHbox.addLayout(vbox)
        bigHbox.addLayout(clothingbox)
        

        self.resize(600, 600)
        self.setLayout(bigHbox)
        self.red_slider.valueChanged.connect(self.update_color) #when slider is changed
        self.green_slider.valueChanged.connect(self.update_color) #when slider is changed
        self.blue_slider.valueChanged.connect(self.update_color) #when slider is changed
        self.btn.clicked.connect(self.generate_color_palette)


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
       
        color1 = QColor(r+10, g-20, b-10)
        color2 = QColor(r-20, g+25, b+10)
        color3 = QColor(r+20, g-10, b+50)
        color4 = QColor(r-10, g-100, b-5)

        color4 = color4.getRgb()[:3]
        color1 = color1.getRgb()[:3]
        color2 = color2.getRgb()[:3]
        color3 = color3.getRgb()[:3]


        # Create palette with the base color, one neutral color, and one accent color
        palette_list = [color4, color1, color2, color3]
        palette_list[1] = tuple(255 - i for i in color4)

         # Add color boxes to layout
        i = 1;
        for color in palette_list:
            if(i == 1):
                self.box1.setStyleSheet(f"background-color: rgb{color};")
                color_str = f"RGB: ({color[0]}, {color[1]}, {color[2]})"
                color_hex = "#{:02x}{:02x}{:02x}".format(*color)
                self.box1Label.setText(color_str + '\n' + 'Hex: ' + color_hex)
            if(i == 2):
                self.box2.setStyleSheet(f"background-color: rgb{color};")
                color_str = f"RGB: ({color[0]}, {color[1]}, {color[2]})"
                color_hex = "#{:02x}{:02x}{:02x}".format(*color)
                self.box2Label.setText(color_str + '\n' + 'Hex: ' + color_hex)
            if(i == 3):
                self.box3.setStyleSheet(f"background-color: rgb{color};")
                color_str = f"RGB: ({color[0]}, {color[1]}, {color[2]})"
                color_hex = "#{:02x}{:02x}{:02x}".format(*color)
                self.box3Label.setText(color_str + '\n'  + 'Hex: ' + color_hex)
            if(i == 4):
                self.box4.setStyleSheet(f"background-color: rgb{color};")
                color_str = f"RGB: ({color[0]}, {color[1]}, {color[2]})"
                color_hex = "#{:02x}{:02x}{:02x}".format(*color)
                self.box4Label.setText(color_str + '\n' + 'Hex: ' + color_hex)
            i = i + 1;
    
# source cst205env/bin/activate

app = QApplication([])
win = Colors()
win.show()
sys.exit(app.exec())