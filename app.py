from liveSensor.logger import logging
from liveSensor.exception import SensorException
import os
import logging
from liveSensor.utils.main_utils import dump_csv_to_mongo_db




if __name__=="__main__":

    file_path=r"C:\End_To_End_LiveSensor_machine_Learning_project\data\aps_failure_training_set1.csv"
    database_name="sensor_database"
    collection_name="sensorcollectiion"
    dump_csv_to_mongo_db(file_path,database_name,collection_name)



