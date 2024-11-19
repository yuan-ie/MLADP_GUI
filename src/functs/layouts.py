from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QGroupBox
from PyQt6.QtCore import Qt

def title_block():
    '''
    Block one:
        displays only the title of the window -- center-aligned.
    '''
    pass

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
    button1 = QPushButton("About Me")
    button2 = QPushButton("All Data")
    button3 = QPushButton("Etc.")
    
    # Add buttons to the layout
    button_layout.addWidget(button1)
    button_layout.addWidget(button2)
    button_layout.addWidget(button3)

    # Add to layout
    block_two.addLayout(button_layout)

    return block_two

def display_block():
    block_three = QVBoxLayout()
    window_layout = QHBoxLayout()
    window_layout.setSpacing(30)  # Space between buttons

    window_layout = display_block_left(window_layout)
    window_layout = display_block_right(window_layout)

    block_three.addLayout(window_layout)
    return block_three

def display_block_left(b3_layout):
    '''
    Block three (left):
        shows image of breast tissue.
    '''

    # LEFT LAYOUT: has window
    left_layout = QGroupBox("Left Window")
    left_layout.setStyleSheet("background-color: lightblue;")
    left_window = QVBoxLayout()
    left_layout.setLayout(left_window)

    b3_layout.addWidget(left_layout)

    return b3_layout

    

def display_block_right(b3_layout):
    '''
    Block three (right):
        shows list of images to choose from (top) and buttons (bottom).
    '''
    # RIGHT LAYOUT
    right_layout = QVBoxLayout()

    # window for right layout
    right_window = QGroupBox("Right Window")
    right_window.setStyleSheet("background-color: lightgreen;")
    # Add a layout to the right window for future content
    right_window_layout = QVBoxLayout()
    right_window.setLayout(right_window_layout)

    
    # buttons for right layout
    right_buttons = QHBoxLayout()
    button_select = QPushButton("Select")
    button_more = QPushButton("More")
    button_save = QPushButton("Save")
    right_buttons.addWidget(button_select)
    right_buttons.addWidget(button_more)
    right_buttons.addWidget(button_save)


    right_layout.addWidget(right_window)
    right_layout.addLayout(right_buttons)

    b3_layout.addLayout(right_layout)

    return b3_layout