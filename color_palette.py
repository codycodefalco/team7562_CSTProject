# CST - Multimedia Design & Programming
# Color Palette Generator
# AUthors: Cody Falconer, Jessica Bejarano, Christian Perez
# May 18, 2023
# Github Link: https://github.com/codycodefalco/team7562_CSTProject
# Trello Link: https://trello.com/invite/b/WR4Iu4I2/ATTI261f0f7330c79146f596512a8442d37c59D40931/team-7562-workspace
# Rgb to Hex formula: https://www.educative.io/answers/how-to-convert-hex-to-rgb-and-rgb-to-hex-in-python
# This app will generate a palette with complimentary colors based on the user's 
# choice in the RGB sliders.
# Generate_color_palette function: By Cody Falconer and Jessica Bejarano, will update color palette boxes with the generated complimentary colors.
# Color_filter: By Jessica Bejarano, will also apply a color scheme filter to the clothing to build an outfit based on the color chosen.


import sys, random
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QComboBox, QSlider)
from PySide6.QtCore import Slot, Qt 
from PySide6.QtGui import QPixmap, QColor
from PySide6 import QtGui, QtWidgets
from PIL import Image, ImageQt

NEUTRAL_COLORS = [
    QColor(128, 128, 128),  # Gray
    QColor(255, 255, 255),  # White
    QColor(0, 0, 0),  # Black
    QColor(245, 245, 220),  # Beige
    QColor(210, 180, 140),  # Tan
]

class Colors(QWidget):
    def __init__(self):
        super().__init__()

        #Basic window structure
        self.first_label = QLabel('<h1>Color Palette</h1>') 
        self.rgb_label = QLabel("RGB:")
        self.hex_label = QLabel("Hex:")
        self.color_label = QLabel()
        self.mid_label = QLabel("0                                                         128                                                        255")
        self.btn = QPushButton('SHOW COLORS')
        self.btn.setFixedWidth(200)

        #set background color to a neutral color
        self.set_background('#afa594')

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
        vbox.setAlignment(self.first_label, Qt.AlignCenter)

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
        rgb_container_layout.addWidget(self.mid_label)
        rgb_container_layout.setAlignment(self.mid_label, Qt.AlignCenter)
        rgb_container_layout.addWidget(self.red_slider)
        rgb_container_layout.addWidget(self.green_slider)
        rgb_container_layout.addWidget(self.blue_slider)
        rgb_container.setLayout(rgb_container_layout)

        #RGB label & sliders
        hbox = QHBoxLayout()  # Horizontal
        hbox.addWidget(self.rgb_label)
        hbox.setAlignment(self.rgb_label, Qt.AlignCenter)
        hbox.addWidget(rgb_container)
        
        #left side vertical layout
        vbox.addLayout(hbox)
        vbox.addWidget(self.color_label)
        vbox.addLayout(boxes)
        vbox.addWidget(self.btn)
        vbox.setAlignment(self.btn, Qt.AlignCenter)

        #Right side Clothing layout:
        clothingbox = QVBoxLayout()
        self.shirt_box = QLabel()
        self.pants_box = QLabel()
        self.shirt_img = QPixmap('image/shirt.webp')
        self.pants_img = QPixmap('image/PANTS.png')
        self.shirt_box.setPixmap(self.shirt_img)
        self.pants_box.setPixmap(self.pants_img)
        clothingbox.addWidget(self.shirt_box) 
        clothingbox.addWidget(self.pants_box)

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

    #Changes background color of app
    @Slot()
    def set_background(self, color):
        p = self.palette()
        p.setColor(self.backgroundRole(), color)
        self.setPalette(p)

    # Gets colors from sliders and makes an RGB
    @Slot()
    def update_color(self):
        r = self.red_slider.value()
        g = self.green_slider.value()
        b = self.blue_slider.value()
        color = QColor(r, g, b)
        self.set_background(color)

    #Updates color palette:
    def generate_color_palette(self):
        r = self.red_slider.value()
        g = self.green_slider.value()
        b = self.blue_slider.value()
       
        color1 = QColor(r, g, b)
        color2 = QColor(random.choice(NEUTRAL_COLORS))
        color3 = QColor(255-r, 255-g, 255-b)
        color4 = QColor(abs(r-100), abs(g-100), abs(b-50))

        color4 = color4.getRgb()[:3]
        color1 = color1.getRgb()[:3]
        color2 = color2.getRgb()[:3]
        color3 = color3.getRgb()[:3]


        # Create palette with the base color, one neutral color, and one accent color
        palette_list = [color4, color1, color2, color3]
        palette_list[1] = tuple(255 - i for i in color4)

        self.color_label.setText('Color chosen: ' + str(color1))
        #Add color boxes to layout
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

        # Apply filter to outfit images:
        # Convert QPixmap to QImage:
        image = self.shirt_img.toImage()
        pants = self.pants_img.toImage()

        # Put a filter on shirt image with the 4 colors:
        for i in range(image.width()):
            for j in range(image.height()):
                pixel= image.pixel(i, j)
                color = QColor(pixel)
                r, g, b, a = color.getRgb()
                new_color = QColor()  # Create a new QColor object
                index = r // 64  # 0 to 3 based on red slider value
                new_color.setRgb(*palette_list[index])  # Apply the desired color from the palette list
                image.setPixel(i, j, new_color.rgb())
        self.shirt_box.setPixmap(QPixmap.fromImage(image))

        # Put a filter on pants image with the 4 colors:
        for i in range(pants.width()):
            for j in range(pants.height()):
                pixel= pants.pixel(i, j)
                color = QColor(pixel)
                r, g, b, a = color.getRgb()
                new_color = QColor()  # Create a new QColor object
                index = b // 64  # 0 to 3 based on blue slider value
                new_color.setRgb(*palette_list[index])  # Apply the desired color from the palette list
                pants.setPixel(i, j, new_color.rgb())
        self.pants_box.setPixmap(QPixmap.fromImage(pants))

    
# source cst205env/bin/activate

app = QApplication([])
win = Colors()
win.resize(1000, 1000)
win.show()
sys.exit(app.exec())