import os

SQLALCHEMY_DATABASE_URI = os.environ.get(
    "SQLALCHEMY_DATABASE_URI",
    "postgresql+psycopg://otus_user:otus_pass@localhost:5432/hw_06",
)
SQLALCHEMY_ECHO = False  # Turn off SQLAlchemy echoing
