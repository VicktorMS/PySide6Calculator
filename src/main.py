import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from src.gui.main_window import MainWindow

ICON_PATH = "src/icons/calculator_icon.png"
APP_NAME = "Calculadora"


app = QApplication(sys.argv)
app.setApplicationDisplayName(APP_NAME)

app_icon = QIcon(ICON_PATH)


window = MainWindow()
window.setWindowTitle(APP_NAME)
window.setWindowIcon(app_icon)

window.show()
app.exec()
