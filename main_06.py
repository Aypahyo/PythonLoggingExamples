import logging
from pythonjsonlogger import jsonlogger
from opentelemetry import trace

class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        log_record['trace_id'] = trace.get_current_span().get_span_context().trace_id
        log_record['span_id'] = trace.get_current_span().get_span_context().span_id
        log_record['trace_flags'] = trace.get_current_span().get_span_context().trace_flags

logger = logging.getLogger(__name__)
logger.setLevel(1) # This logger will log everything
log_handler = logging.StreamHandler()

formatter = CustomJsonFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(trace_id)s - %(span_id)s - %(trace_flags)s')

log_handler.setFormatter(formatter)
logger.addHandler(log_handler)

logger.info('msg: %s', 'Hello from main_06.py')

#python main_06.py > main_06_stdout.json 2> main_06_stderr.json