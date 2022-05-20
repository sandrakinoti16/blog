import os
# from dotenv import load_dotenv
# load_dotenv()
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sandra:12345@localhost/blog'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    DEBUG = True
class ProdConfig(Config):
    """
    production configuration child class
    """
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sandra:12345@localhost/blog'
    DEBUG = True
class DevConfig(Config):
    """
    development configuration child class
    """
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sandra:12345@localhost/blog'
config_options = {
'development':DevConfig,
'production':ProdConfig
}
# class ProdConfig(Config):
#     SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")














