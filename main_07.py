import logging
from pythonjsonlogger import jsonlogger
from opentelemetry import trace


def get_CustomFormatter() -> jsonlogger.JsonFormatter:
    class CustomJsonFormatter(jsonlogger.JsonFormatter):
        def add_fields(self, log_record, record, message_dict):
            super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
            log_record['trace_id'] = trace.get_current_span().get_span_context().trace_id
            log_record['span_id'] = trace.get_current_span().get_span_context().span_id
            log_record['trace_flags'] = trace.get_current_span().get_span_context().trace_flags
    return CustomJsonFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(trace_id)s - %(span_id)s - %(trace_flags)s')

def get_StdErrHandler(formatter: logging.Formatter) -> logging.StreamHandler:
    log_handler = logging.StreamHandler()
    log_handler.setFormatter(formatter)
    return log_handler

def get_Logger(name: str, level: int, handler: logging.StreamHandler) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)
    #clear handlers - useful for testing since the logger is a singleton and adding a handler will persist
    for h in logger.handlers:
        logger.removeHandler(h)
    logger.addHandler(handler)
    return logger

class BusinessClass:
    def __init__(self, logger: logging.Logger = None):
        if logger is None:
            logger = get_Logger(__name__, 1, get_StdErrHandler(get_CustomFormatter()))
        self.logger = logger

    def do_business(self):
        self.logger.info('msg: %s', 'Hello from BusinessClass.do_business')

bc = BusinessClass()
bc.do_business()

#prefere pytest caplog to capture logs
#https://docs.pytest.org/en/7.1.x/how-to/logging.html
#the option below shows how a custom logHandler can be used for testing

class CustomHandler(logging.Handler):
    def __init__(self):
        self.logs = []
        super().__init__()
    
    def emit(self, record):
        self.logs.append(self.format(record))

def get_CustomHandler(formatter: logging.Formatter) -> logging.StreamHandler:
    log_handler = CustomHandler()
    log_handler.setFormatter(formatter)
    return log_handler

test_handler = get_CustomHandler(get_CustomFormatter())

bc_unit_under_test = BusinessClass(get_Logger(__name__, 1, test_handler))
bc_unit_under_test.do_business()

assert len(test_handler.logs) == 1

#python main_07.py > main_07_stdout.json 2> main_07_stderr.json