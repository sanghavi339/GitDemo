import logging

logging.basicConfig(filename="..\\errorlog\logs.logs",format='%(asctime)s:, %(levelname)s:, %(message)s', datefmt='%m/%d/%y %I:%M:%S %p',
                    level = logging.INFO)

log =logging.getLogger()

log.info("This is my First Logger Program")
