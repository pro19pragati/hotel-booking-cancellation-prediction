from src.logger.logger import logger
from src.exception.exception import CustomException
import sys

try:
    logger.info("Testing Exception Handling")

    a = 10
    b = 0

    print(a / b)

except Exception as e:
    logger.error(CustomException(e, sys))
    print(CustomException(e, sys))