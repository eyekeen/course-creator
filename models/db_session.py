from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

SqlAlchemyBase = declarative_base()
__factory = None


def global_init(db_file):
    global __factory

    if __factory:
        return
    conn_str = f"sqlite:///{db_file}"
    engine = create_engine(conn_str)
    __factory = sessionmaker(bind=engine)
    from . import __all_models
    SqlAlchemyBase.metadata.create_all(engine)


def create_session():
    global __factory
    return __factory()