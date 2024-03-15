from PySide6.QtCore import QObject, Signal
import numexpr as ne


class CalculatorEngine(QObject):
    current_expression_changed = Signal(str)  # Sinal para notificar quando o valor de current_expression mudar
    history_updated = Signal()

    def __init__(self):
        super().__init__()
        self.current_expression = ""

    @property
    def current_expression(self):
        return self._current_expression

    @current_expression.setter
    def current_expression(self, value):
        self._current_expression = value
        self.current_expression_changed.emit(value)  # Emitir o sinal quando o valor de current_expression mudar

    # def on_confirm_clicked(self):
    #     print("Confirm Expression called")
    #     self.previous_expression = self.current_expression
    #     result = eval(self.current_expression)
    #     self.current_expression = result
    #     self.history_updated.emit()

    def on_common_button_click(self, text):
        self.current_expression = self.current_expression + text

    def on_clear_button_click(self):
        self.current_expression = ""

    def set_current_and_previous_expressions(self, result):
        self.previous_expression = self.current_expression
        self.current_expression = str(result)
        self.history_updated.emit()

    def calculate_expression(self):
        try:
            result = ne.evaluate(self.current_expression)
            self.set_current_and_previous_expressions(result)
        except Exception as e:
            self.current_expression = "ERROR"