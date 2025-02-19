from starlette.config import Config

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fastapi import FastAPI

from minio import Minio
from db import models
import user_router, emote_router
from db import db_setup

models.Base.metadata.create_all(bind=db_setup.engine)


# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread":False}, future=True)
#
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

app = FastAPI()
app.include_router(user_router.router)
app.include_router(emote_router.router)



