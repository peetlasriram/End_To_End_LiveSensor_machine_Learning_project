import logging
import os
import sys
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('@m_@d_%Y_%H_%M_%S')}.logs"

Log_file=os.path.join(os.getcwd(),"logs",LOG_FILE)

os.makedirs(Log_file,exist_ok=True)

LOG_FILENAME=os.path.join(Log_file,LOG_FILE)

logging.basicConfig(level=logging.INFO,filename=LOG_FILENAME,format='%(asctime)s-%(lineno)d-%(message)s-%(levelname)s')