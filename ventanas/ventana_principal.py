from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

class VentanaPrincipal(QWidget):
    def __init__(self, email=""):
        super().__init__()
        self.setWindowTitle("Panel Principal")
        self.resize(600, 400)
        
        layout = QVBoxLayout()
        self.label = QLabel(f"¡Bienvenido al sistema!\nSesión iniciada con: {email}")
        layout.addWidget(self.label)
        self.setLayout(layout)