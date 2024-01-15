import logging
def check():
    return logging.debug(f"Privet are you print ?")


logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
check()