from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Exercise(Base):
    __tablename__ = 'exercises'
    id = Column(Integer, primary_key=True, index=True)
    exercise_name = Column(String, index=True)
    weight = Column(Float)
    reps = Column(Integer)
    sets = Column(Integer)

# Configuração do banco de dados
DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criar tabelas no banco de dados
def init_db():
    Base.metadata.create_all(bind=engine)
