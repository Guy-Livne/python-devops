import logging
import sys
from pythonjsonlogger.json import JsonFormatter

logger = logging.getLogger("worker_pool")
logger.setLevel(logging.INFO)
logger.handlers.clear()

handler = logging.StreamHandler(sys.stdout)
formatter = JsonFormatter()
handler.setFormatter(formatter)
logger.addHandler(handler)

context_data = {"task_id": "t-456", "worker_id": "w-03"}

logger.info("Task completed successfully", context_data)