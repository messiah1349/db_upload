from .transferer import Base, get_postgres_engine, get_sqlite_engine
from sqlalchemy import MetaData, create_engine, Column, Integer, String, DateTime, Float, BOOLEAN

BD_PATH = './data/main.db'
#
# class Mark(Base):
#
#     __tablename__ = 'mark'
#     id = Column(Integer, primary_key=True)
#     telegram_id = Column(Integer)
#     mark = Column(Integer)
#     mark_time = Column(DateTime)
#
#
# class User(Base):
#
#     __tablename__ = 'user'
#     telegram_id = Column(Integer, primary_key=True)
#     frequency = Column(Integer)
#     start_hour = Column(Integer)
#     end_hour = Column(Integer)
#     minute = Column(Integer)
#     active_flag = Column(BOOLEAN)

def transfer_tables():
    postgres_engine = get_postgres_engine()
    sqllite_engine = get_sqlite_engine(BD_PATH)

    metadata = MetaData()
    metadata.reflect(bind=sqllite_engine)

    metadata.create_all(postgres_engine)
