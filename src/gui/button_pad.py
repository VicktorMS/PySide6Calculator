from PySide6.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout, QWidget


class ButtonPad(QWidget):
    def __init__(self, calculator_engine):
        super().__init__()
        self.create_button_pad()
        self.calculator_engine = calculator_engine

    def create_button(self, text):
        btn = QPushButton(text)
        btn.setMinimumSize(45, 50)
        font = self.font()
        font.setPointSize(14)
        btn.setFont(font)
        return btn

    # def create_clear_button(self, text):
    #     btn = self.create_button(text)
    #     btn.clicked.connect(lambda: self.calculator.on_button_press("PENES")) # Call Clear Display Function

    def create_common_button(self, text):
        button = self.create_button(text)
        button.clicked.connect(lambda: self.calculator_engine.on_common_button_click(button.text()))
        return button

    def create_clear_button(self, text):
        button = self.create_button(text)
        button.clicked.connect(lambda: self.calculator_engine.on_clear_button_click())
        return button

    def create_equal_button(self, text):
        button = self.create_button(text)
        button.clicked.connect(lambda: self.calculator_engine.on_equal_button_click())
        return button

    def create_button_layout(self, button_texts):
        layout = QHBoxLayout()
        for text in button_texts:
            if text == "CE":
                layout.addWidget(self.create_clear_button(text))
            elif text == "=":
                layout.addWidget(self.create_equal_button(text))
            else:
                layout.addWidget(self.create_common_button(text))
        return layout

    def create_button_pad(self):
        main_layout = QVBoxLayout()
        button_rows = [
            ["CE", "(", ")", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "+"],
            ["1", "2", "3", "-"],
            ["%", "0", ".", "="]
        ]

        for row in button_rows:
            main_layout.addLayout(self.create_button_layout(row))

        self.setLayout(main_layout)




