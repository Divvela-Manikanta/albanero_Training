import logging

logging.basicConfig(filename='app.log',filemode='a',format = '%(levelname)s:%(asctime)s:%(message)s')

logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
logging.debug('This is a debug message')



logging.warning('This will get logged to a file')