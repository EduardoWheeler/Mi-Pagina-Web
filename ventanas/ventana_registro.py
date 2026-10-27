from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.uic import loadUi
from controladores.autenticacion import ServicioAutenticacion

class VentanaRegistro(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("ventanas/registro.ui", self)
        self.auth = ServicioAutenticacion()
        
        self.btn_registrar.clicked.connect(self.handle_registro)
        self.btn_volver.clicked.connect(self.volver_login)
    
    def handle_registro(self):
        email = self.txt_email.text()
        contrasenia = self.txt_password.text()
        
        if self.auth.registrar_usuario(email, contrasenia):
            QMessageBox.information(self, "Éxito", "Usuario registrado correctamente")
            self.volver_login()
        else:
            QMessageBox.warning(self, "Error", "El usuario ya existe")
    
    def volver_login(self):
        from ventanas.ventana_login import VentanaLogin
        self.ventana_login = VentanaLogin()
        self.ventana_login.show()
        self.close()