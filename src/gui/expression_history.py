from PySide6.QtWidgets import QLabel, QHBoxLayout, QWidget


class ExpressionHistory(QWidget):
    def __init__(self, calculator_engine):
        super().__init__()
        self.calculator_engine = calculator_engine
        self.create_history()
        self.calculator_engine.history_updated.connect(self.update_history)

    def create_history(self):
        print("Creating History")
        layout = QHBoxLayout()
        self.expression_label = QLabel()
        layout.addWidget(self.expression_label)
        self.setLayout(layout)

    def update_history(self):
        print("Updating History")
        self.expression_label.setText(f"{self.calculator_engine.previous_expression} = {self.calculator_engine.current_expression}")
