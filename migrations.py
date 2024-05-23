from Muna.Model.auth import Base as AuthBase
from Muna.Model.sinau import Base as SinauBase
from Muna.Model.munaqasyah import Base as MunaqasyahBase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from django.conf import settings


def migrate_auth():
    engine = create_engine(settings.DATABASE_URL['AUTH'])
    AuthBase.metadata.create_all(engine)

def migrate_sinau():
    engine = create_engine(settings.DATABASE_URL['SINAU'])
    SinauBase.metadata.create_all(engine)

def migrate_munaqasyah():
    engine = create_engine(settings.DATABASE_URL['MUNAQASYAH'])
    MunaqasyahBase.metadata.create_all(engine)

migrate_auth()
migrate_sinau()
migrate_munaqasyah()