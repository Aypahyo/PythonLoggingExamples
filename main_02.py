import logging
import sys

# CRITICAL = 50
# FATAL = CRITICAL
# ERROR = 40
# WARNING = 30
# WARN = WARNING
# INFO = 20
# DEBUG = 10
# NOTSET = 0

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO) # No log_handler will get anything below INFO
#python main_02.py > main_02_stdout 2> main_02_stderr

log_handler_stderr = logging.StreamHandler() # Default is sys.stderr
log_handler_stderr.setLevel(logging.ERROR) # This log handler will only get ERROR and above

log_handler_stdout = logging.StreamHandler(stream=sys.stdout)
log_handler_stdout.setLevel(logging.NOTSET) # This log handler wants everything, but is limited by the logger's level to INFO and above

logger.addHandler(log_handler_stderr)
logger.addHandler(log_handler_stdout)

logger.log(19, '19 Below INFO')          # logger will not log this
logger.info('20 Hello from main_02.py')  # stdout
logger.log(21, '21 Above INFO')          # stdout
logger.log(39, '39 Below ERROR')         # stdout
logger.error('40 Error from main_02.py') # stdout, stderr
logger.log(41, '41 Above ERROR')         # stdout, stderr