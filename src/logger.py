import logging
import os
import pytz
from datetime import datetime

timezone_ind= pytz.timezone('Asia/Kolkata')

ist_local = datetime.now(timezone_ind)


LOG_FILE=f"{ist_local.strftime('%d_%m_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs")
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(filename)s:%(lineno)s %(funcName)s() %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

if __name__=="__main__":
    logging.info("Logging has started")
