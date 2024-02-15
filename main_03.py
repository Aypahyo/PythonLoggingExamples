import logging

logger = logging.getLogger(__name__)
logger.setLevel(1) # This logger will log everything
log_handler = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#asctime - Time when the LogRecord was created
#name - Name of the logger used to log the call.
#levelname - Text logging level for the message ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
#message - The logged message, computed as msg % args. This is set when Formatter.format() is invoked.

log_handler.setFormatter(formatter)
logger.addHandler(log_handler)

#By passing the format and args, formatting is usually done outside if the main thread
logger.info('msg: %s', 'Hello from main_03.py')

#python main_03.py > main_03_stdout 2> main_03_stderr