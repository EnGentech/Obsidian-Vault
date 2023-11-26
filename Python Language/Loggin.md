video link: [(31) Python Tutorial: Logging Basics - Logging to Files, Setting Levels, and Formatting - YouTube](https://www.youtube.com/watch?v=-ARI4Cz-awo)

real_python link: [Logging in Python – Real Python](https://realpython.com/python-logging/)

formatter values:
Here is the information you provided formatted in a table markup language:

| Attribute name | Format      | Description                                                                                                        |
|----------------|-------------|--------------------------------------------------------------------------------------------------------------------|
| args           | N/A         | You shouldn’t need to format this yourself.                                                                        |
| asctime        | %(asctime)s | Human-readable time when the LogRecord was created. By default this is of the form '2003-07-08 16:49:45,896'.       |
| created        | %(created)f | Time when the LogRecord was created (as returned by time.time()).                                                  |
| exc_info       | N/A         | Exception tuple (à la sys.exc_info) or, if no exception has occurred, None.                                        |
| filename       | %(filename)s| Filename portion of pathname.                                                                                      |
| funcName       | %(funcName)s| Name of function containing the logging call.                                                                      |
| levelname      | %(levelname)s| Text logging level for the message ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').                                |
| levelno        | %(levelno)s | Numeric logging level for the message (DEBUG, INFO, WARNING, ERROR, CRITICAL).                                      |
| lineno         | %(lineno)d  | Source line number where the logging call was issued (if available).                                               |
| message        | %(message)s | The logged message, computed as msg % args. This is set when Formatter.format() is invoked.                        |
| module         | %(module)s  | Module (name portion of filename).                                                                                |
| msecs          | %(msecs)d   | Millisecond portion of the time when the LogRecord was created.                                                     |
| msg            | N/A         | The format string passed in the original logging call. Merged with args to produce message, or an arbitrary object. |
| name           | %(name)s    | Name of the logger used to log the call.                                                                           |
| pathname       | %(pathname)s| Full pathname of the source file where the logging call was issued (if available).                                 |
| process        | %(process)d | Process ID (if available).                                                                                        |
| processName    | %(processName)s| Process name (if available).                                                                                     |
| relativeCreated| %(relativeCreated)d| Time in milliseconds when the LogRecord was created, relative to the time the logging module was loaded.         |
| stack_info     | N/A         | Stack frame information (where available) from the bottom of the stack in the current thread.                    |
| thread         | %(thread)d  | Thread ID (if available).                                                                                         |
| threadName     | %(threadName)s| Thread name (if available).                                                                                       |
| taskName       | %(taskName)s| asyncio.Task name (if available).                                                                                  |

