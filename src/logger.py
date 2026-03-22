import logging
import os
from config import LOG_FILE

os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

logging.basicConfig(
     filename=LOG_FILE,
     level=logging.INFO, 
     format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
 )

logger = logging.getLogger(__name__)