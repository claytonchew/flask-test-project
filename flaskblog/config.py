import os


class Config:
    # SECRET_KEY = os.environ.get("SECRET_KEY")
    SECRET_KEY = "ddd8a4bae57a7f36446e848c4d0c94b415374e93b242515e7aa9d13543aa6c39"

    # SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"

    # Mail Settings

    MAIL_SERVER = "smtp.googlemail.com"

    MAIL_PORT = 587

    MAIL_USE_TLS = True

    MAIL_USERNAME = os.environ.get("EMAIL_USER")

    MAIL_PASSWORD = os.environ.get("EMAIL_PASS")
