import sys
from PyQt6.QtWidgets import QApplication
from database import engine, Base
from ventanas.ventana_login import VentanaLogin

def main():
    # Crea las tablas en MySQL automáticamente si no existen
    Base.metadata.create_all(bind=engine)

    app = QApplication(sys.argv)
    
    try:
        with open("ventanas/estilos.qss", "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        pass
    
    login = VentanaLogin()
    login.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()