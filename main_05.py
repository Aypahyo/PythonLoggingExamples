import logging
from pythonjsonlogger import jsonlogger

class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        log_record['foo'] = 'bar'  
        log_record['extra'] = 'fields'


logger = logging.getLogger(__name__)
logger.setLevel(1) # This logger will log everything
log_handler = logging.StreamHandler()

formatter = CustomJsonFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(foo)s - %(extra)s')

log_handler.setFormatter(formatter)
logger.addHandler(log_handler)

logger.info('msg: %s', 'Hello from main_05.py')

#python main_05.py > main_05_stdout.json 2> main_05_stderr.json