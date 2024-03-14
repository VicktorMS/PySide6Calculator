from PySide6.QtCore import QObject, Signal


class CalculatorEngine(QObject):
    current_expression_changed = Signal(str)  # Sinal para notificar quando o valor de current_expression mudar

    def __init__(self):
        super().__init__()
        self.current_expression = ""
        self.previous_expression = ""

    @property
    def current_expression(self):
        return self._current_expression

    @current_expression.setter
    def current_expression(self, value):
        self._current_expression = value
        self.current_expression_changed.emit(value)  # Emitir o sinal quando o valor de current_expression mudar

    def on_confirm_clicked(self, calc_data):
        result = eval(self.current_expression)
        self.current_expression = result
        print(result)

    def on_common_button_click(self, text):
        self.current_expression = self.current_expression + text
        print(self.current_expression)

    def on_clear_button_click(self):
        self.current_expression = ""

    def on_equal_button_click(self):
        result = eval(self.current_expression)
        self.previous_expression = self.current_expression
        self.current_expression = str(result)
