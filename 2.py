from dirsync import sync
import logging
import time
source_path = input("source path:")
target_path = input("target path:")
log_path = input("log path:")
sec = input("time period in sec:")
while True:
    try:
        logging.basicConfig(filename=log_path, level=logging.DEBUG)
        log = logging.getLogger('dirsync')
        sync(source_path, target_path, 'diff',logger=log)
        sync(source_path, target_path, 'sync',verbose=True)
        time.sleep(int(sec))
    except KeyboardInterrupt:
        break
