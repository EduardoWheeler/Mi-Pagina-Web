# Desktop Authentication System (PyQt6 & MySQL)

A modular desktop application built with Python and PyQt6 featuring user authentication, secure navigation, and persistent data storage using MySQL and SQLAlchemy.

## 🚀 Features
- **User Authentication:** Secure login and registration flow connected to a relational database.
- **Layered Architecture:** Clear separation of concerns between UI views, controllers, data models, and database sessions.
- **Modern UI Styling:** Custom dark theme applied globally via Qt Style Sheets (QSS).
- **Database Persistence:** ORM mapping and session management using SQLAlchemy and MySQL.

## 🛠️ Tech Stack
- **Language:** Python
- **GUI Framework:** PyQt6 (Qt Designer UI files)
- **Database ORM:** SQLAlchemy
- **Database:** MySQL / PyMySQL

## 📂 Project Structure
```text
login_registro/
│
├── controladores/
│   └── autenticacion.py
├── ventanas/
│   ├── estilos.qss
│   ├── login.ui
│   ├── registro.ui
│   ├── ventana_login.py
│   ├── ventana_principal.py
│   └── ventana_registro.py
├── database.py
├── modelos.py
├── main.py
├── requirements.txt
└── README.md