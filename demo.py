from liveSensor.exception import SensorException
from liveSensor.logger import logging
import sys
try:
    
    a=5
    b=0
    a/b
    logging.info("please check once the issue update issue")
except Exception as e:
    raise SensorException(e,sys)
    
