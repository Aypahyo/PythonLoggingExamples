import logging
from pythonjsonlogger import jsonlogger

logger = logging.getLogger(__name__)
logger.setLevel(1) # This logger will log everything
log_handler = logging.StreamHandler()

formatter = jsonlogger.JsonFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

log_handler.setFormatter(formatter)
logger.addHandler(log_handler)

logger.info('msg: %s', 'Hello from main_04.py')

#python main_04.py > main_04_stdout.json 2> main_04_stderr.json