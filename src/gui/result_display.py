from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLineEdit, QHBoxLayout


class ResultDisplay(QWidget):
    def __init__(self, calculator_engine):
        super().__init__()
        self.line_edit = None
        self.calculator_engine = calculator_engine
        self.create_display()
        self.display_handler()

    def display_handler(self):
        self.line_edit.textEdited.connect(self.display_edited)
        self.line_edit.returnPressed.connect(self.calculator_engine.calculate_expression)
        self.calculator_engine.current_expression_changed.connect(self.update_line_edit_text)

    def display_edited(self):
        self.calculator_engine.current_expression = self.line_edit.text()

    def create_display(self):
        main_layout = QHBoxLayout()
        self.line_edit = QLineEdit()
        self.line_edit.setMinimumHeight(50)
        self.line_edit.setAlignment(Qt.AlignRight)

        font = self.line_edit.font()
        font.setPointSize(16)

        self.line_edit.setFont(font)
        main_layout.addWidget(self.line_edit)
        self.setLayout(main_layout)

    def update_line_edit_text(self, new_text):
        self.line_edit.setText(new_text)
        self.line_edit.setFocus()
