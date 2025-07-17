import os
import sys
from fastapi import FastAPI

sys.path.append(os.path.dirname(__file__))
from api.foo import foo_router
from api.bar import bar_router


app = FastAPI()