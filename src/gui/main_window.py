from PySide6.QtWidgets import QWidget, QMainWindow, QVBoxLayout

from src.core.calculator_engine import CalculatorEngine
from src.gui.expression_history import ExpressionHistory
from src.gui.menu_bar import MenuBar
from src.gui.button_pad import ButtonPad
from src.gui.result_display import ResultDisplay


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.calculator_engine = CalculatorEngine()
        self.setup_ui(self.calculator_engine)

    def setup_ui(self, calc_engine):
        self.create_menu_bar()
        self.create_central_widget(calc_engine)

    def create_menu_bar(self):
        MenuBar(self)

    def create_central_widget(self, calc_engine):
        expression_history = ExpressionHistory(calc_engine)
        result_display = ResultDisplay(calc_engine)
        buttons_pad = ButtonPad(calc_engine)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_vlayout = QVBoxLayout()
        central_widget.setLayout(main_vlayout)

        main_vlayout.addWidget(expression_history)
        main_vlayout.addWidget(result_display)
        main_vlayout.addWidget(buttons_pad)

