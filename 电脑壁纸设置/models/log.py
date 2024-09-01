from loguru import logger
from pathlib import Path
import datetime


LOG = Path(__file__).parent.parent / "log"
LOG.mkdir(exist_ok=True)

logDir = LOG / f"{datetime.datetime.now():%Y-%m-%d_%H-%M-%S}"
logDir.mkdir(exist_ok=True)

# logger.add(
#     f"{logDir}/DEBUG.log",
#     level="DEBUG",
# )
# logger.add(
#     f"{logDir}/INFO.log",
#     level="INFO",
# )
# logger.add(
#     f"{logDir}/WARNING.log",
#     level="WARNING",
# )
# logger.add(
#     f"{logDir}/ERROR.log",
#     level="ERROR",
# )
# logger.add(
#     f"{logDir}/CRITICAL.log",
#     level="CRITICAL",
# )
