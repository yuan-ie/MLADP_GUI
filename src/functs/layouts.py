from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QGroupBox, QListWidget
from PyQt6.QtCore import Qt


def menu_block():
    '''
    Block two:
        contains buttons and search: About, All Data, and Search
    '''
    
    # Create the second block
    block_two = QVBoxLayout()

    # Horizontal Layout for buttons
    button_layout = QHBoxLayout()
    button_layout.setSpacing(20)  # Space between buttons
    
    # Create buttons with rounded corners
    button1 = QPushButton("About")
    button2 = QPushButton("Viewer")
    button3 = QPushButton("Data Types")
    
    # Add buttons to the layout
    button_layout.addWidget(button1)
    button_layout.addWidget(button2)
    button_layout.addWidget(button3)

    # Add to layout
    block_two.addLayout(button_layout)

    return block_two, button1, button2, button3

def title_block():
    '''
    Block one:
        displays only the title of the window -- center-aligned.
    '''
    title_label = QLabel("Biopsy Slide Viewer")
    title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    title_label.setStyleSheet("font-size: 24px;") # font-weight: bold;
    return title_label