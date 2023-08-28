import logging

class Logger_Demo:

    def sample_logger(self):

        # create logger
        logger = logging.getLogger(Logger_Demo.__name__)
        logger.setLevel(logging.DEBUG)

        # create stream handler or file handler
        #ch = logging.StreamHandler()
        fh = logging.FileHandler("demolog1.log")

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s -%(name)s : %(message)s')

        # add formatter to the file handler
        fh.setFormatter(formatter)

        # add console handler to logger
        logger.addHandler(fh)

        # log messages
        logger.debug("debug log statement")
        logger.info("info log statement")
        logger.warning("warning log statement")
        logger.error("error log statement")
        logger.critical("critical log statement")



ld = Logger_Demo()
ld.sample_logger()