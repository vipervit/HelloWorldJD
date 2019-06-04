import logging

logger = logging.getLogger(__path__[0])
logger.setLevel(logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logger.addHandler(console)
