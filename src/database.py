from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///db/email.db"

engine = create_engine(DATABASE_URL, echo=False)