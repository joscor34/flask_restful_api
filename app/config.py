class Config:
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://admin:mi_admin123@172.18.48.1:5432/mi_almacen'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SECRET_KEY = 'b6179c99d205dc3798d5d00bd762e7f9'
  JWT_ALGORITHM = 'HS256'
