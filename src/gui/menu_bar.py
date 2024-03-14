from PySide6.QtWidgets import QMainWindow


class MenuBar():
    def __init__(self, QMainWindow):
        super().__init__()

        main_bar = QMainWindow.menuBar()

        view_menu_option = main_bar.addMenu("View")
        edit_menu_option = main_bar.addMenu("Edit")
        help_menu_option = main_bar.addMenu("Help")



