from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.uic import loadUi
from controladores.autenticacion import ServicioAutenticacion
from ventanas.ventana_registro import VentanaRegistro
from ventanas.ventana_principal import VentanaPrincipal

class VentanaLogin(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("ventanas/login.ui", self)
        self.auth = ServicioAutenticacion()
        
        self.btn_login.clicked.connect(self.handle_login)
        self.btn_ir_registro.clicked.connect(self.ir_registro)
    
    def handle_login(self):
        email = self.txt_email.text()
        contrasenia = self.txt_password.text()
        
        if self.auth.iniciar_sesion(email, contrasenia):
            self.ventana_principal = VentanaPrincipal(email)
            self.ventana_principal.show()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Credenciales incorrectas")
    
    def ir_registro(self):
        self.ventana_registro = VentanaRegistro()
        self.ventana_registro.show()
        self.close()