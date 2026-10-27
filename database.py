from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Reemplaza 'root' y '' con tu usuario y contraseña de MySQL si los configuraste distintos
DATABASE_URL = "mysql+pymysql://root:Cvghuikl123zxc!@localhost/login_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()