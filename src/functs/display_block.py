from PyQt6.QtWidgets import QListWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QGroupBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import os
imagepath = "../functs/images/"

class DisplayBlockManager:
    def __init__(self):
        '''
        Constructor:
            Default to no image selected.
        '''
        self.selected_item = None

    def display_block(self):
        '''
        Method:
            Create the display block.

        Returns:
            :display: display block layout.
        '''

        # Initializa the layout.
        display = QVBoxLayout()
        window_layout = QHBoxLayout()
        window_layout.setSpacing(30)  # Space between buttons

        # Split this block in two layouts.
        window_layout = self.image_block(window_layout)
        window_layout, button_select, button_more, button_save = self.list_block(window_layout)
        display.addLayout(window_layout)

        return display, button_select, button_more, button_save

    def image_block(self, display_window):
        '''
        Method:
            Create the image block -- the left side of display block.

        Args:
            :display_window: display block layout.

        Returns:
            :display_window: display block layout with image block added.
        '''

        # Initialize the image block layout.
        self.image_window = QGroupBox("Image Window")
        self.image_window.setStyleSheet("background-color: lightblue;")
        self.image_window.setFixedSize(400, 300)
        self.image_window_layout = QVBoxLayout()

        # Default text for no image.
        self.image_label = QLabel("No Image Selected.")
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setStyleSheet("font-size: 16px; font-style: italic;")

        # Add the elements to the display window layout.
        self.image_window_layout.addWidget(self.image_label)
        self.image_window.setLayout(self.image_window_layout)
        display_window.addWidget(self.image_window)

        return display_window

    def list_block(self, display_window):
        '''
        Method:
            Create the list block -- the left side of display block.
            List of images to choose from.
            Buttons to select image, display more information, and save image.

        Args:
            :display_window: display block layout.

        Returns:
            :display_window: display block layout with list block and buttons added.
        '''

        # Initialize the list block layout.
        self.list_layout = QVBoxLayout()

        list_widget = self.dummy_list()

        # Add the buttons.
        buttons = QHBoxLayout()
        button_select = QPushButton("Select")
        button_more = QPushButton("More")
        button_save = QPushButton("Save")
        button_select.clicked.connect(self.display_selected_item)
        buttons.addWidget(button_select)
        buttons.addWidget(button_more)
        buttons.addWidget(button_save)

        self.list_layout.addWidget(list_widget)
        self.list_layout.addLayout(buttons)

        display_window.addLayout(self.list_layout)

        return display_window, button_select, button_more, button_save
    
    def track_selection(self, item):
        self.selected_item = item

    def display_selected_item(self):
        if self.selected_item:
            image_name = self.selected_item.text()
            pixmap = QPixmap(imagepath+image_name)
            if not pixmap.isNull():
                self.image_label.setPixmap(pixmap.scaled(
                    self.image_label.width(),
                    self.image_label.height(),
                    Qt.AspectRatioMode.KeepAspectRatio
                ))
            else:
                self.image_label.setText("Image not found.")
        else:
            self.image_label.setText("No item selected. Please select an item first.")

    def dummy_list(self):

        # List widget for the scrollable list.
        list_widget = QListWidget()

        list_widget.itemClicked.connect(self.track_selection)
        for image in os.listdir(imagepath):
            list_widget.addItem(image)

        # Add fixed number of items
        for i in range(20):  # Adjust the number as needed
            list_widget.addItem(f"Image {i + 1}")

        return list_widget