import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

#! Important
from dotenv import load_dotenv

#Load enviroment variables from .env file
load_dotenv()