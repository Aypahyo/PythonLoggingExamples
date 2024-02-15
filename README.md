# Python Logging Examples

This project contains a collection of examples illustrating different approaches to logging in Python. The examples cover basic logging configurations, logging to different destinations, and using various logging levels. Each example is designed to provide practical code snippets that can be easily integrated into your projects.

## Example Summaries

## Example 1: Basic Logging to stdout and stderr

* Filename: main_01.py
* Description: This example demonstrates the simplest form of logging by printing messages directly to stdout and stderr. It highlights how to differentiate between standard output for informational messages and standard error for error messages. This method is straightforward but lacks the flexibility and features of the built-in logging module.
* Key Concepts:
  * Printing to stdout using print().
  * Redirecting error messages to stderr using the file=sys.stderr argument in the print() function.
* Usage:
  * To capture stdout: Redirect the standard output to a file named main_01_stdout by running python main_01.py > main_01_stdout.
  * To capture stderr: Redirect the standard error output to a file named main_01_stderr by running python main_01.py 2> main_01_stderr.

## Example 2: Advanced Logging with Handlers for stdout and stderr

* Filename: main_02.py
* Description: This example showcases the use of Python's built-in logging module to create a more sophisticated logging setup. It configures two separate log handlers to direct log messages to stdout and stderr based on their severity. This approach allows for fine-grained control over where messages are output based on their log level, demonstrating a common pattern in more complex applications where different types of logs need to be routed to different destinations.
* Key Concepts:
  * Introduction to the logging module and its basic configuration.
  * Setting a base log level on the logger to filter messages globally.
  * Differentiating between log levels to direct messages to stdout or stderr.
  * Configuring multiple handlers with different severity thresholds for log messages.
    Usage:
  * To capture stdout: Execute python main_02.py > main_02_stdout to redirect standard output messages to a file.
  * To capture stderr: Use python main_02.py 2> main_02_stderr to redirect error messages to a separate file.
* Behavior:
  * Messages with a log level of INFO (20) and above are processed by the logger.
  * The stdout handler captures all messages of level INFO and above, due to its NOTSET level, effectively allowing it to inherit the logger's level.
  * The stderr handler is set to capture only ERROR (40) and above, demonstrating how to segregate more critical messages.
  * Specific messages are directed accordingly, showcasing how different log levels affect the routing of log messages.

### Example 3: Logging with Custom Formatter

* Filename: `main_03.py`
* Description: This example demonstrates how to use the `logging` module to implement logging with a custom formatter. It configures a logger to log all levels of messages and applies a specific format to the log output. The formatter includes the timestamp (`%(asctime)s`), logger name (`%(name)s`), log level (`%(levelname)s`), and the log message (`%(message)s`). This setup enhances the readability and utility of the log output, making it easier to understand the context and severity of each log message.

* Key Concepts:
  * Configuring a logger to capture all levels of log messages by setting the log level to the lowest possible value.
  * Utilizing `logging.Formatter` to define a custom format for log messages, including important metadata like the time of the log entry, the logger's name, the message's severity level, and the log message itself.
  * The importance of formatter in enhancing log message readability and providing contextual information for better log analysis.

* Usage:
  * To capture stdout: Run `python main_03.py > main_03_stdout` to direct the output to a file, capturing the formatted log messages.
  * To capture stderr: Use `python main_03.py 2> main_03_stderr` if expecting error logs to be captured separately; however, this example primarily focuses on stdout output.

This example is particularly useful for applications requiring detailed logs for debugging or monitoring, showing how to include a wealth of information in each log entry for comprehensive logging.

### Example 4: Logging with JSON Formatter

* Filename: `main_04.py`
* Description: This example leverages the `pythonjsonlogger` library to configure a logger that outputs log messages in JSON format. It sets the log level to the lowest possible value to capture all log messages. The `JsonFormatter` is used to format the log messages as JSON, making the logs easily parseable by log management tools and suitable for processing in modern logging pipelines.

* Key Concepts:
  * Use of the `pythonjsonlogger` library to output log messages in a structured JSON format.
  * Configuration of a custom JSON formatter that includes the timestamp, logger name, log level, and message, enhancing both human readability and machine parsability.
  * Demonstrates how structured logging can be beneficial in environments where logs are ingested and analyzed by automated systems.

* Usage:
  * To capture stdout: Execute `python main_04.py > main_04_stdout.json` to save the JSON formatted log output to a file.
  * To capture stderr: If needed, run `python main_04.py 2> main_04_stderr.json` to separately capture error logs in JSON format.

This example is ideal for applications that require structured logging for efficient log analysis and monitoring, showcasing the integration of structured logging within a Python application.

### Example 5: Custom JSON Formatter with Additional Fields

* Filename: `main_05.py`
* Description: This example extends the use of the `pythonjsonlogger` library by implementing a custom JSON formatter. By subclassing `jsonlogger.JsonFormatter`, it introduces additional fields (`foo` and `extra`) into the log output, thereby demonstrating how to enrich log messages with custom data. This customization allows for more detailed logs that can carry extra contextual information beyond the standard log message format.

* Key Concepts:
  * Creation of a `CustomJsonFormatter` class that inherits from `jsonlogger.JsonFormatter` and overrides the `add_fields` method to inject custom fields into the log records.
  * The custom formatter adds specific static values (`'bar'` for `foo` and `'fields'` for `extra`), showcasing how to include additional information in every log entry.
  * This example illustrates the flexibility of structured logging and how it can be tailored to include any relevant information that the application needs to log.

* Usage:
  * To capture stdout: Use `python main_05.py > main_05_stdout.json` to output the enriched JSON formatted logs to a file.
  * To capture stderr: If necessary, run `python main_05.py 2> main_05_stderr.json` to capture any error logs with the custom formatting.

Ideal for scenarios where logs need to include more context or metadata, this example provides a blueprint for enhancing log messages with custom attributes in a structured and parseable format.

### Example 6: Integrating Logging with OpenTelemetry for Trace Context

* Filename: `main_06.py`
* Description: This example demonstrates the integration of logging with OpenTelemetry to include trace context information (trace ID, span ID, and trace flags) in log messages. By using a custom JSON formatter, it enriches the logs with trace context, facilitating the correlation of log messages with specific traces. This approach is particularly useful in distributed systems where tracing and logging provide complementary visibility into the behavior and performance of the system.

* Key Concepts:
  * Modification of the `CustomJsonFormatter` class to extract and include OpenTelemetry trace context information (`trace_id`, `span_id`, `trace_flags`) in each log entry.
  * Utilization of the `opentelemetry` library to access the current trace context, highlighting the synergy between logging and tracing in observability practices.
  * This example underscores the importance of trace context in logs for debugging and monitoring distributed applications, enabling easier identification and analysis of specific request flows.

* Usage:
  * To capture stdout: Run `python main_06.py > main_06_stdout.json` to save the log output, which now includes trace context, in JSON format to a file.
  * To capture stderr: If error logs are expected, execute `python main_06.py 2> main_06_stderr.json` to capture them separately, also enriched with trace context.

Ideal for developers and operators of distributed systems, this example showcases how to augment logging with trace context, thus enhancing the observability and debuggability of applications by linking log entries with specific traces.

### Example 7: Logging with OpenTelemetry Trace Context in Test Environments

* Filename: `main_07.py`
* Description: This comprehensive example showcases advanced logging practices in Python, integrating OpenTelemetry for trace context and demonstrating a flexible logging setup suitable for both production and testing environments. It includes custom logging formatter to enrich log entries with trace context, a pattern for initializing loggers with different handlers, and a specialized logging handler for unit testing that collects log messages in-memory for assertions.

* Key Concepts:
  * The use of factory functions (`get_CustomFormatter`, `get_StdErrHandler`, and `get_Logger`) to create and configure loggers and handlers with custom formatting and behavior. This approach enhances code reuse and flexibility.
  * Integration with OpenTelemetry to include trace ID, span ID, and trace flags in logs, improving the observability of distributed applications.
  * Implementation of a `CustomHandler` for testing, which captures log entries in a list, allowing for easy assertions on logged messages in unit tests. This technique is particularly useful for verifying logging behavior during automated testing.
  * Demonstrates best practices for configuring and using loggers in a modular application, including how to cleanly handle logger initialization in classes that may be used in different contexts (e.g., production, development, testing).

* Usage:
  * Primarily designed for a development environment with an emphasis on testing logging output. The example includes instructions for using pytest's `caplog` fixture as the preferred method for capturing and asserting log messages in tests, alongside demonstrating a custom approach for scenarios where `caplog` might not be suitable.
  * To capture stdout and stderr: While the main focus is on testing, standard output and error can still be redirected to JSON files (`main_07_stdout.json`, `main_07_stderr.json`) to observe the log output structure and content.

This example is particularly valuable for developers looking to implement sophisticated logging mechanisms that support both operational logging and testability, illustrating how to build a logging setup that is both flexible and easily testable.
