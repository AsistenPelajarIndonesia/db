from sqlalchemy import URL
from sqlmodel import Field, SQLModel, create_engine, Session, select
import os


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    email: str
    password: str
    information: str

connection_string = URL.create(
    'postgresql',
    username='admin',
    password=os.environ["password"],
    host='ep-royal-meadow-a14stvyr.ap-southeast-1.pg.koyeb.app',
    database='koyebdb',
)

engine = create_engine(connection_string)
SQLModel.metadata.create_all(engine)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_user(name: str, email: str, password: str, information: str):
    with Session(engine) as session:
        session.add(User(name=name, email=email, password=password, information=information))
        session.commit()

def select_user(name: str) -> User:
    with Session(engine) as session:
        return session.exec(
                select(User).where(User.name == name)
            ).one()

def user_exists(name: str) -> bool:
    import warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    with Session(engine) as session:
        if session.exec(select(User).where(User.name == name)).one():
            return True
        return False

def update_user(name:str, property_name: str, property_value: str) -> None:
    with Session(engine) as session:
        statement = select(User).where(User.name == name)
        results = session.exec(statement)
        user = results.one()
        exec(f"user.{property_name} = {property_value}")
        session.add(user)
        session.commit()
        session.refresh(user)

def delete_user(name: str) -> None:
    with Session(engine) as session:
        session.delete(session.exec(select(User).where(User.name == name)).one())
        session.commit()
