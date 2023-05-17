import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap
from PIL import Image
from PIL.ImageQt import ImageQt

# Create a window
app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Bitmoji Avatar")

# Load the Bitmoji avatar image
avatar = Image.open('bitmoji.jpg')

# Define the clothing options
shirt = Image.open('shirt.jpeg')
pants = Image.open('pants.jpeg')

# Create a combo box with the clothing options
options = ['Shirt', 'Pants']
combo_box = QComboBox()
combo_box.addItems(options)

# Create a horizontal layout and add the avatar label and combo box
hlayout = QHBoxLayout()
avatar_pixmap = QPixmap.fromImage(ImageQt(avatar))
avatar_label = QLabel()
avatar_label.setPixmap(avatar_pixmap)
hlayout.addWidget(avatar_label)
hlayout.addWidget(combo_box)

# Function to update the avatar image when the user selects a clothing item
def update_avatar():
    selected_item = combo_box.currentText()
    if selected_item == 'Shirt':
        avatar.paste(shirt, (0, 0), shirt)
    elif selected_item == 'Pants':
        avatar.paste(pants, (0, 0), pants)
    # Display the updated avatar image in the window
    avatar_pixmap = QPixmap.fromImage(ImageQt(avatar))
    avatar_label.setPixmap(avatar_pixmap)


update_button = QPushButton("Update Avatar")
update_button.clicked.connect(update_avatar)


tool_bar = QToolBar()
tool_bar.addWidget(update_button)
window.addToolBar(tool_bar)

central_widget = QWidget()
central_widget.setLayout(hlayout)
window.setCentralWidget(central_widget)


window.show()
sys.exit(app.exec())
