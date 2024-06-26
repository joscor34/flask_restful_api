from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager # type: ignore

# Creamos una instancia de la DB
db = SQLAlchemy()

# Creamos una instancia de JWT
jwt = JWTManager()