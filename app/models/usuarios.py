from app.extensions import db # <- Variable que almacena la conexión
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
  __tablename__ = 'usuarios' # <- Esta clase se va a comunicar con la tabla usuarios
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), nullable=False)
  email = db.Column(db.String(120), nullable=False)
  password = db.Column(db.Text(), nullable=False)

  def __repr__(self):
    return f'<Usuario es {self.username}>'

    
                        # La contraseña en texto plano
  def set_password(self, password):
    # Agarra el atributo password(esta llegando a la db) y lo sobreescribe
    # con el hash generado
    self.password = generate_password_hash(password)
  
  def check_password(self, password):
    # Esta función compara la contraseña que le hace llegar un usuario
    # con la contraseña en la DB
    return check_password_hash(self.password, password)

  # Este método va a acceder a la clase en si y buscará un usuario por su email
  @classmethod
  def get_user_by_email(cls, email):
    return cls.query.filter_by(email=email).first()
  
  # Este método va a guardar un usuario creado en la db
  def save(self):
    db.session.add(self)
    db.session.commit()
  
  # Este método va a borrar un usuario creado en la db
  def delete(self):
    db.session.delete(self)
    db.session.commit()
