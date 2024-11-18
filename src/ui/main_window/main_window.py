''' app/ui/main_window.py '''
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QTextEdit
from utils.config import AppConfig
from .modules.menu_bar import MenuBar


class MainWindow(QMainWindow):
    """
    MainWindow

    Args:
        QMainWindow (QMainWindow): Inheritance
    """

    def __init__(self) -> None:
        """
        Initialize the Main-Window.
        """
        super().__init__()
        # Window-Settings
        self.setWindowTitle(AppConfig.APP_NAME)
        self.setGeometry(100, 100, 800, 600)
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QHBoxLayout(central_widget)
        central_widget.setLayout(layout)

        # Add Widgets to Window
        self.setMenuBar(MenuBar(self))

        layout.addWidget(self.treeview)
        layout.addWidget(self.editbox, stretch=1)
        layout.addWidget(self.editbox)
