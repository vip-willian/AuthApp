from sqlalchemy.orm import declarative_base
from models.engine import metadata
import asyncio
from datetime import datetime

BaseModel = declarative_base(metadata=metadata)
