from utils.sql_api import DB
from loguru import logger

logger.add(
    "logs.log",
    rotation="10 MB",
    retention="15 days",
    compression="zip",
    level="INFO"
)

db = DB()

__all__ = ["db", "logger"]