import os
user:str = os.environ.get("USER")
password:str = os.environ.get("PASSWORD")
host:str = os.environ.get("HOST")

SINAU_DB = f"mysql+pymysql://{user}:{password}@{host}/sinau?charset=utf8mb4"
AUTH_DB = f"mysql+pymysql://{user}:{password}@{host}/auth?charset=utf8mb4"
MUNAQASYAH_DB = f"mysql+pymysql://{user}:{password}@{host}/munaqasyah?charset=utf8mb4" 