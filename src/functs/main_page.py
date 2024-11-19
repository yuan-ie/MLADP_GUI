import sys
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QGroupBox, QStackedWidget
from PyQt6.QtCore import Qt

import layouts
from display_block import DisplayBlockManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("PyQt6 GUI with Styling")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #f0d1e1;")

        # Central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Set a margin around the window
        central_widget.setContentsMargins(20, 20, 20, 20)

        # Main layout
        main_layout = QVBoxLayout()

        # block one -- title block
        block_one = layouts.title_block()
        main_layout.addWidget(block_one, 0)  # Stretch factor = 0, no extra space is given

        # block two -- menu bar
        block_two, about_button, data_button = layouts.menu_block()
        main_layout.addLayout(block_two)


        # block three -- stacked widget
        self.stacked_widget = QStackedWidget()

        # Create widgets for each view
        self.about_widget = self.create_about_widget()
        self.data_widget = self.create_data_widget()

        # Add widgets to the stacked widget
        self.stacked_widget.addWidget(self.about_widget)
        self.stacked_widget.addWidget(self.data_widget)

        # block three -- display: images (left), scrollbar list + buttons (right)
        main_layout.addWidget(self.stacked_widget)
        

        main_layout.addStretch(1)

        # Set the central widget layout
        central_widget.setLayout(main_layout)

        # Connect buttons to corresponding slots
        about_button.clicked.connect(self.show_about)  # About Me button
        data_button.clicked.connect(self.show_data)   # All Data button
        
    def create_data_widget(self):
        data_widget = QWidget()
        data_layout = QVBoxLayout()

        self.display_block_manager = DisplayBlockManager()
        display_block, button_select, button_more, button_save = self.display_block_manager.display_block()
        data_layout.addLayout(display_block)
        data_widget.setLayout(data_layout)

        button_select.clicked.connect(self.display_selected_item)

        return data_widget
    
    def create_about_widget(self):
        about_widget = QWidget()
        about_layout = QVBoxLayout()
        about_label = QLabel("This will be about me...")
        about_layout.addWidget(about_label)
        about_widget.setLayout(about_layout)

        return about_widget
    
    def show_about(self):
        self.stacked_widget.setCurrentWidget(self.about_widget)

    def show_data(self):
        self.stacked_widget.setCurrentWidget(self.data_widget)

    def display_selected_item(self):
        self.display_block_manager.display_selected_item()