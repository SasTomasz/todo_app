import logging

logging.basicConfig(filename="./logs.log",
                    format='%(asctime)s %(message)s',
                    filemode='a',
                    encoding='utf-8',
                    level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
