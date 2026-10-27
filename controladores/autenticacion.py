from database import SessionLocal
from modelos import UsuarioModel

class ServicioAutenticacion:
    def __init__(self):
        pass
    
    def iniciar_sesion(self, email, contrasenia):
        db = SessionLocal()
        try:
            usuario = db.query(UsuarioModel).filter(UsuarioModel.email == email).first()
            if usuario and usuario.contrasenia == contrasenia:
                return True
            return False
        finally:
            db.close()
    
    def registrar_usuario(self, email, contrasenia):
        db = SessionLocal()
        try:
            # Verificar si el usuario ya existe en la base de datos
            usuario_existente = db.query(UsuarioModel).filter(UsuarioModel.email == email).first()
            if usuario_existente:
                return False
            
            # Crear y guardar el nuevo usuario
            nuevo_usuario = UsuarioModel(email=email, contrasenia=contrasenia)
            db.add(nuevo_usuario)
            db.commit()
            return True
        except Exception:
            db.rollback()
            return False
        finally:
            db.close()